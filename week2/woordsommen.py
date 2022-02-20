# https://dodona.ugent.be/nl/courses/1151/series/12987/activities/1252594784
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def letterwaarde(letter):
    """
    >>> letterwaarde('A')
    1
    >>> letterwaarde('j')
    10
    >>> letterwaarde('!')
    0
    """
    if letter.lower() in alphabet:
        return alphabet.index(letter.lower())+1
    else:
        return 0


def woordwaarde(woord):
    """
    >>> woordwaarde('arm')
    32
    >>> woordwaarde('BEND')
    25
    >>> woordwaarde('elbow')
    57
    """
    tot = 0
    for element in woord:
        tot += letterwaarde(element)
    return tot


def iswoordsom(woord1, woord2, woord3):
    """
    >>> iswoordsom('arm', 'BEND', 'elbow')
    True
    >>> iswoordsom('KING', 'chair', 'THRONE')
    True
    >>> iswoordsom('Monty', 'Python', 'SHRUBBERY')
    False
    """
    return (woordwaarde(woord1) + woordwaarde(woord2)) == woordwaarde(woord3)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
