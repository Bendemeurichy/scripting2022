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
        print(
            f"{letters[i]} {' '.join(['-' if el is None else str(int(el)) for el in tabel[i]])}")


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

    return {el for el in [student1 + "".join(el) + student2 for el in
                          itertools.permutations([el for el in studentenletters(len(tabel)) if el not in
                                                  (student1, student2)])] if is_ketting(el, tabel)}



# returns list of the letters of the students
def studentenletters(aantal):
    return list(map(chr, range(65, 65 + aantal)))
