# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/534402833
import random
import itertools

eigenschap = {"aantal": ("een", "twee", "drie"), "vulling": ("leeg", "halfvol", "vol"),
              "kleur": ("rood", "groen", "paars"), "vorm": ("ruit", "golf", "ovaal")}


def willekeurige_kaart():
    return tuple([eigenschap.get(el)[random.randint(0, 2)] for el in eigenschap])


def willekeurige_kaarten(n):
    res = []
    while len(res) < n:
        kaart = willekeurige_kaart()
        if kaart not in res:
            res.append(kaart)
    return set(res)


def eigenschappen(*kaarten):
    return set([el[0] for el in kaarten]), set([el[1] for el in kaarten]), set([el[2] for el in kaarten]), set(
        [el[3] for el in kaarten])


def isset(*kaarten):
    return all(len(el) != 2 for el in eigenschappen(*kaarten))


def sets(kaarten):
    return len([el for el in itertools.permutations(kaarten, 3) if isset(*el)])//6
    # //6 door sets die meerdere kereen voorkomen in verschillende volgorde, dus 3! letters dubbele
