# https://dodona.ugent.be/nl/courses/1151/series/12987/activities/1605325419
import re
import textwrap

string = re.sub(" +", " ", input().strip())
breedte = int(input())


def cow(width, text):
    print("+" + "-" * (width + 2) + "+")
    for element in text.splitlines():
        print("|" + element.center(width + 2) + "|")
    print("+" + "-" * (width + 2) + "+")
    print("        \\   ^__^")
    print("         \\  (oo)\\_______")
    print("            (__)\\       )\\/\\")
    print("                ||----w |")
    print("                ||     ||")


if len(string) < breedte:
    cow(len(string), string)
else:
    formattedString = textwrap.fill(string, breedte)
    cow(breedte, formattedString)
