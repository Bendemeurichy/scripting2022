# https://dodona.ugent.be/nl/courses/1151/series/12987/activities/1515945638
scorelijst = {1: ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'],
              2: ['d', 'g'],
              3: ['b', 'c', 'm', 'p'],
              4: ['f', 'h', 'v', 'w', 'y'],
              5: ['k'],
              8: ['j', 'x'],
              'X': ['q', 'z']}


def find(val):
    for key, element in scorelijst.items():
        if val in element:
            return key


def cijfers(string):
    cijferwoord = ""
    for element in string:
        cijferwoord += str(find(element.lower()))
    return cijferwoord


def ispalindroom(string):
    return cijfers(string) == cijfers(string)[::-1]


def score(string):
    cijferwoord = 0
    multiplier = 1
    for element in string:
        if element.isdigit():
            multiplier = int(element)
        elif find(element.lower()) == 'X':
            cijferwoord += multiplier * 10
            multiplier = 1
        else:
            cijferwoord += multiplier * find(element.lower())
            multiplier = 1
    return cijferwoord
