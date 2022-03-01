# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/1406306356

def splitsen(t, m):
    res = []
    i = 0
    for _ in range(0, m):
        res.append(t[i:i + len(t) // m])
        i += len(t) // m
    return res


def samenvoegen(reeks):
    return ''.join(reeks)


def halveren(reeks):
    return [el for listlist in [splitsen(tekst, 2) for tekst in reeks] for el in listlist]


def verdubbelen(reeks):
    return [reeks[i] + reeks[i + 1] for i in range(0, len(reeks), 2)]


def verwisselen(reeks):
    res = []
    for i, _ in enumerate(reeks[0]):
        string = ''
        for c, _ in enumerate(reeks):
            string += reeks[c][i]
        res.append(string)
    return res


def verweven(reeks, s):
    res = []
    for i in range(s):
        for c in range(i, len(reeks), s):
            res.append(reeks[c])
    return res


def decoderen(t, m):
    return samenvoegen(verweven(verwisselen(verdubbelen(verweven((halveren(splitsen(t, m))), m))), 2))
