# Viikkoraportti 6

Huomasin, että keskeneräinen A* algoritmi oli käytännössä valmis Greedy Best-First algoritmi, joten lisäsin sen sovellukseen ja tein uuden A* algoritmin.

Algoritmin tuottamat polut olivat tylsiä. Löysin [netistä](https://www.redblobgames.com/pathfinding/a-star/implementation.html) ohjeen, miten poluista saa oikeamman näköisiä (vaihdellaan solun naapureiden läpikäyntijärjestystä).

---

Sovelluksessa on tällä hetkellä iso bugi: tein polun etsimisen visualisoinnin luomalla uuden threadin, joka päivittäisi kartan QPixmap oliota tietyllä nopeudella.
Qt kuitenkin ilmeisesti myös käyttää threadejä QPixmapin piirtämiseen eikä osaa tarkistaa kirjoitetaanko olion muistiin main-threadin ulkopuolella.

Mahdollinen ratkaisu on siirtää koko käyttöliittymä omaan threadiin ja kaikki QPixmapin kirjoittamiseen liittyvä koodi main-threadiin.