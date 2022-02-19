# https://dodona.ugent.be/nl/courses/1151/series/12986/activities/990750894
willekeurig = int(input())
loon = int(input())
aantal = 0
tot = willekeurig
while loon != 'stop':
    aantal += 1
    tot += int(loon)
    print(f'werknemer #{aantal} fluistert €{tot}')
    loon = input()


gemiddeld = float((tot - willekeurig) / aantal)
print('gemiddeld loon: €' "%.2f" % gemiddeld)
