# https://dodona.ugent.be/nl/courses/1151/series/12990/activities/82601015


def coordinaten(loc):
    res = []
    with open(loc, encoding='UTF-8') as sterren:
        i = 0
        for line in sterren:
            res.extend([(i, el) for el in [ind for ind, el in enumerate(line) if el == "*"]])
            i += 1
    return set(res)


def afwijkingen(loc1, loc2):
    sterren1 = coordinaten(loc1)
    sterren2 = coordinaten(loc2)
    return sterren1 - sterren2, sterren2 - sterren1


def planeten(loc1, loc2):
    res = {}
    keys = list(afwijkingen(loc1, loc2)[1])
    values = list(afwijkingen(loc1, loc2)[0])
    if len(values) != 0:
        for el in keys:
            res[el] = minimizer(el, values)
        return res
    return {key: set() for key in keys}


def minimizer(val1, vergelijk):
    d = ((val1[0] - vergelijk[0][0]) ** 2 + (val1[1] - vergelijk[0][1]) ** 2)
    smallest = {(vergelijk[0])}

    for el in vergelijk[1:]:
        if d > (val1[0] - el[0]) ** 2 + (val1[1] - el[1]) ** 2:
            smallest = {(tuple(el))}
            d = (val1[0] - el[0]) ** 2 + (val1[1] - el[1]) ** 2
        elif d == (val1[0] - el[0]) ** 2 + (
                val1[1] - el[1]) ** 2:
            smallest.add(tuple(el))
    return smallest


def comparator(loc1, loc2):
    res = []
    with open(loc1, encoding='UTF-8') as dim:
        kolom = len(dim.readline()) - 1
    with open(loc1, encoding='UTF-8') as dim:
        rij = len(dim.readlines())
    for i in range(0, rij):
        temp = []
        for _ in range(0, kolom):
            temp.append("-")
        res.append(temp)

    o = afwijkingen(loc1, loc2)[0]
    n = afwijkingen(loc1, loc2)[1]

    for el in coordinaten(loc1):
        res[el[0]][el[1]] = "*"

    for el in o:
        res[el[0]][el[1]] = "o"

    for el in n:
        res[el[0]][el[1]] = "n"

    for i, el in enumerate(res):
        res[i] = "".join(el)
    return "\n".join(map(str, res))
