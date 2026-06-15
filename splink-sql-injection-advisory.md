# Security disclosure — Unquoted SQL identifier interpolation in Splink

**Project:** Splink (`moj-analytical-services/splink`)
**Affected version:** 4.0.16 (pattern present across 4.x; please confirm earlier)
**Component:** SQL generation in backend `DatabaseAPI` implementations (DuckDB confirmed; Spark/SQLite/Postgres likely analogous)
**Class:** CWE-89 (SQL injection) via unsanitized SQL **identifiers**; on the DuckDB backend this escalates to CWE-22/local file read & write and potential code execution.
**Reporter:** btmaffiliate
**Disclosure:** Full public disclosure, 2026-06-15.

---

## Summary

Splink builds backend SQL using f-string interpolation of **table names, schema names, and
related identifiers** without quoting or validation. Column names and string literals are
already escaped (`splink_dataframe.columns_escaped`, `vertically_concatenate.py` literal
escaping), so this report is scoped narrowly to the **identifier** sinks that are not.

In the normal single-operator library use case this is not a vulnerability: the operator who
supplies the identifiers already controls the host process. **The issue is realized when Splink
is embedded in a multi-tenant or service context** where an untrusted party can influence a
table/schema name (e.g. a hosted record-linkage service that accepts user-supplied dataset or
table identifiers). On a DuckDB backend, SQL injection becomes filesystem access, because DuckDB
SQL can read and write arbitrary files and load extensions.

## Affected sinks (v4.0.16)

- `splink/internals/duckdb/database_api.py`
  - `f"DROP TABLE IF EXISTS {name}"` (delete_table_from_database)
  - `f"PRAGMA table_info('{table_name}');"` (table_exists_in_database — interpolated into a string literal)
  - `CREATE SCHEMA IF NOT EXISTS {output_schema}; SET schema '{output_schema}';` (constructor)
- `splink/internals/blocking.py`
  - `f"select * from {input_tablename}"`
- `splink/internals/dialects.py`, `internals/completeness.py`, `internals/testing.py`
  - `... from {tbl_name}` / `from {table_name}` analogues

(Column identifiers reaching SQL are quoted via `InputColumn`/`columns_escaped`; this report does
**not** claim those are vulnerable.)

## Preconditions / threat model (honest scope)

This is exploitable **only** when **all** of the following hold:
1. Splink runs inside a service/pipeline that accepts identifier strings (table or schema names)
   from a party other than the host operator; and
2. those strings reach one of the sinks above without the caller having quoted/validated them; and
3. the backend is one where SQL grants filesystem reach (DuckDB confirmed).

It is **not** a remote, unauthenticated, or network-reachable issue. Splink is a local library
with no listener. There is no cross-deployment exposure.

## Impact (DuckDB backend)

A controlled identifier such as a table name can terminate the intended statement and append
attacker SQL. DuckDB then permits, on the **host running the linkage job**:
- arbitrary file read: `read_csv_auto('/etc/passwd')`, `read_text(...)`
- arbitrary file write / exfiltration: `COPY (SELECT ...) TO '/path/out'`
- extension load → potential code execution: `INSTALL ...; LOAD ...;`

Scope is that single host and the privileges of the Splink process. No remote reach.

## Proof of concept (local, against an instance you control)

```python
# Demonstrates that an unquoted table identifier breaks out of the generated SQL.
# Run only against your own local DuckDB instance.
from splink import DuckDBAPI
db = DuckDBAPI()
# An identifier supplied by an untrusted caller in a multi-tenant wrapper:
malicious = "x; COPY (SELECT 'pwned') TO '/tmp/splink_poc_proof.txt'; --"
db.delete_table_from_database(malicious)   # reaches f"DROP TABLE IF EXISTS {name}"
# -> /tmp/splink_poc_proof.txt is written, proving statement break-out + file write.
```

## Remediation

1. **Quote all identifiers** before interpolation, using the dialect's identifier quoting
   (sqlglot is already a dependency: `sqlglot.exp.to_identifier(name).sql(dialect=...)`),
   matching how column names are already handled.
2. **Validate** internal table/schema names against a strict allowlist
   (`^[A-Za-z_][A-Za-z0-9_]*$`) — Splink's own temp tables already fit this; reject others.
3. Use parameter binding for the PRAGMA string literal rather than f-string interpolation.
4. Document explicitly that **untrusted input must never be passed as table/schema identifiers**,
   for downstream service builders.

## Suggested CVSS (illustrative)

Local/adjacent, high-privilege-precondition, high impact within host scope. ~6–7 (Medium/High)
depending on deployment. Maintainers to assign.

---

*This report concerns the software only. It is not a claim against any specific deployment or
operator, and no third-party systems were accessed in preparing it.*
