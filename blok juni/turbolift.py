# https://dodona.ugent.be/nl/activities/690012949/#

class Platform:
    OP = 1
    NEER = -1
    STIL = 0

    def __init__(self, stand, richting, laagste=None, hoogste=None):
        self.laagste: int = laagste if laagste is not None else stand
        self.hoogste: int = hoogste if hoogste is not None else stand
        self.stand: int = stand
        assert self.hoogste >= self.laagste and self.laagste <= self.stand <= self.hoogste, "ongeldige configuratie"
        self.richting: int = richting

    def volgende(self):
        if self.hoogste == self.laagste:
            self.richting = Platform.STIL
        elif self.stand == self.hoogste:
            self.richting = Platform.NEER
        elif self.stand == self.laagste:
            self.richting = Platform.OP
        self.stand += self.richting
        return self


class TurboLift:
    def __init__(self):
        self.platforms = []

    def voegtoe(self, platf):
        self.platforms.append(platf)

    def tijdsstappen(self):
        tijd = 0
        plaats = 0
        while plaats < (len(self.platforms)-1) and tijd < 1000:
            tijd += 1
            self.platforms=[el.volgende() for el in self.platforms]
            if int(self.platforms[plaats].stand) == int(self.platforms[plaats + 1].stand):
                plaats += 1
        if tijd == 1000:
            return None
        return tijd
