# https://dodona.ugent.be/nl/activities/1933332633/#
import copy


class Verkaveling:
    def __init__(self, m, n):
        self.veld = [(["#"] * n) for _ in range(m)]

    def __str__(self):
        return "\n".join(["".join(el) for el in self.veld])

    def reserveer(self, brij, bkol, orij=None, okol=None):
        cp = copy.deepcopy(self.veld)
        orij = brij if orij is None else orij
        okol = bkol if okol is None else okol
        for i in range((orij - brij) + 1):
            for k in range((okol - bkol) + 1):
                if self.veld[brij + i][bkol + k] == "#":
                    self.veld[brij + i][bkol + k] = "-"
                else:
                    self.veld = cp
                    raise AssertionError("perceel kan niet gereserveerd worden")

    def grootstePerceel(self):
        maxarea = 0
        rows = []
        cols = []
        for i in range(0, len(self.veld)):
            rowtemp = []
            coltemp = []
            for j in range(0, len(self.veld[0])):
                rowtemp.append(0)
                coltemp.append(0)
            rows.append(rowtemp)
            cols.append(coltemp)

        for i in range(len(self.veld) - 1, -1, -1):
            for j in range(len(self.veld[0]) - 1, -1, -1):
                area = 0
                if self.veld[i][j] == '#':
                    if i == len(self.veld) - 1:
                        rows[i][j] = 1
                    else:
                        rows[i][j] = rows[i + 1][j] + 1
                    if j == len(self.veld[0]) - 1:
                        cols[i][j] = 1
                    else:
                        cols[i][j] = cols[i][j + 1] + 1
                    area = cols[i][j]
                    mincol = cols[i][j]
                for k in range(1, rows[i][j]):
                    if mincol > cols[i + k][j]:
                        mincol = cols[i + k][j]
                    if (k + 1) * mincol > area:
                        area = (k + 1) * mincol
                maxarea = max(maxarea, area)
        return maxarea
