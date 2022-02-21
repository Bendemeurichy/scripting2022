# https://dodona.ugent.be/nl/courses/1151/series/12987/activities/1542049812
import re

getallen = '0123456789'


def zout(handel):
    zouthoeveelheid = 0
    for element in handel:
        if element == '#':
            zouthoeveelheid += 1
    return zouthoeveelheid


def goud(handel):
    goudhoeveelheid = 0
    for element in handel:
        if str(element) in getallen:
            goudhoeveelheid += int(element)
    return goudhoeveelheid


def zout_verwijderen(handel):
    return handel.replace('#', '')


def goud_verwijderen(handel):
    return re.sub('[0-9]', '', handel)


def verhandelen(handel):

    if goud(handel) >= zout(handel):
        handelt = goud_verwijderen(handel)
    elif goud(handel) < zout(handel):
        handelt = zout_verwijderen(handel)
    else:
        handelt = handel
    return handelt
