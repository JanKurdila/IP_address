# Sú dve alebo viacere zariadenia v jednej sieti ????

Urobme kód inak ako do teraz, ale nepouživajme taktiež žiadne moduly.
## Návrh na riešenie

      1) Prekonvertujeme dekadicke ip adresy na na jedno celé čislo, pomocou mocnin 256**3,  256**2, 256**1, 256**0
      2) Prekonvertujme opačne celé číslo na jednotlivé 4 oktety
      3) Vypočítajme ip siete ako logický súčin pomoc and
      Porovnáme dve vypočítané siete