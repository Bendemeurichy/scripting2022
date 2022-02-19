# https://dodona.ugent.be/nl/courses/1151/series/12986/activities/1898834779

eerste_cijfer = input()
while eerste_cijfer != 'stop':

    berekend_controlecijfer = int(eerste_cijfer)
    for index in range(2, 10):
        volgende_cijfer = int(input())
        berekend_controlecijfer += index * volgende_cijfer
    berekend_controlecijfer %= 11

    gegeven_controlecijfer = int(input())

    print('OK' if gegeven_controlecijfer == berekend_controlecijfer else 'FOUT')

    eerste_cijfer = input()
