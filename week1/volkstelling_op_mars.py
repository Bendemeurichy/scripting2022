# https://dodona.ugent.be/nl/courses/1151/series/12986/activities/73914958
import math


# source: https://www.pythonpool.com/check-if-number-is-prime-in-python/
def isprime(num):
    return all(num % k != 0 for k in range(2, int(num ** 1 / 2) + 1))


n = int(input())
m = int(input())
prod = int(0)
i = int(math.sqrt(n))

while prod == int(0):
    if (n <= (i ** 2) <= m) and isprime(i):
        prod = int(i)
    i += 1

print(f'Er zijn {prod} marsmannetjes met elk {prod} vingers.')
