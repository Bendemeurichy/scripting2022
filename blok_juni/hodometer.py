# https://dodona.ugent.be/nl/activities/1177565993/#

class OdoMeter:
    def __init__(self, afgelegd=0.0, eenheid=True):
        self.afstand: float = afgelegd
        self.eenheid: str = "km" if eenheid else "mi"

    def __str__(self) -> str:
        return f"{self.afstand:.1f} {self.eenheid}"

    def __repr__(self) -> str:
        return f"OdoMeter({self.afstand:.6f}, {self.eenheid == 'km'})"

    def __add__(self, other):
        self.afstand += other
        return self

    def __sub__(self, other):
        self.afstand = 0.0 if other > self.afstand else self.afstand - other
        return self

    def switch(self):
        convert = 1.609344
        if self.eenheid == "km":
            self.eenheid = "mi"
            self.afstand /= convert
        else:
            self.eenheid = "km"
            self.afstand *= convert
