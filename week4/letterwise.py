# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/1301698881
import re

keyboard = [" ", "_,@", "ABC", "DEF", "GHI",
            "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


def lees_databank(db):
    dictionair = {}
    with open(db, encoding='UTF-8') as databank:
        for line in databank:
            line = line.replace('\n', '')
            (key, val) = line.split(",")
            dictionair[str(key)] = str(val)
    return dictionair


def combinaties(comb):
    return re.split(" ", re.sub("([0-9]N*)", r" \1", comb))[1:]


def letter(prefix, combinatie, db):
    if len(prefix) > 3:
        prefix = prefix[-3:len(prefix)]
    if prefix not in db:
        prefix = ""
    alph = list(db[prefix])
    mogletters = list(keyboard[int(combinatie.replace("N", ""))])
    volgorde = [el for el in alph if el in mogletters]
    return volgorde[combinatie.count("N") % len(volgorde)]


def woord(lijst, db):
    res = ""
    for el in combinaties(lijst):
        res += (letter(res, el, db))
    return res
