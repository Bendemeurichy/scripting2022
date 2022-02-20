# https://dodona.ugent.be/nl/courses/1151/series/12987/activities/350682425
Bewerking = str(input())
tot = int(0)
multiplier = 1


# source: https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
def remove(string):
    return string.replace(" ", "")


Bewerking = remove(Bewerking)
for letter in Bewerking:
    if letter == "-":
        multiplier = -1
    elif letter == "+":
        multiplier = 1
    else:
        tot += multiplier

print(tot)
