# https://dodona.ugent.be/nl/courses/264/series/3260/activities/659392988/#
import functools


class Maan:
    def __init__(self, val):
        if not (isinstance(val, (int, float)) and val >= 0):
            raise AssertionError("ongeldige waarde")
        self.val = int(val)

    def __int__(self):
        return self.val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f"Maan({self.val})"

    def __add__(self, other):
        temp = ""
        if isinstance(other, Maan):
            smallest: int = self.val if len(str(self.val)) < len(
                str(other.val)) else other.val
            largest: int = self.val if len(str(self.val)) >= len(
                str(other.val)) else other.val
        else:
            smallest: int = self.val if len(
                str(self.val)) < len(str(other)) else other
            largest: int = self.val if len(
                str(self.val)) >= len(str(other)) else other
        for _ in range(0, len(str(largest))):
            temp += str(smallest %
                        10) if smallest % 10 > largest % 10 else str(largest % 10)
            smallest //= 10
            largest //= 10

        return Maan(int(temp[::-1]))

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        mult = []

        if isinstance(other, Maan):
            smallest: int = self.val if len(str(self.val)) < len(
                str(other.val)) else other.val
            largest: int = self.val if len(str(self.val)) >= len(
                str(other.val)) else other.val
        else:
            smallest: int = self.val if len(
                str(self.val)) < len(str(other)) else other
            largest: int = self.val if len(
                str(self.val)) >= len(str(other)) else other
        for el in str(smallest)[::-1]:
            temp = "0" * len(mult)
            for k in str(largest)[::-1]:
                temp += el if el < k else k

            mult.append(Maan(int(temp[::-1])))
        return functools.reduce(lambda a, b: a + b, mult)

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power):
        if isinstance(power, Maan):
            power = power.val
        temp = self
        for _ in range(0, power - 1):
            temp *= self
        return temp

    def __rpow__(self, other):
        return Maan(other) ** self
