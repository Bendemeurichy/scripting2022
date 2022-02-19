# https://dodona.ugent.be/nl/courses/1151/series/12986/activities/1432498809
n = int(input())
hoogste = float(0)

for i in range(0, (n // 2)):
    lift = float(input())
    if lift > hoogste:
        hoogste = lift

lifter = float(0)
i = int(0)
kandidaat = float(0)

while i < (n-(n // 2)) and lifter == 0:
    kandidaat = float(input())
    i += 1
    if kandidaat > hoogste:
        lifter = kandidaat

if lifter == 0:
    lifter = kandidaat

print(lifter)
