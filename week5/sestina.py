# https://dodona.ugent.be/nl/courses/1151/series/12990/activities/678203984
import re


def eindwoord(tekst):
    return re.sub("^.*[^A-Z]([A-Z]+)[^A-Z]*$", r"\1", tekst, flags=re.IGNORECASE)


def stanzas(loc):
    lijst = [[]]
    with open(loc, encoding='UTF-8') as gedicht:
        i = 0
        prev = '\n'
        for line in gedicht:
            if line == "\n" and prev != "\n":
                i += 1
                lijst.append([])
            elif not (line == "\n" and prev == "\n"):
                lijst[i].append(eindwoord(line).lower())
            prev = line
    return lijst


def permutatie(lijst, volgorde=None):
    if volgorde is None:
        helft = len(lijst) // 2
        achter = lijst[helft:]
        achter.reverse()
        voor = lijst[:helft]
        res = [item for sublist in zip(achter, voor) for item in sublist]
        if len(achter) > len(voor):
            res.append(achter[-1])
        return res

    if len(set(volgorde)) != len(lijst):
        raise AssertionError('ongeldige permutatie')
    for i, _ in enumerate(lijst):
        if i + 1 not in volgorde:
            raise AssertionError('ongeldige permutatie')

    res = []
    for el in volgorde:
        res.append(lijst[el - 1])
    return res


def sestina(loc, volgorde=None):
    gedicht = stanzas(loc)
    if len(gedicht) == len(gedicht[0]):
        for i in range(0, len(gedicht) - 1):
            if permutatie(gedicht[i], volgorde) != gedicht[i + 1]:
                return False
        return True
    elif len(gedicht) == len(gedicht[0]) + 1:
        for i in range(0, len(gedicht) - 2):
            if permutatie(gedicht[i], volgorde) != gedicht[i + 1]:
                return False
        if len(gedicht[-1]) != len(gedicht[0]) // 2:
            return False

        for el in gedicht[-1]:
            if el not in gedicht[0]:
                return False
        return True
    return False
