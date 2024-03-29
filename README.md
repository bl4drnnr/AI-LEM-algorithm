# AI-LEM-algorithm

### Toolbox

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Description
Prototype of LEM AI generating rules algorithm.

### Status

11.04.2022
- Basic dependencies, start development stage.

24.04.2022
- Basic working prototype, that is able to generate only one single rule.

27.04.2022
- Basic working prototype, that is able to generate more complex rules.

### Example of working

All you need to do is just put your JSON data in `inputdata` in `input.json` file.

There is only **one** condition for the correct operation of the algorithm.

- Decision parameter needs to be placed on last place of every input record in `JSON`.

As a result you will get the table, that is going to look like this one,
where on the left side you can see index of the records and on the right side, after `-` symbol
you can see generated rule for this record. For example, you see in `input.json` you will see
this outcome.

---

```
1 - IF Typ = kompakt THEN Zuzycie = srednie - [5, 6, 7]
2 - IF Cena = akceptowalna AND Typ = duzy THEN Zuzycie = srednie - [1, 2]
3 - IF Cena = wysoka AND Typ = maly AND Predkosc = mala THEN Zuzycie = srednie - [9]
4 - IF Typ = duzy AND Cena = wysoka THEN Zuzycie = wysokie - [3, 4, 10]
5 - IF Typ = maly AND Cena = akceptowalna THEN Zuzycie = male - [8]
```
