# https://dodona.ugent.be/nl/courses/1151/series/12991/activities/1130089622

class Rooster:

    def __init__(self, s):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        self.sleutel = []
        self.rooster = [[], [], []]
        for el in s.lower():
            if el not in self.sleutel:
                self.sleutel.append(el)
                self.alphabet.remove(el)
        if " " not in s:
            self.alphabet.remove(" ")
            self.sleutel.extend(" ")
            self.sleutel.extend(self.alphabet)
        else:
            self.sleutel.extend(self.alphabet)
        self.rooster[0] = self.sleutel[0:9]
        self.rooster[1] = self.sleutel[9:18]
        self.rooster[2] = self.sleutel[18:27]

    def __str__(self):
        res = ""
        for el in self.rooster:
            res += f"{''.join(el).upper()}\n"
        return res.strip()

    def positie(self, c):
        for el in self.rooster:
            if c.lower() in el:
                return self.rooster.index(el), el.index(c.lower())

    def karakter(self, r, c):
        return self.rooster[r][c].upper()


class Digrafid:
    def __init__(self, s1, s2):
        self.rooster1 = Rooster(s1)
        self.rooster2 = Rooster(s2)

    def triplet(self, digraaf):
        return self.rooster1.positie(digraaf[0])[1], 3 * self.rooster1.positie(digraaf[0])[0] + \
               self.rooster2.positie(digraaf[1])[0], self.rooster2.positie(digraaf[1])[1]

    def digraaf(self, g1, g2, g3):
        return f"{self.rooster1.karakter(g2 // 3, g1)}{self.rooster2.karakter(g2 % 3, g3)}"

    def codeer(self, plain):
        res = ""
        if len(plain) % 6 != 0:
            plain += 'X' * (6 - len(plain) % 6)
            plain = plain.upper()
        for i in range(0, len(plain), 6):
            trip1 = self.triplet(f"{plain[i]}{plain[i + 1]}")
            trip2 = self.triplet(f"{plain[i + 2]}{plain[i + 3]}")
            trip3 = self.triplet(f"{plain[i + 4]}{plain[i + 5]}")
            for k in range(0, 3):
                res += self.digraaf(trip1[k], trip2[k], trip3[k])
        return res

    def decodeer(self, cypher):
        return self.codeer(cypher)
