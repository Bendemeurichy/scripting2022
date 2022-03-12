# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/312941025

import itertools


def vul_tabel(aantal, kenissen):
    res = []
    start = 0
    for i in range(0, aantal):
        temp = [int(el) == 1 for el in kenissen[start:start + ((aantal - i) - 1)]]
        temp.insert(0, None)
        start += (aantal - i) - 1
        for j in range(i, 0, -1):
            temp.insert(0, res[j - 1][i])
        res.append(temp)
    return res


def print_tabel(tabel):
    letters = studentenletters(len(tabel))
    print("  " + " ".join(letters))
    for i, _ in enumerate(tabel):
        for j in range(len(tabel[i])):
            if tabel[i][j]:
                tabel[i][j] = "1"
            elif tabel[i][j] is False:
                tabel[i][j] = "0"
            else:
                tabel[i][j] = "-"

        print(f"{letters[i]} {' '.join(tabel[i])}")


def spreekt_met(persoon, tabel):
    letters = studentenletters(len(tabel))
    return {letters[i] for i in range(len(tabel)) if tabel[letters.index(persoon)][i]}


def spreken_met_elkaar(student1, student2, tabel):
    return student2 in spreekt_met(student1, tabel)


def is_ketting(mogketting, tabel):
    letters = studentenletters(len(tabel))
    for i in range(len(tabel) - 1):
        if mogketting[i] not in letters or not spreken_met_elkaar(mogketting[i], mogketting[i + 1], tabel) \
                or mogketting.count(letters[i]) != 1:
            return False
    if mogketting.count(letters[-1]) != 1:
        return False
    return True


def kettingen(student1, student2, tabel):
    overige = [el for el in studentenletters(
        len(tabel)) if el not in (student1, student2)]

    gewilde = [
        student1 + "".join(el) + student2 for el in itertools.permutations(overige)]
    return {el for el in gewilde if is_ketting(el, tabel)}


def studentenletters(aantal):
    return list(map(chr, range(65, 65 + aantal)))
