# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/276629077
pijltjes = [">", "v", "<", "^"]


def rooster(grootte, seq):
    assert grootte ** 2 == len(seq), "ongeldige argumenten"
    res = []
    i = 0
    for _ in range(grootte):
        res.append(seq[i:i + len(seq) // grootte])
        i += len(seq) // grootte
    return [list(el) for el in res]


def tekst(lijst):
    string = ''
    for el in lijst:
        string += " ".join(el) + "\n"
    return string.strip("\n")


def stap(veld, pos):
    waardes = {">": (0, +1), "v": (+1, 0), "<": (0, -1), "^": (-1, 0)}
    hteken = veld[pos[0]][pos[1]]
    nteken = pijltjes[(pijltjes.index(hteken) + 1) % 4]
    veld[pos[0]][pos[1]] = nteken
    npos = (waardes.get(hteken)[0] + pos[0], waardes.get(hteken)[1] + pos[1])

    if 0 <= npos[0] < len(veld) and 0 <= npos[1] < len(veld):
        return npos
    return pos


def stappen(veld):
    lijst = []
    npos = (len(veld) - 1, 0)
    while npos != (0, len(veld) - 1):
        lijst.append(npos)
        npos = stap(veld, npos)
    lijst.append(npos)
    return lijst
