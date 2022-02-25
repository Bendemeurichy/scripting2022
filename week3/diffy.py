# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/636597847

def volgende(lijst):
    nextducci = []

    for i, element in enumerate(lijst):
        bereken = lambda el1, el2: el2 - el1 if el2 > el1 else el1 - el2
        nextducci.append(bereken(element, lijst[(i + 1) % len(lijst)]))

    return tuple(nextducci)


def ducci(lijst):
    fullducci = []
    fullducci.append(tuple(lijst))

    if all([v == 0 for v in lijst]):
        return tuple(fullducci)

    tempducci = volgende(tuple(lijst))

    while tempducci not in fullducci and not all([v == 0 for v in tempducci]):
        fullducci.append(tuple(tempducci))
        tempducci = volgende(tempducci)

    fullducci.append(tempducci)
    return tuple(fullducci)


def periode(lijst):
    duccilijst = list(ducci(lijst))
    lastEl = duccilijst[-1]

    if not all([v == 0 for v in lastEl]):
        index = duccilijst.index(lastEl)
        return len(duccilijst) - index - 1

    return 0
