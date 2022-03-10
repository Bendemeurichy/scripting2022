# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/1652696920
import datetime
from datetime import date


def verjaardag(geboorte, huidig):
    return geboorte.day == huidig.day and huidig.month == geboorte.month


def verweekdag(geboorte, huidig):
    return geboorte.weekday() == huidig.weekday() and huidig.day == geboorte.day


def verhonderddag(geboorte, huidig):
    return (huidig - geboorte).days % 100 == 0


def onjaardag(geboorte, huidig):
    return not verjaardag(geboorte, huidig)


def verjaardagen(geboorte, verjaardag=verjaardag, start=None, einde=date.today()):
    if start is None:
        start = geboorte
    res = []
    while start <= einde:
        if verjaardag(geboorte, start):
            res.append(start)
        start += datetime.timedelta(days=1)
    return tuple(res)
