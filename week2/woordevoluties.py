# https://dodona.ugent.be/nl/courses/1151/series/12987/activities/1713291174
woord = input()
letter = input()
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

verschil = int(Alphabet.index(letter) - Alphabet.index(woord[0]))
if verschil < 0:
    verschil = 26 + verschil

for element in woord:
    nieuweLetter = Alphabet[(Alphabet.index(element) + verschil) % 26]
    interval = (Alphabet[Alphabet.index(element) + 1:(Alphabet.index(element) + verschil)])

    if (Alphabet.index(element) + verschil) > 26:
        interval += Alphabet[0:(Alphabet.index(element) + verschil) % 26]

    print(f"{element}{interval.lower()}{nieuweLetter}")
