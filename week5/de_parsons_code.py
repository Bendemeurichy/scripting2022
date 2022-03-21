# https://dodona.ugent.be/nl/courses/1151/series/12990/activities/345941930


def maximale_afwijking(code):
    hoogte = [0]
    choogte = 0
    for el in code.upper():
        if el == "U":
            choogte += 1
            hoogte.append(choogte)
        elif el == "D":
            choogte -= 1
            hoogte.append(choogte)
    return min(hoogte), max(hoogte)


def parsons(loc):
    res = list(str(max(open(loc), key=len)))
    with open(loc, encoding="UTF-8") as tekening:
        for line in tekening:
            for c, el in enumerate(line):
                if el != " ":
                    res[c] = el
    tekst = "".join(res)
    tekst = tekst.replace("*", "")
    tekst = tekst.replace("\n", "")
    tekst = tekst.replace("\\", "D")
    tekst = tekst.replace("/", "U")
    tekst = tekst.replace("-", "R")
    return "*" + tekst


def contour(code, loc=None):
    res = []
    lengte = ((abs(maximale_afwijking(code)[0]) + maximale_afwijking(code)[1]) * 2) + 1
    for _ in range(0, lengte):
        res.append("")
    choogte = maximale_afwijking(code)[1] * 2

    def print_spaties(nspatie, lijst=None, ):
        if lijst is None:
            lijst = res
        sp = list(range(len(lijst)))
        sp.remove(nspatie)
        for c in sp:
            lijst[c] += " "

    res[choogte] += "*"
    print_spaties(choogte)
    for el in code.upper():
        if el == "R":
            res[choogte] += "-"
            res[choogte] += "*"
            print_spaties(choogte)
            print_spaties(choogte)

        elif el == "U":
            choogte -= 1
            res[choogte] += "/"
            print_spaties(choogte)
            choogte -= 1
            res[choogte] += "*"
            print_spaties(choogte)

        elif el == "D":
            choogte += 1
            res[choogte] += "\\"
            print_spaties(choogte)
            choogte += 1
            res[choogte] += "*"
            print_spaties(choogte)
    out = "\n".join(res)
    if loc is not None:
        file = open(loc, "w")
        file.write(out)
    else:
        print(out)
