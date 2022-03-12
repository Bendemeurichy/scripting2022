# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/19996627
import random

alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
        "W", "X", "Y", "Z", " "]


def fitness(gekregen, gewenst):
    if len(gekregen) != len(gewenst):
        raise AssertionError("strings moeten even lang zijn")
    c = 0
    for i, el in enumerate(gekregen):
        if el == gewenst[i]:
            c += 1
    return c


def mutatie(gekregen, mutaties=1):
    if mutaties > len(gekregen):
        raise AssertionError("ongeldig aantal mutaties")
    i = 0
    res = list(gekregen)
    geweest = []
    while i < mutaties:

        index = random.randint(0, len(gekregen) - 1)
        if index not in geweest:
            nchar = alph[random.randint(0, 26)]
            if nchar != res[index]:
                i += 1
                geweest.append(index)
                res[index] = nchar
    return "".join(res)


def crossover(w1, w2, punt=None):
    if len(w1) != len(w2):
        raise AssertionError("strings moeten even lang zijn")
    if punt is None:
        punt = random.randint(1, len(w1) - 1)

    if punt >= len(w1) or punt == 0:
        raise AssertionError("ongeldig crossoverpunt")

    return w1[0:punt] + w2[punt:len(w2)], w2[0:punt] + w1[punt:len(w2)]
