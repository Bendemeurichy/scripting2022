# https://dodona.ugent.be/nl/activities/1770460000/#
import random


class NaamGenerator:
    def __init__(self):
        self.prefixen = set()
        self.triples = {}
        self.namen = set()

    def naam_toevoegen(self, naam):
        assert naam.capitalize() == naam and len(naam) > 2, "ongeldige naam"
        self.namen.add(naam)
        self.prefixen.add(naam[0:3])
        for i in range(1, len(naam) - 1):
            if naam[i:i + 2] in self.triples:
                self.triples[naam[i:i + 2]].add(naam[i + 2] if i + 2 < len(naam) else "_")
            else:
                self.triples[naam[i:i + 2]] = {naam[i + 2] if i + 2 < len(naam) else "_"}

    def namen_toevoegen(self, bestand):
        with open(bestand) as file:
            for line in file:
                self.naam_toevoegen(line.strip())

    def naam(self):
        nm = random.choice(list(self.prefixen))
        ends = list(self.triples[nm[1:]])
        char = "a"
        while char != "_":
            char = random.choice(ends)
            if char != "_":
                nm += char
                ends = list(self.triples[nm[-2:]])
        if nm in self.namen:
            return self.naam()
        return nm
