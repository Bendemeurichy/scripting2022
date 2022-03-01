# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/276629077
pijltjes = [">", "V", "<", "^"]


def rooster(grootte, seq):
    if len(seq) == grootte ** 2:
        res = []
        i = 0
        for c in range(grootte):
            res.append(seq[i:i + len(seq) // grootte])
            i += len(seq) // grootte
        return [list(el) for el in res]
    else:
        raise AssertionError("ongeldige argumenten")


def tekst(lijst):
    string = ''
    for el in lijst:
        string += " ".join(el) + "\n"
    return string.strip("\n")
