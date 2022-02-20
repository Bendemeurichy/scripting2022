# https://dodona.ugent.be/nl/courses/1151/series/12987/activities/174432505
# eerste ISBN-10 code (of het woord stop) inlezen
code = input()
# opeenvolgende ISBN-10 codes inlezen totdat regel met "stop" ingelezen wordt
while code != "stop":
    # controlecijfer berekenen
    controlecijfer = int(code[0])
    for i in range(2, 10):
        controlecijfer += i * int(code[i - 1])
        controlecijfer %= 11

    # controlecijfer extraheren uit ingelezen ISBN-10 code
    x10 = code[-1]
    # nagaan of berekende en geëxtraheerde controlecijfers gelijk zijn
    if (controlecijfer == 10 and x10 == "X") or x10 == str(controlecijfer):
        print("OK")
    else:
        print("FOUT")
    # volgende ISBN-10 code (of het woord stop) inlezen
    code = input()
