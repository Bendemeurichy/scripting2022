# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/135042872

def getallenrij(n, k=0, aantal=None):
    spl = [int(i) for i in str(n)]
    w = 0
    res = [k]
    if aantal is None:
        aantal = n
    while k < n:
        k += int(spl[w])
        res.append(k)
        w = (w + 1) % len(spl)
    return res[0:aantal]


def isbelgisch(n, k=0):
    return n in getallenrij(n, k)
