# https://dodona.ugent.be/nl/courses/1151/series/12990/activities/2055708402
import urllib.request


def isISBN13(code):
    def controlecijfer(code):
        controle = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
        return str((10 - controle) % 10)

    if not isinstance(code, str):
        return False
    if len(code) != 13:
        return False
    # prefix van de gegeven code controleren
    if code[:3] not in {'978', '979'}:
        return False
    # controleer of alle karakters van de gegeven code cijfers zijn
    if not code.isdigit():
        return False
    # controleer het controlecijfer van de gegeven code
    return controlecijfer(code) == code[-1]


def verwijder_tags(s):
    begin = s.find('<')
    while s.find('<') >= 0:
        einde = s.find('>', begin + 1)
        if einde == -1:
            einde = len(s)
        s = s[:begin] + s[einde + 1:]
        begin = s.find('<')
    return s.strip()


def print_boek_info(code):
    code = code.strip()
    # geldigheid van ISBN-13 code nagaan
    if not isISBN13(code):
        print('Foutieve ISBN-13 code')
    else:
        url = f'http://pythia.ugent.be/pythia-share/exercises/isbn9/books.php?isbn={code}'
        info = urllib.request.urlopen(url)
        # informatie over boek uit antwoord filteren en uitschrijven
        for regel in info:
            regel = regel.decode('utf-8')
            if regel.startswith('<Title>'):
                print(f'Titel: {verwijder_tags(regel)}')
            elif regel.startswith('<AuthorsText>'):
                print(f'Auteurs: {verwijder_tags(regel).rstrip(", ")}')
            elif regel.startswith('<PublisherText '):
                print(f'Uitgever: {verwijder_tags(regel).rstrip(", ")}')
