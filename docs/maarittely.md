# Määrittelydokumentti

*Pathfinger (working title)* on pythonilla toteuttu polunetsintäsovellus graafisella käyttöliittymällä.
Käyttöliittymässä käytetään PyQt6 -kirjastoa.

Sovelluksella voi luoda yksinkertaisia karttoja jotka koostuvat ruudukosta jonka jokainen ruutu on joko seinä tai lattia. Karttoja voi generoida automaattisesti ja niitä voi myös itse muokata ja piirtää. Sovelluksessa on toiminnallisuudet karttojen tallentamiseen ja avaamiseen.

Pääpaino sovelluksessa kuitenkin on polunetsintä kahden kartan mielivaltaisen pisteen välillä, jotka käyttäjä voi valita hiirellä. Sovelluksesta näkee visuaalisesti eri algoritmeillä saadut polut ja niihin liittyvät statistiikat.

Mukana olevia polunetsintäalgoritmejä ovat ainakin Dijkstra ( O(m log n) ), IDA* ( O(d) ) ja JPS ( O(\sqrt{n}) ). Muita algoritmejä toteutetaan sovellukseen ajan puitteissa.

---

Valitsin kyseisen aiheen, koska se vaikuttaa aiheelta jonka ehtii toteuttaa huolellisesti kurssin aikana ja polunetsintä vaikuttaa hyvin keskeiseltä ongelmalta ohjelmoinnissa.

Projektin dokumentaatio kirjoitetaan suomeksi.

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)

Pathfinger on toteutettu pythonin 3.8.3 -versiolla.

Vertaisarviointeja voin tehdä python-, java-, C#-, javascript-, typescript- ja rust-projekteihin.
