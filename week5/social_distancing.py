# https://dodona.ugent.be/nl/courses/1151/series/12990/activities/777728597
import re


def wissen(tewissen, gegeven):
    for el in tewissen:
        gegeven = re.sub('(?i)' + re.escape(el), lambda m: " ", gegeven)
    return gegeven


def weglaten(s, bestand, output=None):
    if output is not None:
        output = open(output, "w")
    with open(bestand) as file:
        for line in file:
            print(wissen(s, line), end="", file=output)


def isconsistent(file1, file2):
    with open(file1) as f1, open(file2) as f2:

        for line1, line2 in zip(f1, f2):
            if len(line1) != len(line2):
                return False
            if not [line1[el] == line2[el] for el in range(len(line1)) if " " not in (line1[el], line2[el])]:
                return False
        return True
