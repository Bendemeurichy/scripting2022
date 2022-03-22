# https://dodona.ugent.be/nl/courses/1151/series/12991/activities/1200797771


class Display:
    letters = ""
    licht = {'A': ["-", 0, [1, 2]], 'B': ["|", 1, [3]], 'C': ['|', 3, [3]], 'D': ['-', 4, [1, 2]],
             'E': ['|', 3, [0]], 'F': ['|', 1, [0]], 'G': ['-', 2, [1, 2]]}

    def __init__(self, getal):
        assert all(el in self.licht and getal.count(el) ==
                   1 for el in getal), "ongeldige segmenten"
        self.letters = getal

    def __repr__(self):
        return __class__.__name__ + f"('{''.join((sorted(self.letters)))}')"

    def __str__(self):
        res = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ']]
        for el in self.letters:
            val = self.licht[el]
            for i in val[2]:
                res[val[1]][i] = val[0]
        res = ["".join(el) for el in res]
        return "\n".join(res)

    def __len__(self):
        return len(self.letters)

    def __and__(self, other):
        return Display(''.join([el for el in self.letters if el in other.letters]))

    def __sub__(self, other):
        return Display(''.join([el for el in self.letters if el not in other.letters]))

    def __or__(self, other):
        return Display(''.join(list(set(self.letters + other.letters))))

    def __xor__(self, other):
        return Display(''.join([el for el in (self | other).letters if el not in (self & other).letters]))

    def __invert__(self):
        return Display(''.join([el for el in self.licht if el not in self.letters]))
