# https://dodona.ugent.be/nl/courses/1151/series/12991/activities/747849983

class Rechthoek:
    def __init__(self, r, k, h, b=None):
        if b is None:
            self.b = h
        else:
            self.b = b
        self.r = r
        self.k = k
        self.h = h

    def __repr__(self):
        return f"Rechthoek({self.r}, {self.k}, {self.h}, {self.b})"

    def oppervlakte(self):
        return self.h * self.b

    def cellen(self):
        res = []
        for el in range(0, self.b):
            for c in range(0, self.h):
                res.append((self.r + c, self.k + el))
        return set(res)

    def __le__(self, other):
        return all(el in other.cellen() for el in self.cellen())

    def __and__(self, other):
        if all(el not in other.cellen() for el in self.cellen()):
            return None
        cel = [el for el in self.cellen() if el in other.cellen()]
        cel.sort(key=lambda x: (x[0], x[1]))
        return Rechthoek(cel[0][0], cel[0][1], (cel[-1][0] - cel[0][0]) + 1, (cel[-1][1] - cel[0][1]) + 1)


class Shikaku:
    def __init__(self, loc):
        self.nummervelden = {}
        self.rechthoeken = []

        with open(loc) as puzzel:
            lijn1 = puzzel.readline()
            self.rijen = int(lijn1[0:lijn1.index(" ") + 1])
            self.kolommen = int(lijn1[lijn1.index(" ") + 1:])

            for line in puzzel:
                self.nummervelden[(int(line[0]), int(line[2]))] = int(line[4:])

    def cellen(self, rechthoek):
        res = []
        rcellen = rechthoek.cellen()
        for el in self.nummervelden:
            if el in rcellen:
                res.append(el)
        return res

    def getallen(self, rechthoek):
        return [self.nummervelden[el] for el in self.cellen(rechthoek)]

    def onbedekt(self):
        res = list(self.nummervelden)
        if len(self.rechthoeken) == 0:
            return set(self.nummervelden)
        for el in self.nummervelden:
            for k in self.rechthoeken:
                if el in k.cellen():
                    res.remove(el)
        return set(res)

    def bedekken(self, rechthoek):
        if not (all(el[0] <= self.rijen and el[1] <= self.kolommen for el in rechthoek.cellen()) and
                all(rechthoek & el is None for el in self.rechthoeken) and len(self.cellen(rechthoek)) == 1 and
                rechthoek.oppervlakte() == self.getallen(rechthoek)[0]):
            raise AssertionError("ongeldige rechthoek")
        self.rechthoeken.append(rechthoek)

    def verwijderen(self, pos):


        if not (any(pos not in self.cellen(el) for el in self.rechthoeken) and pos in self.nummervelden):
            raise AssertionError('ongeldige positie')

        for el in self.rechthoeken:
            if pos in self.cellen(el):
                self.rechthoeken.remove(el)

    def isopgelost(self):
        return len(self.onbedekt()) == 0
