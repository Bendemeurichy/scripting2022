# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/1325500143

def samenvoegen(tuple1, tuple2):
    resultaat = []

    for i in range(0, kortste(tuple1, tuple2)):
        resultaat.append(tuple1[i])
        resultaat.append(tuple2[i])
    return resultaat


def kortste(el1, el2):
    return len(el1) if len(el1) < len(el2) else len(el2)


def langste(el1, el2):
    return len(el1) if len(el1) > len(el2) else len(el2)


def weven(tuple1, tuple2):
    tot = []

    for i in range(0, langste(tuple1, tuple2)):
        tot.append(tuple1[i % len(tuple1)])
        tot.append(tuple2[i % len(tuple2)])
    return tot


def ritsen(tuple1, tuple2):
    tot = samenvoegen(tuple1, tuple2)

    for i in range(kortste(tuple1, tuple2), langste(tuple1, tuple2)):
        tot.append(tuple1[i]) if len(tuple1) > len(tuple2) else tot.append(tuple2[i])

    return tot
