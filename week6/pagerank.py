# https://dodona.ugent.be/nl/courses/1151/series/12991/activities/1652380359
import re


class Netwerk:
    demping = 0
    scores = {}
    verbindingen = {}

    def __init__(self, loc, demping=0.85):
        with open(loc) as netwerk:
            for line in netwerk:
                self.verbindingen[re.sub("[^A-Z]", "", line)[0]] = re.sub("[^A-Z]", "", line)[1:]

        with open(loc) as netwerk:
            stdscorde = 1 / len(netwerk.readlines())

        with open(loc) as netwerk:
            for line in netwerk:
                self.scores[line[0]] = stdscorde

        self.demping = demping

    def __len__(self):
        return len(self.verbindingen)

    def uitgaand(self, label):
        return set(self.verbindingen[label]) if self.verbindingen[label] != "" else set(self.verbindingen)

    def inkomend(self, label):
        return {el for el in self.verbindingen if label in self.verbindingen[el] or self.verbindingen[el] == ""}

    def score(self, label):
        return self.scores[label]

    def volgende_score(self, label):
        som = 0
        for el in self.inkomend(label):
            som += (self.scores[el] / len(self.uitgaand(el)))
        nscore = ((1 - self.demping) / len(self.scores)) + (self.demping * som)
        return nscore

    def scores_bijwerken(self, stappen=1):
        nscores = {}
        for _ in range(0, stappen):
            for el in self.scores:
                nscores[el] = self.volgende_score(el)
            self.scores = nscores

    def scores_initialiseren(self):
        for el in self.scores:
            self.scores[el] = 1 / len(self.scores)

    def rangschikking(self):
        return sorted(self.scores.items(), key=lambda x: (-x[1], x[0]))
