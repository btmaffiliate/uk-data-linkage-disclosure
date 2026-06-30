#!/usr/bin/env python3
# Translate the capstone ("the-whole-picture") into the site's main languages.
# Faithful, hedge-preserving summary + the (English) overview graphic + links to the authoritative English reports/PDF.
import json, pathlib

GFX = pathlib.Path("/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/capstone_embed.txt").read_text()

# Per language: (title, intro/thesis, what-is-NOT-connected, links+machine-translation note)
T = {
 "es": ("Toda la imagen: lo que todo esto significa",
  "Se han documentado dos máquinas. Una <strong>vigila y clasifica</strong> a las poblaciones —el enlace de registros del Estado, las plataformas operativas de Palantir, la fusión de datos del ICE—. La otra las <strong>persuade</strong>: operaciones de influencia financiadas por gobiernos extranjeros que ya alcanzan a la propia IA. <strong>No son una única conspiración, y este trabajo no afirma que lo sean.</strong> Lo que las une es un patrón: los sistemas más importantes —los que vigilan, clasifican y ahora persuaden a poblaciones enteras— funcionan cada vez más <strong>con la supervisión apagada</strong>: contratos a dedo o secretos, sin evaluaciones de impacto, propiedad y financiación extranjera en el extremo operativo y de persuasión, la IA como la capa menos visible, y a nadie se le preguntó.",
  "Dicho con la misma claridad que los hallazgos: <strong>lo que NO está conectado</strong>. No hay vínculo Parscale–Palantir. No hay camarilla de Silicon Valley: una lista difundida de ~85 nombres arrojó una sola conexión ya conocida. Las acusaciones se etiquetan, no se afirman; los mitos se corrigen. Esa disciplina es lo que lo sostiene.",
  "Los informes completos y un PDF descargable están en inglés. Esta es una traducción asistida por máquina; la versión en inglés es la autorizada."),
 "fr": ("Le tableau complet : ce que tout cela révèle",
  "Deux machines ont été documentées. L'une <strong>surveille et trie</strong> les populations — le couplage de fichiers de l'État, les plateformes opérationnelles de Palantir, la fusion de données de l'ICE. L'autre les <strong>persuade</strong> : des opérations d'influence financées par des gouvernements étrangers qui atteignent désormais l'IA elle-même. <strong>Ce n'est pas une seule conspiration, et ce travail ne le prétend pas.</strong> Ce qui les relie est un schéma : les systèmes les plus déterminants — ceux qui surveillent, trient et désormais persuadent des populations entières — fonctionnent de plus en plus <strong>sans contrôle</strong> : contrats de gré à gré ou secrets, aucune évaluation d'impact, propriété et financement étrangers au bout opérationnel et persuasif, l'IA comme couche la moins visible — et personne n'a été consulté.",
  "Dit aussi clairement que les conclusions : <strong>ce qui n'est PAS lié</strong>. Aucun lien Parscale–Palantir. Aucune cabale de la Silicon Valley : une liste diffusée d'environ 85 noms n'a donné qu'un seul lien déjà connu. Les allégations sont étiquetées, non affirmées ; les mythes sont corrigés. C'est cette rigueur qui tient l'ensemble.",
  "Les rapports complets et un PDF téléchargeable sont en anglais. Ceci est une traduction assistée par machine ; la version anglaise fait foi."),
 "de": ("Das Gesamtbild: Worauf alles hinausläuft",
  "Zwei Maschinen wurden dokumentiert. Die eine <strong>überwacht und sortiert</strong> Bevölkerungen — die Datenverknüpfung des Staates, Palantirs operative Plattformen, die Datenfusion der ICE. Die andere <strong>überzeugt</strong> sie: von ausländischen Regierungen finanzierte Einflussoperationen, die nun bis in die KI selbst reichen. <strong>Es ist keine einzige Verschwörung, und diese Arbeit behauptet das nicht.</strong> Was sie verbindet, ist ein Muster: die folgenreichsten Systeme — jene, die ganze Bevölkerungen überwachen, sortieren und nun überzeugen — laufen zunehmend <strong>ohne Aufsicht</strong>: freihändige oder geheime Verträge, keine Folgenabschätzungen, ausländisches Eigentum und ausländische Finanzierung am operativen und am Überzeugungs-Ende, KI als die unsichtbarste Schicht — und niemand wurde gefragt.",
  "So klar wie die Befunde gesagt: <strong>was NICHT verbunden ist</strong>. Keine Verbindung Parscale–Palantir. Keine Silicon-Valley-Kabale — eine kursierende Liste von ~85 Namen ergab genau eine bereits bekannte Verbindung. Vorwürfe werden gekennzeichnet, nicht behauptet; die Mythen werden korrigiert. Diese Disziplin trägt das Ganze.",
  "Die vollständigen Berichte und ein herunterladbares PDF sind auf Englisch. Dies ist eine maschinell unterstützte Übersetzung; maßgeblich ist die englische Fassung."),
 "pt": ("O quadro completo: o que tudo isto significa",
  "Foram documentadas duas máquinas. Uma <strong>vigia e classifica</strong> populações — a ligação de registos do Estado, as plataformas operacionais da Palantir, a fusão de dados do ICE. A outra <strong>persuade-as</strong>: operações de influência financiadas por governos estrangeiros que já alcançam a própria IA. <strong>Não são uma única conspiração, e este trabalho não o afirma.</strong> O que as une é um padrão: os sistemas mais decisivos — os que vigiam, classificam e agora persuadem populações inteiras — funcionam cada vez mais <strong>com a supervisão desligada</strong>: contratos por ajuste direto ou secretos, sem avaliações de impacto, propriedade e financiamento estrangeiros na ponta operacional e de persuasão, a IA como a camada menos visível — e ninguém foi consultado.",
  "Dito com a mesma clareza que as conclusões: <strong>o que NÃO está ligado</strong>. Não há ligação Parscale–Palantir. Não há cabala de Silicon Valley — uma lista divulgada de ~85 nomes deu apenas uma ligação já conhecida. As alegações são rotuladas, não afirmadas; os mitos são corrigidos. É essa disciplina que sustenta tudo.",
  "Os relatórios completos e um PDF para download estão em inglês. Esta é uma tradução assistida por máquina; a versão em inglês é a oficial."),
 "it": ("Il quadro completo: a cosa porta tutto questo",
  "Sono state documentate due macchine. Una <strong>sorveglia e classifica</strong> le popolazioni — il collegamento dei registri statali, le piattaforme operative di Palantir, la fusione dei dati dell'ICE. L'altra le <strong>persuade</strong>: operazioni di influenza finanziate da governi stranieri che ora raggiungono la stessa IA. <strong>Non sono un'unica cospirazione, e questo lavoro non lo sostiene.</strong> Ciò che le lega è uno schema: i sistemi più decisivi — quelli che sorvegliano, classificano e ora persuadono intere popolazioni — funzionano sempre più <strong>senza controllo</strong>: contratti diretti o segreti, nessuna valutazione d'impatto, proprietà e finanziamenti stranieri all'estremità operativa e persuasiva, l'IA come strato meno visibile — e nessuno è stato interpellato.",
  "Detto con la stessa chiarezza dei risultati: <strong>ciò che NON è collegato</strong>. Nessun legame Parscale–Palantir. Nessuna cabala della Silicon Valley — un elenco diffuso di ~85 nomi ha prodotto un solo collegamento già noto. Le accuse sono etichettate, non affermate; i miti vengono corretti. È questa disciplina a reggere il tutto.",
  "I rapporti completi e un PDF scaricabile sono in inglese. Questa è una traduzione assistita da macchina; fa fede la versione inglese."),
 "nl": ("Het hele plaatje: waar het allemaal op neerkomt",
  "Twee machines zijn gedocumenteerd. De ene <strong>bewaakt en sorteert</strong> bevolkingen — de gegevenskoppeling van de overheid, Palantirs operationele platforms, de datafusie van ICE. De andere <strong>overtuigt</strong> hen: door buitenlandse overheden gefinancierde beïnvloedingsoperaties die nu tot de AI zelf reiken. <strong>Het is geen enkele samenzwering, en dit werk beweert dat niet.</strong> Wat ze verbindt is een patroon: de meest ingrijpende systemen — die hele bevolkingen bewaken, sorteren en nu overtuigen — draaien steeds vaker <strong>zonder toezicht</strong>: onderhandse of geheime contracten, geen effectbeoordelingen, buitenlands eigendom en financiering aan het operationele en overtuigende eind, AI als de minst zichtbare laag — en niemand werd iets gevraagd.",
  "Net zo duidelijk als de bevindingen: <strong>wat NIET verbonden is</strong>. Geen band Parscale–Palantir. Geen Silicon Valley-kliek — een rondgestuurde lijst van ~85 namen leverde precies één reeds bekende connectie op. Beschuldigingen worden gelabeld, niet beweerd; de mythes worden gecorrigeerd. Die discipline houdt het geheel overeind.",
  "De volledige rapporten en een downloadbare pdf zijn in het Engels. Dit is een machinaal ondersteunde vertaling; de Engelse versie is gezaghebbend."),
 "pl": ("Pełny obraz: co z tego wszystkiego wynika",
  "Udokumentowano dwie maszyny. Jedna <strong>inwigiluje i segreguje</strong> ludność — państwowe łączenie rejestrów, operacyjne platformy Palantira, fuzję danych ICE. Druga ją <strong>przekonuje</strong>: finansowane przez obce rządy operacje wpływu, sięgające już samej SI. <strong>To nie jest jeden spisek i ta praca tego nie twierdzi.</strong> Łączy je wzorzec: najważniejsze systemy — te, które inwigilują, segregują i teraz przekonują całe społeczeństwa — coraz częściej działają <strong>z wyłączonym nadzorem</strong>: kontrakty z wolnej ręki lub tajne, brak ocen skutków, zagraniczna własność i finansowanie na końcu operacyjnym i perswazyjnym, SI jako najmniej widoczna warstwa — a nikogo nie zapytano.",
  "Powiedziane tak jasno jak ustalenia: <strong>co NIE jest powiązane</strong>. Brak powiązania Parscale–Palantir. Brak kliki z Doliny Krzemowej — krążąca lista ~85 nazwisk dała dokładnie jedno, już znane powiązanie. Zarzuty są oznaczane, nie stawiane; mity są prostowane. Ta dyscyplina utrzymuje całość.",
  "Pełne raporty i PDF do pobrania są po angielsku. To tłumaczenie wspomagane maszynowo; wersja angielska jest wiążąca."),
 "ru": ("Полная картина: к чему всё сводится",
  "Здесь задокументированы две машины. Одна <strong>следит и сортирует</strong> население — государственное связывание записей, операционные платформы Palantir, объединение данных ICE. Другая его <strong>убеждает</strong>: финансируемые иностранными правительствами операции влияния, теперь дотягивающиеся и до самого ИИ. <strong>Это не единый заговор, и эта работа этого не утверждает.</strong> Их связывает закономерность: самые значимые системы — те, что следят, сортируют и теперь убеждают целые народы, — всё чаще работают <strong>с отключённым надзором</strong>: контракты без конкурса или секретные, без оценок воздействия, иностранная собственность и финансирование на операционном и убеждающем конце, ИИ как наименее заметный слой — и никого не спросили.",
  "Сказано так же прямо, как и выводы: <strong>что НЕ связано</strong>. Нет связи Parscale–Palantir. Нет клики из Кремниевой долины — распространявшийся список из ~85 имён дал лишь одну уже известную связь. Обвинения помечаются, а не утверждаются; мифы опровергаются. Именно эта дисциплина всё удерживает.",
  "Полные отчёты и PDF для скачивания — на английском. Это перевод с помощью машины; авторитетной является английская версия."),
 "he": ("התמונה המלאה: למה כל זה מצטבר",
  "תועדו כאן שתי מכונות. האחת <strong>מנטרת וממיינת</strong> אוכלוסיות — קישור רשומות ממשלתי, הפלטפורמות התפעוליות של פלנטיר, מיזוג הנתונים של ICE. השנייה <strong>משכנעת</strong> אותן: מבצעי השפעה הממומנים בידי ממשלות זרות, המגיעים כעת אל הבינה המלאכותית עצמה. <strong>אין מדובר בקנוניה אחת, והעבודה הזו אינה טוענת זאת.</strong> מה שמקשר ביניהן הוא דפוס: המערכות המשמעותיות ביותר — אלו המנטרות, ממיינות וכעת משכנעות אוכלוסיות שלמות — פועלות יותר ויותר <strong>ללא פיקוח</strong>: חוזים סגורים או חשאיים, ללא הערכות השפעה, בעלות ומימון זרים בקצה התפעולי והמשכנע, בינה מלאכותית כשכבה הסמויה ביותר — ואיש לא נשאל.",
  "נאמר באותה בהירות כמו הממצאים: <strong>מה שאינו מקושר</strong>. אין קשר פרסקייל–פלנטיר. אין קליקה של עמק הסיליקון — רשימה שהופצה ובה כ-85 שמות הניבה קשר ידוע אחד בלבד. ההאשמות מסומנות, לא נטענות; המיתוסים מתוקנים. המשמעת הזו היא שמחזיקה את הכול.",
  "הדוחות המלאים וקובץ PDF להורדה הם באנגלית. זהו תרגום מכונה; הגרסה האנגלית היא המחייבת."),
 "ar": ("الصورة الكاملة: إلامَ يؤول كل هذا",
  "وُثِّقت هنا آلتان. الأولى <strong>تراقب وتُصنِّف</strong> السكان — الربط الحكومي للسجلات، ومنصّات بالانتير التشغيلية، ودمج بيانات ICE. والأخرى <strong>تُقنِعهم</strong>: عمليات تأثير تموّلها حكومات أجنبية وصارت تطال الذكاء الاصطناعي نفسه. <strong>ليست مؤامرة واحدة، وهذا العمل لا يدّعي ذلك.</strong> ما يربط بينهما نمطٌ: أكثر الأنظمة أثرًا — تلك التي تراقب وتُصنِّف والآن تُقنِع شعوبًا بأكملها — تعمل على نحوٍ متزايد <strong>بلا رقابة</strong>: عقود بالأمر المباشر أو سرّية، بلا تقييمات أثر، ملكية وتمويل أجنبيان عند الطرف التشغيلي وطرف الإقناع، والذكاء الاصطناعي بوصفه الطبقة الأقل وضوحًا — ولم يُسأل أحد.",
  "يُقال بالوضوح نفسه الذي تُقال به النتائج: <strong>ما هو غير مرتبط</strong>. لا صلة بين بارسكال وبالانتير. لا عصبة من وادي السيليكون — قائمة متداولة تضم نحو 85 اسمًا أعطت صلة واحدة معروفة سلفًا. الاتهامات تُوسَم ولا تُؤكَّد؛ والخرافات تُصحَّح. هذا الانضباط هو ما يصمد به العمل كله.",
  "التقارير الكاملة وملف PDF للتنزيل باللغة الإنجليزية. هذه ترجمة آلية؛ والنسخة الإنجليزية هي المرجع."),
 "ja": ("全体像 — すべては何に行き着くのか",
  "ここでは二つの「機械」が記録された。一方は人々を<strong>監視し、選別する</strong>——政府の記録連結、パランティアの運用プラットフォーム、ICE のデータ統合。もう一方は人々を<strong>説得する</strong>——外国政府が資金提供する影響工作で、いまや AI 自体にまで及んでいる。<strong>これは単一の陰謀ではなく、本作はそう主張しない。</strong>両者を結ぶのはパターンだ。最も重大なシステム——人々を監視し、選別し、いまや説得するもの——はますます<strong>監督が切られた状態</strong>で動いている。随意契約や秘密契約、影響評価の不在、運用と説得の末端における外国の所有と資金、最も見えにくい層としての AI——そして誰も問われなかった。",
  "調査結果と同じくはっきりと述べる——<strong>つながっていないもの</strong>。パースケールとパランティアの結びつきはない。シリコンバレーの結社もない——出回った約85名の名簿からは、既知のつながりが一つ出ただけだ。主張は「主張」として明示し、断定しない。神話は訂正する。この規律こそが全体を支えている。",
  "完全な報告書とダウンロード可能な PDF は英語です。これは機械支援による翻訳であり、英語版が正本です。"),
 "ko": ("전체 그림 — 이 모든 것이 가리키는 것",
  "여기에는 두 개의 '기계'가 기록되었다. 하나는 사람들을 <strong>감시하고 분류</strong>한다 — 정부의 기록 연계, 팔란티어의 운영 플랫폼, ICE의 데이터 융합. 다른 하나는 사람들을 <strong>설득</strong>한다 — 외국 정부가 자금을 댄 영향력 공작으로, 이제 AI 자체에까지 닿고 있다. <strong>이는 하나의 음모가 아니며, 이 작업은 그렇게 주장하지 않는다.</strong> 둘을 잇는 것은 하나의 패턴이다. 가장 중대한 시스템 — 사람들을 감시하고 분류하며 이제 설득하는 시스템 — 은 점점 더 <strong>감독이 꺼진 채</strong> 작동한다. 수의계약이나 비밀계약, 영향평가의 부재, 운영과 설득의 말단에 있는 외국 소유·자금, 가장 보이지 않는 층으로서의 AI — 그리고 아무도 의견을 묻지 않았다.",
  "조사 결과만큼 분명하게 말한다 — <strong>연결되지 않은 것</strong>. 파스케일–팔란티어 연결 없음. 실리콘밸리 결사도 없음 — 떠돌던 약 85명 명단에서는 이미 알려진 연결 하나만 나왔다. 의혹은 의혹으로 표시하고 단정하지 않으며, 신화는 바로잡는다. 이 규율이 전체를 지탱한다.",
  "전체 보고서와 내려받을 수 있는 PDF는 영어로 제공됩니다. 이것은 기계 보조 번역이며, 영어판이 정본입니다."),
 "zh": ("全貌——这一切的指向",
  "这里记录了两台「机器」。一台<strong>监控并分类</strong>人群——政府的记录关联、Palantir 的运营平台、ICE 的数据融合。另一台<strong>说服</strong>人群——由外国政府出资的影响行动，如今已伸向人工智能本身。<strong>这并非单一阴谋，本作也不作此主张。</strong>将二者联系起来的是一种模式：最具影响力的系统——那些监控、分类、如今还说服整批人口的系统——越来越在<strong>监督被关闭</strong>的状态下运行：单一来源或保密合同、没有影响评估、运营端与说服端的外国所有权与资金、作为最不可见一层的人工智能——而无人被征询。",
  "以与结论同样的坦率说明：<strong>哪些并无关联</strong>。不存在 Parscale–Palantir 的关联。不存在硅谷小集团——一份流传的约85人名单只得出一个早已知晓的关联。指控被标注为指控，而非断言；谬误被纠正。正是这种克制使整体站得住脚。",
  "完整报告与可下载的 PDF 为英文。本文为机器辅助翻译；以英文版为准。"),
}

REPO_INDEX = "/writing/investigations"
PDF = "/static/the-whole-picture.pdf"

def build_content(intro, notconn, linksnote):
    return [
        "<em style='color:var(--text2)'>" + intro + "</em>",
        GFX,
        "<em style='color:var(--text2)'>" + notconn + "</em>",
        "<span style='display:block;border-left:3px solid var(--border);padding-left:14px;color:var(--text3);font-size:.92rem'>" + linksnote + " &nbsp;&middot;&nbsp; <a href='" + REPO_INDEX + "' style='color:var(--accent)'>brandonmyers.net/writing/investigations</a> &nbsp;&middot;&nbsp; <a href='" + PDF + "' style='color:var(--accent)'>PDF</a></span>",
    ]

D="/opt/treechain/brandonmyers"  # not used here; merge happens after scp-down
src=pathlib.Path("/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/essay_translations.json")
tr=json.loads(src.read_text())
added=[]
for lang,(title,intro,notconn,linksnote) in T.items():
    tr.setdefault(lang, {})
    tr[lang]["the-whole-picture"] = {"title": title, "label":"Investigation · Capstone", "date":"June 2026", "content": build_content(intro,notconn,linksnote)}
    added.append(lang)
src.write_text(json.dumps(tr, ensure_ascii=False, indent=1))
print("added the-whole-picture translations for:", added)
print("total langs in file:", len(tr), "| file bytes:", src.stat().st_size)
