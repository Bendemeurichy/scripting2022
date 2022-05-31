# https://dodona.ugent.be/nl/activities/1861565904/#
import re


class Bijbel:
    def __init__(self, best):
        self.bundle = {}
        with open(best) as file:
            book = ""
            ch = ""
            vnr = ""
            for line in file:
                if re.match(r"\*\*\*[^*]*\*\*\*", line):
                    title = line.replace("*", "")
                    book = title.strip()
                    if book not in self.bundle:
                        self.bundle[book] = {}
                elif re.match(r"\d*:\d*", line):
                    divided = line.split(":")
                    ch = divided[0]
                    vnr = re.match(r'\d*', divided[1]).group(0)
                    txt = ":".join(divided[1:])[len(vnr):]
                    vtxt = txt.strip()
                    if ch in self.bundle[book]:
                        self.bundle[book][ch][vnr] = [vtxt]
                    else:
                        self.bundle[book][ch] = {vnr: [vtxt]}
                elif re.match(r"^.+$", line):
                    self.bundle[book][ch][vnr].append(line.strip())

    def citaat(self, place) -> str:
        res = []
        tot = place.split(":")
        ch = re.sub(r"^.* (\d*)$", r"\1", tot[0])
        book = re.sub(r"\d*$", "", tot[0]).strip()
        verse = (tot[1]).strip()

        if re.match(r'\d*-\d*', verse):
            verse = verse.split("-")
            begin = int(verse[0])
            end = int(verse[1]) + 1
        else:
            begin = int(verse)
            end = begin + 1

        for i in range(begin, end):
            res.append(" ".join(self.bundle[book][ch][str(i)]))
        return " ".join(res).strip()
