# https://dodona.ugent.be/nl/courses/1151/series/12986/activities/1477235114
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
h3 = int(input())
m3 = int(input())
h4 = int(input())
m4 = int(input())

i1 = (h4 * 60 + m4) - (h1 * 60 + m1)
i2 = (h3 * 60 + m3) - (h2 * 60 + m2)
ct = int(((i1 - i2) / 2) + (h3 * 60 + m3))

if h4 < h1:
    ct += 720

if h3 < h2:
    ct -= 720

if ct > 1440:
    ct -= 1440

print(ct // 60)
print(ct % 60)
