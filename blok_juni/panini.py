# https://dodona.ugent.be/nl/activities/1126687163/#


class Panini:
    def __init__(self, collection):
        if not isinstance(collection, (int, list, tuple, set)):
            raise AssertionError("ongeldige stickers")

        ls = []
        ls.extend([collection] if isinstance(collection, int) else collection)
        self.col = []
        if len(ls) != 0:

            if not all(isinstance(el, int) for el in ls):
                raise AssertionError("ongeldige stickers")

            for el in ls:
                if "-" in str(el):
                    for i in range(el.split("-")[0], el.split("-")[1] + 1):
                        self.col.append(i)
                else:
                    self.col.append(el)
            self.col = list(set(self.col))
            self.col.sort()

    def __repr__(self):
        length = 1
        list = []

        if len(self.col) == 0:
            return "".join(list)

        for i in range(1, len(self.col) + 1):

            if (i == len(self.col) or self.col[i] -
                    self.col[i - 1] != 1):

                if length == 1:
                    list.append(str(self.col[i - length]))
                else:
                    temp = (str(self.col[i - length]) +
                            "-" + str(self.col[i - 1]))
                    list.append(temp)

                length = 1

            else:
                length += 1
        return ", ".join(list)

    def __add__(self, other):
        nls = [el for el in self.col]
        nls.extend(other.col)
        return Panini(nls)

    def __sub__(self, other):
        return Panini(set(self.col) - set(other.col))
