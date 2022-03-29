# https://dodona.ugent.be/nl/courses/1151/series/12991/activities/341848809


class ISBN13:
    """
    >>> code = ISBN13(9780136110675)
    >>> print(code)
    978-0-13611067-5
    >>> code
    ISBN13(9780136110675, 1)
    >>> code.isgeldig()
    True
    >>> code.alsISBN10()
    '0-13611067-3'
    >>> ISBN13(9780136110675, 6)
    Traceback (most recent call last):
    AssertionError: ongeldige ISBN code
    """

    def __init__(self, code, lengte=1):
        # controleer geldigheid van argumenten
        boodschap = 'ongeldige ISBN code'
        if not isinstance(code, int):
            raise AssertionError(boodschap)
        if not (isinstance(lengte, int) and 1 <= lengte <= 5):
            raise AssertionError(boodschap)
        # objecteigenschappen: ISBN-code en lengte van landaanduiding
        # omzetten naar string van 13 karakters met voorloopnullen
        self.code = str(code).zfill(13)
        self.lengte = lengte

    def __int__(self):
        return int(self.code)

    def __str__(self):
        # opgemaakte versie van ISBN-code teruggeven
        c = self.code
        return f'{c[:3]}-{c[3:3 + self.lengte]}-{c[3 + self.lengte:-1]}-{c[-1]}'

    def __repr__(self):
        # string teruggeven met Python expressie die resulteert in een nieuw
        # object met dezelfde toestand als het huidige object
        return f'ISBN13({int(self)}, {self.lengte})'

    def isgeldig(self):
        def controlecijfer(code):
            # ISBN-13 controlecijfer berekenen
            controle = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
            # controlecijfer omzetten naar stringvoorstelling
            return str((10 - controle) % 10)
            # nagaan of controlecijfer geldig is

        return self.code[12] == controlecijfer(self.code)

    def alsISBN10(self):
        def controlecijfer(code):
            # ISBN-10 controlecijfer berekenen
            controle = sum((i + 1) * int(code[i]) for i in range(9)) % 11
            # controlecijfer omzetten naar stringvoorstelling
            return "X" if controle == 10 else str(controle)

        # geen resultaat teruggeven voor ongeldige ISBN-13 codes
        if not self.isgeldig() or self.code[:3] != '978':
            return None
        # ISBN-13 code omzetten naar ISBN-10 code
        code = self.code[3:-1]
        controle = controlecijfer(code)
        return f'{code[:self.lengte]}-{code[self.lengte:]}-{controle}'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
