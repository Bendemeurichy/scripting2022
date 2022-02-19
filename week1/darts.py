# https://dodona.ugent.be/nl/courses/1151/series/12986/activities/960794524
import math

x = float(input())
y = float(input())

r = math.sqrt(x ** 2 + y ** 2)
if x == 0:
    theta = math.pi / 2
else:
    theta = math.atan(y / x)
if x < 0 < y:
    theta += math.pi
elif x < 0 and y < 0:
    theta += math.pi

punten = 0
if r > 170:
    punten = 0
elif r < 6.35:
    punten = 50
elif r < 15.9:
    punten = 25
else:
    multiplier = 1
    if 160.4 <= r <= 170:
        multiplier = 2
    elif 97.4 <= r <= 107:
        multiplier = 3

    beta = (math.pi / 2) + (math.pi / 20) - theta
    index = math.ceil(beta / (math.pi / 10))
    if index <= 0:
        index = 20 + index

    punten = index * multiplier

print(punten)
