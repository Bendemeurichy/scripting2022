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


def beginwaarden(n):
    return [el for el in range(0, n + 1) if isbelgisch(n, el)]


def isvlaams(n):
    return isbelgisch(n, int(str(n)[0]))


def iswestvlaams(n):
    return isvlaams(n) and str(n) in "".join(map(str, getallenrij(n, int(str(n)[0]))))[0:len(str(n))]
