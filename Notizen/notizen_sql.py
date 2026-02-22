# Sql alleine ist nur eine Sprache und verwaltet noch keine Datenbanken, sie alleine ist nur wie eine anleitung und kann ohne ein DBMS nichts tun
# DBMS -> Database managment system -> versteht sql und arbeitet damit um datenbanken zu verwalten
# es gibt verschiedene DBMS darunter RDBMS -> Relations Datenbank managment systeme -> benutzen sql und speichern daten in tabellen und
# No sql DBMS -> sie speichern daten nicht in tabellen sondern in Graphen, dokumenten oder key value paaren
# Manche Dinge lassen sich als Tabellen schwer abbilden z.B. wer kennt wenn von wo kommt man wohin usw darum nimmt man graphen
# Da man in der Prayxis oft beides braucht hat man oft haupt daten in relation und beziehungne in nosql

# man verbindet sich zu einer DBMS und übergibt anweisungen in sql, das DBMS führt anweisungen aus und sendet ergebnisse zurück
# Eine relationale Datenbank besteht aus tabellen die miteinander über keys verbunden werden können
# Da Festplatte oft langsam zum speichern ist und RAM schnell, lädt das RDBMS häufig genutzte daten in den RAM Cache damit sie schnell zum abfragen sind
# Wichtige SQL COMMANDS
    # SELECT - extracts data from a database
    # UPDATE - updates data in a database
    # DELETE - deletes data from a database
    # INSERT INTO - inserts new data into a database
    # CREATE DATABASE - creates a new database
    # ALTER DATABASE - modifies a database
    # CREATE TABLE - creates a new table
    # ALTER TABLE - modifies a table
    # DROP TABLE - deletes a table
    # CREATE INDEX - creates an index (search key)
    # DROP INDEX - deletes an index

# Sqlite läuft direkt am PC, man braucht nur eine .DB datei und programme schreiben dann direkt auf die datei

# Datenbank kennt nur Indexe wenn man sie mit Primary Key angibt, ab CREATE INDEX idx_user_ma,e ON user(name); wei die DB es gibt einen index für den User
# Bei SELECT * FROM users WHERE name = "xy" -> überlegt DB ungefähr zuerst Filter ist auf Name, gibt es Index auf Name -> Ja, DB schaut im Index nach xy,
# findet dort xy -> Zeile 4 und springt direkt zur richtigen zeile ohne durchgehen der ganzeb tabelle
# Intern speichert DB sowas
# Tabelle: users
# Spalte: name
# Index: idx_users_name
# Typ: B-Tree
# Die DB muss Index aber nicht nutzen, wenn DB denkt Index bringt nichts
# Die DB verwendet keine Hashmaps da Hashmaps nicht sortiert sind und keine Reihenfolge haben,
# DB verwendet B - Tree und speichert Namen alphabetisch das sie mit Binary Search suchen kann
# DB verwendet nicht Heap da heap nur versichern kann eltern < Kinder und darum bereichsabfragen nicht gehen würden

# B - Baum -> https://de.wikipedia.org/wiki/B-Baum
# Optimiert für Datenbanken und Festplatten
# wird in fast jeder DB verwendet und zählt zu einer der Häufigsten Datenstrukturen, löschen einfügen, sortieren ist in logarithmischer zeit möglich
# Ein B - Baum muss nicht Binär sein, er eugbet sich ideal als Datenstruktur zur verwaltung von indizes relationaler Datenbankmodelle
# B Bäume wachsen von unten nach oben, in Knoten von B - Bäumen ist eine Variable Anzahl an Schlüssel gespceichert
# Innere Knoten zeigen nur den Weg, alle Blätter enthalten Daten und liegen auf der selben ebene
# Diskriptor ist innerer Knoten und dient als wegweiser, zb wenn man einen wert einfügen will sagt diskribtor links sind alle werte kleiner x und rechts größer x
# Jeder Baum hat eine Root, die Root startpunkt für jede Suche, Einfüge- oder Löschoperation
# m = Anzahl der Werte, die ein Blatt / Knoten im B-Baum maximal halten kann
	# •	Suche in Blatt: O(log m)
	# •	Einfügen + evtl. Split: O(m) lokal → sehr klein, weil m ≪ n
	# •	Höhe des Baums: O(log n)
# Die Blätter Seiten sind oft Arrays, Innere Knoten (also Root + alle Knoten, die nicht Blätter sind)
# die keys + values sind kein dict sondern z.B. eine Liste von Tuples mit (k, v)
# B - Baum teilt die Daten in kleine Blätter, bei einer operation muss man sich immer nur auf ein blatt fokussieren nicht auf mehrere

# SQL
# Kommunikation zwischen Client und Server funktioniert über TCP/IP Unix sockets
# Bei lokalen verbindungen läuft MYSQL auf Computer und man braucht kein WLAN um sich zu verbinden (localhost port 3306), wenn MYSQL auf einem server läuft
# SQL erlaubt nicht mehrere Datenbanken in einem befehl zu löschen wie z.B. bei Tables, DROP DATABASE IF NOT EXISTS xy;
# Wenn man etwas Dropt das nicht existiert macht sql einen error,

# ____QUOTES____
# In sql verwendet man meistens singel quotes für text/strings alles was keine namen sind zb SELECT * FROM users WHERE name = 'xy' 
# -> name ist spaltenname darum ohne quotes und xy ist textwert
# Wenn man leerzeichen bei z.B. Tabellenname will, muss man es in quotes setzen

# __DB erstellen__
# CREATE DATABASE [IF NOT EXISTS] xy;
# Bevor man mit DB arbeitet muss man sie mit USE xy; auswählen
# man kann nicht mehrere DB auf einmal erstellen

# __automatisch angelegte unterObjekte__
# sind keine unterordner sondern automatisch angelegete objekte
	# •	Tables → Tabellen, in denen die Daten gespeichert werden
	# •	Views → Virtuelle Tabellen, die gespeicherte Abfragen darstellen
	# •	Stored Procedures / Functions → Kleine Programme oder Funktionen, die du in der DB speichern kannst
	# •	Triggers → Aktionen, die automatisch bei Insert/Update/Delete auf Tabellen ausgelöst werden
	# •	Events → Zeitgesteuerte Aktionen (z. B. einmal täglich etwas aktualisieren)
	# •	Indexes → Indexe auf Tabellen für schnellere Abfragen
	# •	Foreign Keys / Constraints → Regeln, die Beziehungen zwischen Tabellen erzwingen
# In tables werden Daten gespeichert, Views sind virtuelle Tables die keine eigenen Daten speichern sondern die ergebnisse aus einer gespeicherten abfrage anzeigen
# wenn man auf eine View zugreift macht mysql die eigentlich gespeicherte anfrage auf den echten tabellen, sie zeigt immer aktuellen stand der Tabelle
# stored procedures ist ein gespeichertes programm das eine reihe von befehlen ausführt, kann daten zurückgeben, muss aber nicht
# Funktionen machen z.B. eine FUnktion die dir alle User in einer Bestimmten stadt gibt, man kann logik machen und es hat ein return, aufruf wie eine Normale Fuktion in Sql z.B. SELECT
# SHOW CREATE PROCEDURE ps_setup_save; zeigt eine Procedure, \G formatiert, CREATE PROCEDURE... macht neue Procedure, während SHOW nur anzeigt

# __neue Tabelle__
# CREATE TABLE tabellenname (
#     spalte1 DATENTYP [OPTIONEN],
#     spalte2 DATENTYP [OPTIONEN],
#     ...
#     [PRIMARY KEY (spalte1)]
# );
# VARCHAR(50) -> steht für die maximale länge an textzeichen die gespeichert werden können
# Primary Key, sagt das keine der Zeilen zwei gleiche werte haben darf, wenn schon dann Fehler, AUTO_INCREMENT -> sql soll bei einer neuen Zeile die Zahl Automatisch hochzählen
# PRIMARY KEY (user_id, product_id) -> erlaubt zwei user bestellen das gleiche produkt, erlaubt aber nicht ein user bestellt zweimal das selbe produkt
# Kombinierter Primärschlüssel -> alle keys können gleich sein bis auf die gemeinsamen kombinationen
# user_id                 produkt_id              menge
#   1                       10                      2
# User kann produkt maximal 10 mal bestellen
# Spalte nachträglich einfügen
# man muss bei jeder Spalte den Datentypen bekanntgeben
# Werte nur mit AUTOINCREMENT ohne Primary Key erlauben doppelte Werte
# Primary Key identifiziert dei Zeile eindeutig also darf es nur einen geben
# AUTO_INCREMENT funktioniert nur auf der ersten Spalte des PRIMARY KEY -> die hochzuzählende Spalte muss die erste in der PK kombination sein
# Primary Key kann in der spaltendefinition direkt stehen, oder am ende der Spaltendefinition mit PRIMARY KEY (spaltenname)
# Primary Keys dürfen nie Null sein auch composite primary keys nicht

# __ALTER__
# ALTER TABLE tabellenname ADD spaltenname DatenTYP [OPTIONEN], ALTER bedeuted verändern -> kein If exists nötig

# __INSERT__
# INSERT INTO tablename (spaltenname1, spaltenname2...) VALUES (wert1, wert2...), (wert1, wert2...);

# __SELECT__
# SELECT (spaltenname1, spaltenname2...) FROM xy WHERE spaltenname = nummer, wenn spaltenname index ist braucht es nur logaritmische zeit
# ORDER BY first_name -> sortiert ausgaben alphabetisch, ORDERED BY braucht immer sortieralgoritmus auser die Daten sind schon passend aus enen Index, MYSQL baut für jede indexierte spalte eigene DAtenstrukur
# MYSL weis anhand der vorhandenen datentyp welche sortierungsmethode man braucht
# man muss immer angeben von welcher Tabelle man select will, SELECT 1, 2; Fragt konstante werte ab, gibt Tabelle mit werten von den Konstanten zurück ohne das sie gespeichert sind
# man knn auch berechnunge mit SELECT 4/2; durchführen
# Es gibt bei Befehle optionale werte, die reihenfolge der werte maht unterschied
# überfüllte SELECT statements kann den server, netzwerk unter druck setzen
# Bei SELECT (spaltenname3, spaltenname2...)... wird es in der abgefragten reihenfolge zurückgegeben
# SELECT user_id, product_id + 12 FROM users; -> macht bei jeder Product Id + 12, SELECT user_id, product_id, product_id + 12 FROM users; -> zeigt einmal ohne + 12 und einmal mit
# man kann klammern in ausdrücken wie (product_id * 12) + 32 einfügen
# Bei SELECT [DISTINCT] ... nimmt man nur werte ohne duplikate, wenn mehr als wie eine spalte dann angegeben ist nimmt es die kombination aus den zwei spalten -> es darf zb nicht eine spalte mit gleichen produkt und gleichem user_id zweimal geben
# mann kan auch SELECT *, 10 AS price machen
# __WHERE__
# SELECT ... FROM xy WHERE spaltenname = nummer; -> WHERE points > 3000 gibt nur die werte mit punkten über 3000 zurück, SQL engine geht über jeeden wert in dem Table und bei jedem wert wo die bedinung stimmt gibt es ihn zurück
# Equal Signs in mysql -> <, <=, >, >=, != / <>, =
# Wenn den wert denn man herausfiltern will ein String ist muss man douple oder ingle quotes verwenden, wenn man schreibt WHERE state = "VA", gilt das für va und für VA und für Va / vA
# Dates werden auch mit quotes geschrieben auch wenn sie keine strings sind, in sql werden daten "yyyy-mm-dd" angegeben
# In SQL kann man nicht eindeutig eine Zeile identifizieren ohne einen Index, da es keine garantie gibt welche zeile die erste oder dritte ist da es eine baum struktur ist

# __IN__
# wenn man zb alle customer in state x, y und z haben will könte man SELECT ... WHERE state = x OR state = y OR state = z; mit in kann man
# prefered_shop IN ("UK", "DC", "Sidney") schreiben
# man muss querys immer bei state = x OR y OR z immer ganz ausschreiben weil state = x bool zurückgibt und man keinen bool mit einem string vergleichen kann

# __Between__
# um alle werte zu bekommen die zwischen werten sind zb alle werte die zwischen id = 34 und id = 74 sind, mit index dauert es nur O(log n + k) k -> abgefragte werte, ohne dauert es O(n) full table scan
# statt WHERE price <= 23 AND price > 84 kann man price BETWEEN 23 AND 84, funktioniert auch bei nicht ints

# __AND, OR, NOT__
# WHERE
# 	customer_id >= 3
#     AND
# 	payback_points <> 3
# AND verbindet verschiedene Statements
# NOT operator kann statements umdrehen zb bei WHERE NOT wird der untige Block umgedreht, Bei WHERE NOT (birthdate > "1990-02-12" OR points > 1000), dreht NOT die expression auf
# (birthdate <= "1990-02-12" AND points <= 1000) um
# logical Operatoren haben auch order so wie operatoren (+ - / *)

# __LIKE__
# mit dem LIKE operator kann man werte bekommen die eine bestimmte string pathern folgen,
# wenn man zb alle namen die mit x starten haben will, mit WHERE name LIKE "a%" -> bekommt man jeden wert der mit a / A anfängt egal was danach ist
# %xyz -> hohlt nur werte die damit enden, %x% -> alle werte die x enthalten, %x%y -> alle werte die x enthalten und danach mit y aufhören
# bei "_y" -> werte bei denen der zweitletze buchstabe y ist egal was davor kommt solange es die richtige anzahl hat, "_m%" alle werte wo der zweite buchstabe ein m ist, "b__y" -> werte die mit b starten mit y enden und 4 wörter lang sind
# Like operator ist älter, neuerer ist REGEXP

# __REGEXP__
# REGEXP -> Regular Expression
# wenn man nach einen customer sucht der den wert x in seinem namen hat dann WHERE name REGEXP "x"
# REGEXP benutzt andere operatioren, wenn man alle werte dei mit a anfangen dann "^a", ^ -> anfang eines strings, $ für ende eines strings
# um nach x, y, z zu suchen kann man "x|y|z" -> | or, "^x|y$" -> string startet mit x oder endet mit y,
# wenn man sichergehen möchte das vor buchstaben x ein a oder b vorkommt macht man "[ab]x$" -> das gilt dann für alle werte dei mit ax oder bx enden, "[xy]" alle werte die x oder y enthalten
# "[xy]d" -> alle werte die vor einem d ein x oder y haben, "d[xy]" -> alle werte die nach einem d ein x oder y enthalten, wenn man vor einem e alle werte von b-d haben will dann "[b-d]e"

# __NULL__
# Um nach werten zu sehen die keinen wert haben verwendet man NULL
# man überprüft mit IS NULL, In sql gibt es 3 logische ergebnisse -> TRUE, FALSE, UNKNOWN, UNKNOWN kommt immer wenn NULL wo ist z.B. bei WHERE id = NULL, fragt ist 5 gleich unbekannt -> antwort -> man weis es nicht
# NULL = NULL gibt auch UNKNOWN zurück, in sql bedeuted Null nicht kein wert sondern -> wert existiert aber ist nicht bekannt, NULL bedeuted nicht es gibt keinen wert / leer
# Wenn zb bei geburtstag NULL ist bedeuted das wert noch nicht bekannt nicht es gibt keinen wert
# in python ist None ein Objekt und bedeuted leer, darum None = None -> TRUE
# Um in SQL werte mit NULL zu suchen -> WHERE name IS NULL;

# In SQL representiert 0 -> False und 1 -> True, bei WHERE 1; -> gibt 1 True zurück, man kann SELECT * FROM users WHERE 4=4;

# __ORDER BY__
# Ohne ORDER BY gibt es keine garantierte Reihenfolge nach der ausgegeben wird, man sagt sql einfach man will alle zeilen,
# es ist ohne ordered by oft nach primary key sortiert, weil pyhsich oft nach primary key gespeichert ist, is aber keine garantie
# primary key ist immer der wert der die zeilen identifiziert, da bei ihm schnelle sortierung möglich ist und schnelle suche
# bei WHERE user_id = 231; dauert ohne primary key suche solange bis 231, mit pk springt es direkt logaritmisch zum eintrag
# Syntax ist SELECT * FROM xy WHERE x = y ORDER BY spaltenname [DESC]; -> absteigend / descending,
# um zb customers nach einem bestimmten ort zu sortieren und dann in dem sortierten ort nach dem namen -> SELECT * FROM users ORDRED BY state, firstname DESC
# man kann auch SELECT id, 24 AS "24" FROM customers ORDERED BY "24"
# man kann auch in ORDERED BY product_price * quantity; machen
# mit ASC macht man aufsteigend -> standart ist aufsteigen
# __LIMIT__
# wenn man nur die ersten 3 einträge will, kann man SELECT * FROM customers WHERE x = y ORDERED BY x LIMIT 3; -> wenn limit über die werte ist bekommt man alle werte
# LIMIT limiteirt oft erst danach die ausgabe, aber wenn die spalte indexiert ist wird oft nur die ersten n werte herausgegeben
# bei LIMIT gibt es auch OFFSETS wenn man zb die ersten 6 werte überspringen will, da man werte einer db anzeigt und man mehrere pages macht zb page1: 1 - 3, page2: 3 - 6, page3: 6 -9
# kann man ein offset 6 für page 3 mit LIMIT 6, 3 machen

# __INNER JOINS__
# man kann statt werte von nur einer tabelle auch werte von mehreren tabellen gleichzeitig hohlen,
# wenn man customer_id seperat und die informationen zum customer seperat in einer tabelle speichert und zb in der tabelle orders, wo die bestellungen sind und daneben die client id steht
# für jede order statt der customer id den namen des customers haben will, kann man JOIN benutzen
# es gibt INNER JOIN und OUTER JOIN -> INNER keyword ist optional
# um orders mit customers zu joinen kann man SELECT * FROM orders JOIN customers ON orders.customer_id = customers.customer_id;
# SELECT o.customer_id, order_id, product_name, c.first_name
# FROM orders AS o
# JOIN customers AS c
# 	ON o.customer_id = c.customer_id
# WHERE o.customer_id > 2
# ORDER BY c.customer_id DESC, order_id
# LIMIT 400;
# Query sagt man soll die werte aus den jeweiligen tabellen nehmen auf die order id die gleiche wie die customer id ist
# man muss in SELECT angeben aus welcher tabelle man den wert will, wenn es einen wert in beiden tabellen gibt wie zb bei customer_id
# man muss bei zb customer_id nicht immer den ganzen tabellennamen hinschreiben man kann auch einen alieas mit FROM table1 AS t1 / JOIN table2 AS t2 machen oder auch AS weglassen
# wenn man alias benuzt muss man ihn auch verwenden

# __JOIN bei verschiedenen DB__
# um werte aus verschiedenen DBs zu kombinieren muss man vor der DB auf der man sich nicht gerade befindet dann foreign_db.products machen um aus verschiedenen DB werte zu kombinieren
# um sicherzugehen kann man auch auf der db auf der man sich derzeitig befindet ein db1.orders machen, damit man wenn man nicht vorher kein USE gemacht hat einen Error hat

# __SELF JOINS__
# In sql kann man auch db mit sich selbst joinen, wenn man zb tabelle mit allen personen in der firma hat mit id und ihr manager mit id und der manager ist auch teil der firma kann man mit sich selbst joinen
# SELECT e.employee_id AS id, e.first_name AS Name, m.first_name AS Manager
# FROM employees AS e
# JOIN employees AS m
# 	On e.manager_id = m.employee_id
# ;
# man joint die tabelle mit sich selbst und macht zu jedem wert den wert in der tabelle vom manager
# Bei ON e.manager_id = m.employee_id OR e.manager_id IS NULL schaut mysql auf die zeile vom ceo und bedinung manager id = Null ist erfüllt aber mysql muss trotzdem zeile finden die on erfüllt
# in mysql nimmt inner join nur die werte wenn es tatsächlich etwas in m findet

# __Join mit mehreren Tabellen__
# Wenn man zb in einer orders tabelle einen abschnitt für bestellstatus hat und eine tabelle die den einzelnen statusen einen namen gibt
# und eine customer id mit einer tabelle für den jeweiligen customer die informationen, dann muss man um den bestellstatusnamen und kundennamen zu bekommen,
# einen join mit 3 tabellen machen
# wenn bei einem join der angegebene wert nicht existeirt wird alles ignoriert, bei mehreren inner joins gilt, wenn mehr als ein statement keinen passenden wert hat wird dei ganze zeile ingoriert
# SELECT order_id, order_date, last_name, first_name, state_name
# FROM orders o
# JOIN customers c
# 	ON o.customer_id = c.customer_id
# JOIN status s
# 	ON o.status = s.identifier
# ;
# man kann einfach mehrere joins kombinieren

# __COMPUND JOIN Contionen__
# man hat in sql nicht immer einen primary key der die zeile identifiziert, wenn man zb in order_items order_id product_id quantity und unit_price hat gibt es keinen klaren identifier für die zeile
# in order_id, product_id, quantity und unit_price können doppelte werte vorkommen, desshalb kann man die kombination von verschiedenen werten nutzen, man braucht einen composite primary key
# mit PRIMARY KEY (spalte1, spalte2...) macht man einen composite primary key
# um einen composite primary key zu sortieren kann man ORDER BY spalte1 ASC, spalte2 ASC; -> je nachdem in welcher reihenfolge man in den primary key übergeben hat
# um zu Selecten -> WHERE spalte1 = ersten teil vom primary key AND spalte2 = zweiter teil vom primary key
# um ein JOIN mit gemeinsamen primary keys zu machen -> bei nur ON orders.order_id = order_notes.order_id kann es sein das order_id zweimal vorkommt, desshalb benutzt man
# ON orders.order_id = order_notes.order_id AND ON orders.product_id = order_notes.product_id

# __IMPLICIT JOIN SYNTAX__
# SELECT *
# FROM orders o
# JOIN customers c
# 	IN o.customer_id = c.customer_id
# kann man auch
# SELECT *
# FROM orders o, customers c
# WHERE o.customer_id = c.customer_id
# Wenn man bei implicit join syntax where vergisst wird alles mit allem gejoined n^2

# __Outer JOINS__
# JOIN -> INNER JOIN
# SELECT o.customer_id, order_id, product_name, c.first_name
# FROM initial_db.orders AS o
# JOIN initial_db.customers AS c
# 	ON o.customer_id = c.customer_id
# ORDER BY customer_id
# ;
# Man sieht nur die kunden die eine bestellung gemacht haben mit inner join, bei ON o.customer_id = c.customer_id returnt man nur werte die diese bedinung erfüllen
# in sql gibt es 2 subtypen für outer joins -> left joins und right joins, bei left join werden alle werte vom linken table (orders) returnt egal ob ON True oder False ist
# Bei right join werden alle werte von der rechten tabelle zurückgegeben egal ob ON True oder False ist
# man kann auch LEFT OUTER JOIN schreiben statt LEFT JOIN
# Der unterschied von Left und Right Join liegt darin welche Tabelle vollständig zurückgegeben wird
# SELECT *
# FROM A
# LEFT JOIN B ON A.id = B.id;
# 	•	alle Zeilen aus A werden angezeigt
# 	•	passende Zeilen aus B werden ergänzt
# 	•	wenn kein Match → Werte aus B = NULL
# -- statt RIGHT JOIN
# FROM A RIGHT JOIN B ON ...

# -- einfach Tabellen tauschen
# FROM B LEFT JOIN A ON ...

# SELECT * FROM products p LEFT JOIN orders o ON p.id = o.order_id; -> wenn es zwei passende orders zu einem produkt gibt erscheint produkt 2 mal

# __Alle JOIN kategorien
# __CROSS JOIN__
# bei cross join wird jede spalte der einen tabelle mit jeder spalte der anderen tabelle angezeigt
# man kann cross join mit CROSS JOIN t2; machen oder nur mit FROM t1, t2 -> sql interpretiert beitstriche bei FROM als kartesisches produkt
# bei cross join wird alles mit allem multipliziert darum gibt es kein on
# wenn man alles mit allem kombinieren möchte dann cross join

# __INNER JOIN__
# bei inner join werden nur die zeilen ausgegeben, bei denen die werwte aus bestimmten spalten der tabellen übereinstimmen
# wenn die zu überprüfenden spalten einen wert nicht gemeinsam haben, dann wird die zeile ignoriert
# es wird für alle zeilen überprüft ob die beiden spalten der zeile den gleichen wert haben
# man kann auch
# Select *
# From Tabelle1, Tabelle 2
# Where Tabelle1.Spalte = Tabelle2.Spalte;
# schreiben
# __NATURAL JOIN__
# vergleicht automatisch spalten die den gleichen namen haben und in ausgabe wird zweite spalte gelöscht da sie die gleichen werte hat 
# SELECT *
# FROM Tabelle1 NATURAL JOIN Tabelle2, wenn nur zwei spalten gleichen namen haben liefert gleiche ergebniss wie ein inner join aber die spalten werden noch zusammengefasst
# SELECT * FROM A NATURAL JOIN B; sql macht intern ON a.id = B.id AND A.typ = B.typ, es selected nur das wo alle werte in der spalte mit gleichem wert zusammenpassen
# wenn keine spalten übereinanderstimmen macht sql einen cross join, weil es dann keine Join werte also kombiniert es jede zeile aus A mit jeder Zeile aus B
# Bei inner join wird nichts automatisch zu einen kartesischen produkt, inner join bedeuted verbinde zeilen die diese bedinung erfüllen
# bei mehreren JOINS hohlt jedes join eine tabelle dazu, bei AND nicht
# Sql führt joins von links nach rechts aus, es filtert zeilen sofort bevor der nächste join auf die gefilterte zeile macht
# SELECT order_date, order_id, first_name, shipper, status FROM orders o INNER JOIN customers c ON o.customer_id = c.customer_id LEFT JOIN shippings s ON s.shipper_id = o.shipper_id INNER JOIN status st ON o.status_identifier = st.status_identifier;
# man nimmt alle werte einer zeile die als LEFT markiert wurden egal ob sie mit etwas von der anderen tabelle übereinstimmen oder nicht, wenn bei der anderen tabelle etwas nicht übereinstimmt zb man hat customer id die nie in der LEFT tabelle vorkommt wird es nicht angezeigt
# __SELF OUTER JOINS__
# um einen outer join auf einen self join zu machen um alle werte anzuzeigen egal ob sie übereinstimmen oder nicht, macht man einfach normalen self join mit LEFT

# __USING__
# man kann ON o.customer_id = c.customer_id mit USING (customer_id)
# SELECT c.customer_id, order_id, product_name, c.first_name
# FROM initial_db.orders AS o
# INNER JOIN initial_db.customers AS c
# 	-- ON o.customer_id = c.customer_id
# 	USING (customer_id)
# LEFT OUTER JOIN bonus_programm b
# 	-- ON o.customer_id = b.customer_id
# 	USING (customer_id)
# ORDER BY customer_id
# ;
# bei kombinierten primary key kann man auch statt ON a.id = b.id AND a.name = b.name -> USING (id, name) schreiben

# __UNIONS__
# wenn man zb eine tabelle hat mit werten vom derzeitigen jahr und werte vom vorherigen jahr, kann man allen jahren die davor sind ein label geben und allen danach ein label
# man will die bestellungen in ei9nem jahr markieren und die bestellungen im vorherigen, wenn man einfach WHERE order_date >= "2026-01-01" schreibt, dann wird im nächsten jahr die abfrage nicht mehr gültig sein
# SELECT order_id, order_date, "active" as status
# FROM initial_db.orders
# WHERE order_date >= "2026-02-09"
# UNION
# SELECT order_id, order_date, "archived" as status
# FROM initial_db.orders
# WHERE order_date < "2026-02-09 "
# ;
# man kann die zeilen so in einer ausgabe kombinieren, beide zeilen müssen gleiches select länge haben sonst error, man kann es auch auf daten von verschiedenen tabellen anwenden
# wenn man zb SELECT name, order_id... macht und dann SELECT customer_name, date... macht dann wird immer der wert der zuletzt steht der spaltenname
# man kann bei union auch joins, sorts, where, limits usw machen diese gelten dann auf die beiden spalten gemeinsam

# __COLUMN ATTRIBUTES__
# Der unterschied von VARCHAR(50) und CHAR(50) ist das varchar für variable charactere steht und wenn ein string zb nicht 50 zeichen lang ist es nur 50 zeichen speichert,
# char fügt wenn es nicht 50 zeichen sind die restlichen zeichen als spaces hinzu
# PK identifiziert endeutig den customer, es darf kein wert zwei mal vorkommen und dar nicht null sein
# NN steht für not null und sagt das bei einer spalte der wert bekannt sein muss
# AI -> AUTO_INCREMENT -> bei jedem neuen wert macht mysql bei jeder neuer zeile die eingefügt wird den wert um eins erhöhen
# man kann den wert auch selbst setzen solange er noch nicht vorhanden ist, mysql vergibt dann automatisch dem nächsten wert den eingefügten wert + 1
# Default / Expression definiert welcher wert eingefügt wird wenn kein wert angegeben ist

# __INSERT__
# um eine einzelne zeile einzufügen verwendet man INSERT INTO tabellenname VALUES (DEFAULT, "x", "y");
# wenn man in einer spalte einen default wert hat kann man in sql einfach DEFAULT als wert schreiben
# dates und string in sql immer mit quotes
# man kann auch optional bei SELECT * FROM tabellenname (spaltenname1, spaltenname2...)...
# um mehrere zeilen einzufügen nach VALUES (s1, s2, s3), (s1, s2, s3)...
# INSERT INTO orders2 (
# 	order_id,
#     product_id,
#     quantity,
#     unit_price
# )
# VALUES
# 	(DEFAULT, 112, 23, 12.23),
#     (DEFAULT, 112, 23, 12.23),
#     (DEFAULT, 112, 23, 12.23)
# ;
# Insert in mehrere tabellen
# wenn man zb eine orders tabelle hat mit order_id, customer_id, order_date, status hat sind die bestellten sachen nicht in der tabelle sondern die order id in order_items,
# wo sich die order_id, product_id, quantity und der preis befindet
# eine order kann 1 oder mehrere order_items haben, man spricht von einer aprent child beziehung, wo order das parent und alle order_tems die kinder sind
# um gleich mehrere zeilen in verschiedenen tabellen einfügen zu können, brauchen wir um bei autoincrement order_id den wert der order zu bekommen eine funktion
# Mysql hat mehrere funktionen eine davon ist LAST_INSERT_ID() -> die dir die letzte ID von einem insert zurückgibt
# funktionen in mysql kann man nur mit SELECT abrufen, LAST_INSERT_ID() gibt die letzte erzeugte autoincrement id zurück, dies geht nur für die aktuelle verbindung
# Um ein insert dann in mehreren tabellen zu machen wenn es autoincrement gibt macht man
# INSERT INTO orders3 (
# 	customer_id, -- 1 - 8
#     product_id, -- 1 - 74
#     order_date,
#     total
# )
# VALUES (
# 	(2, 12, "2026-02-03", 19.99)
# );
# INSERT INTO order_items (
# 	order_id,
#     product_id,
#     quantity
# )
# VALUES (
# 	(LAST_INSERT_ID(), 23, 2),
# 	(LAST_INSERT_ID(), 13, 4),
#     (LAST_INSERT_ID(), 43, 1)
# );

# __KOPIEREN VON TABELLEN__
# wenn man eine Tabelle in eine andere kopieren will, kann man das effizient machen und nicht alle werte einzeln kopieren mit CREATE TABLE orders_backup AS SELECT * FROM orders;
# mysql wird jedoch die attribute wie primary key nicht übernehmen und ignorieren
# Ein subquery ist ein SELECT statemnt das teil eines anderen statements ist, man kann auch ein subselect in einen insert statement machen
# TRUNCATE Table löscht alle inhalte einer Tabelle
# um Tabelleninhalte zu kopieren und dann einzufügen, kann man
# INSERT INTO orders_backup
# SELECT * FROM orders3;
# benutzen

# __UPDATING SINGLE ROW__
# wenn man einen falschen eintrag gemacht hat in einer zeile kann man UPDATE invoices SET payment_total = 10, pagment_date = "1990-04-03" WHERE client_id = 3;
# -- Updating single row
# UPDATE order_items
# SET product_id = 3*2, quantity = 23
# WHERE order_id = 2 AND product_id = 23
# LIMIT 1;
# nur die erste zeile wo übereinstimmt updaten

# __UPDATING MULTIPLE ROWS__
# Wenn man WHERE order_id = 3; ausführt und order_id kein primary key ist,
# kann man die query nicht ausführen da mysql bei default im safe update mode läuft und es dir nur erlaubt eine zeile zu updaten
# safe update mode ist nur bei mysql workbench nicht wenn man sich normal verbindet
# nachdem man den mode in den einstellungen ausgeschaltet hat und sich erneut verbunden hat, kann man mehrere rows updaten
# wenn man jede zeile updaten will kann man auch WHERE auslassen

# __SUBQUERYS IN UPDATES__
# wenn man zuerst herausfinden muss welche zeile man updaten will braucht man ein select statement zuerst und man kann das select statement direkt einbauen
# UPDATE bonus_program
# SET points = points + 50
# WHERE
# 	client_id = (
#     SELECT client_id
#     FROM customers
#     WHERE first_name = "ANNA"
#     )
# ;
# Mysql wird zuerst das select statement ausführen und dann mit bonus_program.client_id vergleichen 
# wenn das select statement mehrere dinge zurückgibt, muss man statt = IN schreiben
# UPDATE bonus_programm
# SET payback_points = payback_points + 50
# WHERE
# 	bonus_programm.customer_id IN (
#     SELECT customer_id
#     FROM customers
#     WHERE birthdate < "1990-03-12"
#     )
# ;
# query sucht zuerst alle customer_ids wo das statement zutrifft und vergleicht dann ob bonus_programm.customer_id darin enthalten ist
# man kann aber auch
# UPDATE bonus_programm b
# JOIN customers c
# 	ON c.customer_id = b.customer_id
# SET payback_points = payback_points + 50
# WHERE c.date < "1990-11-11"
# ;
# schreiben was oft schneller ist

# __DELETING ROWS__
# Fürs löschen von zeilen benutzt man DELETE FROM tabelle WHERE x = y;
# man kann auch DELETE FROM tabelle WHERE x IN (SELECT x FROM tabelle WHERE x > y); schreiben, der syntax ist ähnlich zu einem update - set  statement

# __RESTORING DATABASES__
# wenn man eine database von einem bestimmten zeitpunkt resotren will, muss man die skripts ausführen

# __CASCADE__
# Wenn in der Parent-Tabelle etwas gelöscht oder aktualisiert wird, führe die gleiche Aktion automatisch in der Child-Tabelle aus.
# 1.	ON DELETE CASCADE
# •	Wenn der referenzierte Datensatz gelöscht wird, werden automatisch alle Zeilen gelöscht, die auf ihn zeigen.
# •	Beispiel: Benutzer gelöscht → alle Posts des Benutzers werden ebenfalls gelöscht.
# 2.	ON UPDATE CASCADE
# •	Wenn der referenzierte Wert geändert wird, werden automatisch alle FK-Spalten aktualisiert, die darauf verweisen.
# •	Beispiel: Benutzer-ID geändert → alle Posts, Kommentare, Votes mit dieser Benutzer-ID werden automatisch angepasst.
# 3. RESTRICT / NO ACTION
# blockiert die löschung solange das child existiert

# __CHECK__
# Check ist constraint / regel in sql die jede zeile einer tabelle erfüllen muss, CHECK (age>18) -> Age muss größer als 18 in jeder zeile sein

# __AS__
# man kann bei (payback_points + 23) % 12 AS Discounted_points, AS verwenden um der Tabelle in der Ansicht einen namen zu geben
# man muss nicht AS schreiben, standartmäßig nimmt es die rechnung zb 12*42/2 als namen

# __Line Breaks__
# Line Breaks werden als whitespace gezählt und mehr als ein whitespace zwischen dingen wird ignoriert 

# __KOMMENTAR_:
# kommentar wird mit -- gemacht und wird nicht ausgeführt

# __INTS__
# SQL spalten haben Feste Datentypen, MSQL muss schon vorher wissen wie viele BYTES reserviert werden sollen, dadurch liegt speicher vorhersehbar, gibt dadurch um die größe zu wissen INT, BIGINT, TINYINT; VARCHAR(n) usw.
# SMALLINT zb nur 2 Bytes im speicher, wenn man überall BigINT nimmt dann hat die Tabelle viel mehr speicher

# __Relations___
# Relation wenn man zb eine spalte cosumer_id hat mit customer_id und dann eine tabelle mit cusotmers mit genauen infos zum customer und seiner ID ist das eine Relation

# __Indexe__
# Primar schlüssel sit immer automatisch ein index, er hilft datenbank sehr schnell zu durchsuchen
# Bei Tabelle mit 400000 werten müsste mysql einen full table scan machen und jeden wert durchsuchen mit Index geht es logaritmisch weil es baum ist
# Index verweist intern auf den zeilennamen in der tabelle
# Index (B-Baum):
# 1 → Zeile 1
# 2 → Zeile 2
# 3 → Zeile 3
#         50
#        /  \
#      20    80
#     / \    / \
#    10 30  60 90
# wenn Id = 60 kann man logaritmisch vergleichen und kommt in log(n) schritten zum ziel, die 60 node verweist auf eigentliche zeile in der tabelle
	# •	Blätter (10, 30, 60, 90)
	# •	Enthalten die Keys
	# •	Plus Pointer auf die tatsächliche Datenzeile
# inneren Knoten enthalten nur Trennwerte
#         [50]  <- Root (Trennwert)
#        /    \
#    [20]      [60] <- Innere Knoten (Trennwerte)
#   /  \      /  \
# [10 30]  [50 60 80 90] <- Blätter, alle Keys enthalten
# MYSQL erstellt automatisch index bei Primary Key oder bei CREATE INDEX idx_age ON users(age); -> damit optimiert man zeile fürs sortieren, mysql erstellt dann automatisch index für die spalte