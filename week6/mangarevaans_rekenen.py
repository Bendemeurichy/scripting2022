# https://dodona.ugent.be/nl/courses/1151/series/12991/activities/2129134533
import re


class Mangarevaans:
    symbols = {"K": 10, "P": 20, "T": 40, "V": 80}
    value = 0

    def __init__(self, number):
        if type(number) == int:
            assert (1 <= number <= 799), "ongeldige waarde"
            self.value = number
        elif type(number) == str and re.match("^[0-9]?V?T?P?K?[0-9]?$", number) is not None:
            letterv = 0
            a80 = int(number[0]) if (number[0]).isdigit() else 1
            for el in re.sub("[0-9]", "", number):
                letterv += self.symbols[el] * a80 if el == "V" else self.symbols[el]

            eenheden = int(number[-1]) if number[-1].isdigit() else 0
            self.value = letterv + eenheden
        else:
            raise AssertionError("ongeldige waarde")

    def __int__(self):
        return self.value

    def __str__(self):
        value = self.value
        res = ""
        if value // 80 > 0:
            res += f"{value // 80}V"
            value -= value // 80 * 80

        if value // 40 > 0:
            res += "T"
            value -= 40

        if value // 20 > 0:
            res += "P"
            value -= 20

        if value // 10 > 0:
            res += "K"
            value -= 10
        res += str(value) if value != 0 else ""
        return res

    def __repr__(self):
        return f"Mangarevaans('{str(self)}')"

    def __add__(self, other):
        try:
            return Mangarevaans(self.value + other.value)
        except AttributeError:
            return Mangarevaans(self.value + other)

    def __radd__(self, other):
        return Mangarevaans(self.value + other)

    def __sub__(self, other):
        try:
            return Mangarevaans(self.value - other.value)
        except AttributeError:
            return Mangarevaans(self.value - other)

    def __rsub__(self, other):
        return Mangarevaans(other - self.value)

    def __mod__(self, other):
        try:
            return Mangarevaans(self.value % other.value)
        except AttributeError:
            return Mangarevaans(self.value % other)

    def __rmod__(self, other):
        return Mangarevaans(other % self.value)

    def __mul__(self, other):
        try:
            return Mangarevaans(self.value * other.value)
        except AttributeError:
            return Mangarevaans(self.value * other)

    def __rmul__(self, other):
        return Mangarevaans(other * self.value)

    def __pow__(self, power):
        try:
            return Mangarevaans(self.value**power.value)
        except AttributeError:
            return Mangarevaans(self.value**power)

    def __rpow__(self, other):
        return Mangarevaans(other**self.value)

    def __floordiv__(self, other):
        try:
            return Mangarevaans(self.value//other.value)
        except AttributeError:
            return Mangarevaans(self.value//other)

    def __rfloordiv__(self, other):
        return Mangarevaans(other//self.value)
