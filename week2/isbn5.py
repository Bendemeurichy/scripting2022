# https://dodona.ugent.be/nl/courses/1151/series/12987/activities/620641000

def isISBN(code):
    """
    Geeft True terug als het argument een string is die een geldige ISBN-10 code
    bevat. Anders wordt False teruggegeven.
    >>> isISBN("9971502100")
    True
    >>> isISBN("9971502108")
    False
    >>> isISBN("53WKEFF2C")
    False
    >>> isISBN(4378580136)
    False
    """
    # opmerking: isinstance is een ingebouwde functie die een Booleaanse waarde
    # teruggeeft die aangeeft of het eerste argument een object is
    # van het gegevenstype dat als tweede argument wordt doorgegeven
    # aan de functie
    return (
        isinstance(code, str) and  # code moet string zijn
        len(code) == 10 and  # code moet bestaan uit 10 karakters
        code[:9].isdigit() and  # eerste 9 karakters moeten cijfers zijn
        controlecijfer(code) == code[-1]  # controlecijfer moet correct zijn
    )


def controlecijfer(code):
    """
    Berekent het controlecijfer voor een gegeven string die bestaat uit de
    eerste negen cijfers van een ISBN-10 code. Het controlecijfer wordt
    teruggegeven als een string, waarbij de waarde 10 wordt voorgesteld door de
    letter X.
    >>> controlecijfer("997150210")
    "0"
    >>> controlecijfer("938389293")
    "5"
    """
    # controlecijfer berekenen
    controle = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    # controlecijfer omzetten naar stringvoorstelling
    return "X" if controle == 10 else str(controle)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
