# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/863170715

def opeenvolgend(myTuples):
    return sorted(myTuples) == list(range(sorted(myTuples)[0], sorted(myTuples)[-1] + 1))


def goudlokje(myTuples):
    correctlist = list(range(sorted(myTuples)[0], sorted(myTuples)[-1] + 1))
    if len(correctlist) - len(myTuples) == 1:
        return (set(correctlist) - set(myTuples)).pop()
    return None


def verhuizen1(myTuples):
    correctlist = list(range(sorted(myTuples)[0], sorted(myTuples)[-1] + 1))
    if len(correctlist) - len(myTuples) == 1:
        returnlist = list(myTuples)
        returnlist.append(goudlokje(myTuples))
        return returnlist
    return list(myTuples)


def verhuizen2(myList):
    correctlist = list(range(sorted(myList)[0], sorted(myList)[-1] + 1))
    if len(correctlist) - len(myList) == 1:
        myList.append(goudlokje(myList))
