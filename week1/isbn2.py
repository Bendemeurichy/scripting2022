# https://dodona.ugent.be/nl/courses/1151/series/12986/activities/182880102
# tien cijfers van ISBN-10 code inlezen (elk op een afzonderlijke regel)
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
x10 = int(input())
# controlecijfer berekenen
controlecijfer = (
    x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5 + 6 * x6 + 7 * x7 + 8 * x8 + 9 * x9
) % 11
# correctheid controlecijfer testen en uitschrijven
print("OK" if x10 == controlecijfer else "FOUT")
