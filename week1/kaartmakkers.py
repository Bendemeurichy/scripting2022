# https://dodona.ugent.be/nl/courses/1151/series/12986/activities/42831568
kleur1 = input()
kaart1 = input()
kleur2 = input()
kaart2 = input()

if kaart1 == kaart2:
    if (kleur1 == 'klaveren' and kleur2 == 'schoppen') or (kleur1 == 'schoppen' and kleur2 == 'klaveren'):
        print(f'{kleur1} {kaart1} en {kleur2} {kaart2} zijn makkers')
    elif (kleur1 == 'harten' and kleur2 == 'ruiten') or (kleur1 == 'ruiten' and kleur2 == 'harten'):
        print(f'{kleur1} {kaart1} en {kleur2} {kaart2} zijn makkers')
    else:
        print(f'{kleur1} {kaart1} en {kleur2} {kaart2} zijn geen makkers')
else:
    print(f'{kleur1} {kaart1} en {kleur2} {kaart2} zijn geen makkers')
