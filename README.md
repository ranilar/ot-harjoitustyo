# Ohjelmistotekniikka harjoitustyö

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

## Dokumentaatio

-  [Vaatimusmäärittely](ilaris-openings/dokumentaatio/vaatimusmaarittely.md)
-  [Työaikakirjanpito](ilaris-openings/dokumentaatio/tuntikirjanpito.md)
-  [Changelog](ilaris-openings/dokumentaatio/changelog.md)

