# Ilari's openings
Shakkiavauksen Harjoitussovellus.

Tämä sovellus auttaa käyttäjiä oppimaan ja harjoittelemaan shakkiavauksia. Käyttäjät voivat rekisteröityä, kirjautua sisään ja valita ennalta määritellyistä avauksista. Sovellus näyttää siirrot vaihe vaiheelta, sisältää kommentteja ja tarjoaa mahdollisuuden testata muistia siirtojärjestyksestä.

## Asennusohjeet

1. Kloonaa repositorio koneellesi ja navigoi sen hakemistoon "ilaris-openings"
```bash
git clone git@github.com:ranilar/ot-harjoitustyo.git
```

3. Asenna riippuvuudet
```bash
poetry install
```

3. Käynnistä sovellus
```bash
poetry run invoke start
```

## Komennot

- Käynnistä sovellus
```bash
poetry run invoke start
```

- Suorita testit
```bash
poetry run invoke test
```

- Tee testikattavuusraportti
```bash
poetry run invoke coverage-report
```

- Pylint tarkistukset
```bash
poetry run invoke lint
```
## Dokumentaatio

-  [Vaatimusmäärittely](ilaris-openings/dokumentaatio/vaatimusmaarittely.md)
-  [Työaikakirjanpito](ilaris-openings/dokumentaatio/tuntikirjanpito.md)
-  [Changelog](ilaris-openings/dokumentaatio/changelog.md)
-  [Release] (https://github.com/ranilar/ot-harjoitustyo/releases/tag/viikko5)
-  [Arkkitehtuuri -dokumentti](ilaris-openings/dokumentaatio/arkkitehtuuri.md)

