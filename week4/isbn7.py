# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/387454511

# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/387454511
def isISBN10(code):
    """
    Gaat na of de gegeven ISBN-10 code geldig is.
    >>> isISBN10(’9971502100’)
    True
    >>> isISBN10(’9971502108’)
    False
    """

    # hulpfunctie voor berekening van ISBN-10 controlecijfer
    def controlecijfer(code):
        # controlecijfer berekenen
        controle = sum((i + 1) * int(code[i]) for i in range(9)) % 11
        # controlecijfer omzetten naar stringvoorstelling
        return 'X' if controle == 10 else str(controle)
        # controleer of de gegeven code een string is

    if not isinstance(code, str):
        return False
    # controleer of de gegeven code bestaat uit 10 karakters
    if len(code) != 10:
        return False
    # controleer of de eerste negen karakters van de gegeven code cijfers zijn
    if not code[:9].isdigit():
        return False
    # controleer het controlecijfer van de gegeven code
    return controlecijfer(code) == code[-1]


def isISBN13(code):
    """
    Gaat na of de gegeven ISBN-13 code geldig is.
    >>> isISBN13(’9789743159664’)
    True
    >>> isISBN13(’9787954527409’)
    False
    >>> isISBN13(’8799743159665’)
    False
    """

    # hulpfunctie voor berekening van ISBN-13 controlecijfer
    def controlecijfer(code):
        # controlecijfer berekenen
        controle = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
        # controlecijfer omzetten naar één enkel cijfer
        return str((10 - controle) % 10)
        # controleer of de gegeven code een string is

    if not isinstance(code, str):
        return False
    # controleer of de gegeven code bestaat uit 13 karakters
    if len(code) != 13:
        return False

    # controleer of alle karakters van de gegeven code cijfers zijn
    if not code.isdigit():
        return False
    # controleer het controlecijfer van de gegeven code
    return controlecijfer(code) == code[-1]


def isISBN(code, isbn13=True):
    return isISBN13(code) if isbn13 else isISBN10(code)


def zijnISBN(codes, isbn13=None):
    controles = []

    for code in codes:
        if isinstance(code, str):
            if isbn13 is None:
                controles.append(isISBN(code, len(code) == 13))
            else:
                controles.append(isISBN(code, isbn13))
        else:
            controles.append(False)

    return controles


if __name__ == '__main__':
    import doctest

    doctest.testmod()
