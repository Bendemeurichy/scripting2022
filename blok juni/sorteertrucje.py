# https://dodona.ugent.be/nl/activities/449438870/#

class Rooster:
    def __init__(self, inp):
        lijst = []
        if isinstance(inp, str):
            with open(inp) as file:
                for line in file:
                    row = " ".join(line.split())
                    lijst.append([int(el) for el in row.split()])
        else:
            lijst = [list(el) for el in inp]
            assert len(inp) > 0, "ongeldig rooster"
        lengte = len(lijst[0]) if len(lijst[0]) > 0 else -1
        assert all(len(el) == lengte for el in lijst) and \
               all(isinstance(item, int) for sublist in lijst for item in sublist), "ongeldig rooster"
        self.veld = lijst

    def grootste(self):
        m = self.veld[0][0]
        for el in self.veld:
            for i in el:
                if i > m:
                    m = i
        return m

    def kleinste(self):
        m = self.veld[0][0]
        for el in self.veld:
            for i in el:
                if i < m:
                    m = i
        return m

    def __str__(self):
        return "\n".join([" ".join([
            f"{str(i): >{len(str(self.grootste())) if len(str(self.grootste())) > len(str(self.kleinste())) else len(str(self.kleinste()))}}"
            for i in el]) for el in self.veld])

    def gesorteerd(self, dalend=False, kolommen=False):
        if kolommen:
            for i, _ in enumerate(self.veld[0]):
                kolom = []
                for el, _ in enumerate(self.veld):
                    kolom.append(self.veld[el][i])
                verg = kolom[:]
                verg.sort(reverse=dalend)
                if kolom != verg:
                    return False
        else:
            for el in self.veld:
                verg = el[:]
                verg.sort(reverse=dalend)
                if el != verg:
                    return False
        return True

    def sorteer(self, dalend=False, kolommen=False):
        raster = []
        if kolommen:
            for i, _ in enumerate(self.veld[0]):
                kolom = []
                for el, _ in enumerate(self.veld):
                    kolom.append(self.veld[el][i])
                raster.append(kolom)
        else:
            raster = self.veld

        for el in raster:
            el.sort(reverse=dalend)

        if kolommen:
            temp = []
            for i, _ in enumerate(raster[0]):
                kolom = []
                for el, _ in enumerate(raster):
                    kolom.append(raster[el][i])
                temp.append(kolom)
            raster = temp
        self.veld = raster
        return self

    def __add__(self, other):
        assert len(self.veld) == len(other.veld), "aantal rijen is verschillend"
        roost = []
        for i, el in enumerate(self.veld):
            temp = el[:]
            temp.extend(other.veld[i])
            roost.append(temp)
        return Rooster(roost)

    def __sub__(self, other):
        assert len(self.veld[0]) == len(other.veld[0]), "aantal kolommen is verschillend"
        roost = self.veld[:]
        roost.extend(other.veld)
        return Rooster(roost)
