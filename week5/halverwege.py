# https://dodona.ugent.be/nl/courses/1151/series/12990/activities/14689798

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def lees_standaard(loc):
    res = {}
    with open(loc, encoding='UTF-8') as codes:
        next(codes)
        for line in codes:
            cline = line.split(";")
            res[cline[0]] = tuple(cline[1:4])
    return res


def omkeren(landcodes):
    return {value[1]: key for (key, value) in landcodes.items()}


def middelletter(letter1, letter2, asymmetrisch=False):
    if (alphabet.index(letter1) - alphabet.index(letter2)) % 2 == 1:
        raise AssertionError("geen middelpunt")

    if asymmetrisch:
        if alphabet.index(letter1) > alphabet.index(letter2):
            return alphabet[alphabet.index(letter1) + (
                    alphabet.index(letter2, alphabet.index(letter1)) - alphabet.index(letter1)) // 2]
    return alphabet[alphabet.index(letter1) - (alphabet.index(letter1) - alphabet.index(letter2)) // 2]


def middelcode(code1, code2, asymmetrisch=False):
    res = ""
    for i in range(3):
        res += middelletter(code1[i], code2[i], asymmetrisch)
    return res


def halverwege(land1, land2, codes, asymmetrisch=False):
    try:
        nland = middelcode(codes[land1][1], codes[land2][1], asymmetrisch)
        return omkeren(codes)[nland]
    except:
        raise AssertionError("geen middelpunt")
