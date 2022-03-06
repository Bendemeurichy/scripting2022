# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/70570533

richtingen = {"O": (0, +1), "Z": (+1, 0), "W": (0, -1), "N": (-1, 0)}
aansluitend = {"N": "Z", "Z": "N", "O": "W", "W": "O"}


def dwarsdoorsnede(grootte, veld):
    assert (len(veld) // 2) % grootte == 0, "ongeldige dwarsdoorsnede"
    coordinaten = [(veld[i:i + 2]) for i in range(0, len(veld), 2)]
    return [(coordinaten[i:i + (len(coordinaten) // grootte)]) for i in
            range(0, len(coordinaten), len(coordinaten) // grootte)]


def diepte(doorsnede):
    pos = (0, 0, "N")
    depth = 1

    while npos(pos, doorsnede) != -1:
        pos = npos(pos, doorsnede)
        depth += 1
    return depth


def npos(hpos, doorsnede):
    mog = (doorsnede[hpos[0]][hpos[1]]).replace(hpos[2], '')
    vervolg1 = hpos[0] + (richtingen.get(mog))[0]
    vervolg2 = hpos[1] + (richtingen.get(mog))[1]
    if vervolg1 not in range(0, len(doorsnede)) or vervolg2 not in range(0, len(doorsnede[0])):
        return -1

    if aansluitend.get(mog) in doorsnede[vervolg1][vervolg2]:
        return hpos[0] + (richtingen.get(mog))[0], hpos[1] + (richtingen.get(mog))[1], aansluitend.get(mog)
    return -1
