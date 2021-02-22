import sys
import re

parsingStage = 0  # 0: start, 1: AnaDegiskenler, 2: YeniDegiskenler, 3: Sonuc
tDigits = ['sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz']
keywords = ['AnaDegiskenler', 'YeniDegiskenler', 'Sonuc', 'degeri', 'olsun', 'dogru', 'yanlis',
            'ac-parantez', 'kapa-parantez', '(', ')', 'arti', 'eksi', 'carpi', '+', '-', '*',
            'nokta', 've', 'veya'] + tDigits
var = []
avar = []
lvar = []


def syntax_error():
    with open('calc.out', 'w') as f:
        f.write('Dont Let Me Down')
    sys.exit()


def replace_numerals(lst):
    for i in range(len(lst)):
        if lst[i] in tDigits:
            lst[i] = '_tdigit'
        elif re.search(r'^\d\.\d$|^\d$', lst[i]):
            lst[i] = '_aterm'

    for i in range(len(lst)):
        if lst[i] == 'nokta':
            if i == 0 or i == len(lst) - 1:
                syntax_error()
            if not (lst[i - 1] == '_tdigit' and lst[i + 1] == '_tdigit'):
                syntax_error()

            lst[i] = '_aterm'
            lst[i - 1] = '_'
            lst[i + 1] = '_'

    lst = [i for i in lst if i != '_']

    for i in range(len(lst)):
        if lst[i] == '_tdigit':
            lst[i] = '_aterm'

    return lst


def replace_logicals(lst):
    for i in range(len(lst)):
        if lst[i] == 'dogru' or lst[i] == 'yanlis':
            lst[i] = '_lterm'

    return lst


def search_illegal_vars(lst):
    for i in range(len(lst)):
        word = lst[i]
        if word[0] == '_':
            continue
        if word not in keywords:
            if word in var or len(word) > 10 or not word.isalnum():
                syntax_error()
            else:
                var.append(word)

    return lst


def calculations(lst):
    for i in range(len(lst)):
        if lst[i] == '_aterm' or lst[i] in avar:
            lst[i] = '_aexp'
        if lst[i] == '_lterm' or lst[i] in lvar:
            lst[i] = '_lexp'

    s = ' '.join(lst)

    while True:
        s_copy = re.sub(r'(ac-parantez|\() _aexp (kapa-parantez|\))', '_aexp', s)
        s_copy = re.sub(r'_aexp ([+\-*]|(arti)|(carpi)|(eksi)) _aexp', '_aexp', s_copy)

        s_copy = re.sub(r'(ac-parantez|\() _lexp (kapa-parantez|\))', '_lexp', s_copy)
        s_copy = re.sub(r'_lexp ((ve)|(veya)) _lexp', '_lexp', s_copy)

        if s_copy == s:
            break
        s = s_copy

    return s.split()


def pull_variables(lst):
    for i in range(len(lst)):
        if lst[i] in avar:
            lst[i] = '_aterm'
        elif lst[i] in lvar:
            lst[i] = '_lterm'
    return lst


with open('calc.in', 'r') as file:
    while True:
        chunk = file.readline()
        if not chunk:
            break

        line = chunk.split()
        if not line:
            continue

        for x in line:
            if '_' in x:
                syntax_error()

        if len(line) == 1:
            if line[0] == 'AnaDegiskenler':
                if parsingStage == 0:
                    parsingStage = 1
                    continue
                else:
                    syntax_error()

            elif line[0] == 'YeniDegiskenler':
                if parsingStage == 1:
                    parsingStage = 2
                    continue
                else:
                    syntax_error()

            elif line[0] == 'Sonuc':
                if parsingStage == 2:
                    parsingStage = 3
                    continue
                else:
                    syntax_error()

        if parsingStage == 0 or parsingStage == 4:
            syntax_error()

        if parsingStage == 1:
            line = replace_numerals(line)
            line = replace_logicals(line)
            line = search_illegal_vars(line)

            if len(line) != 4 or line[0] not in var or line[1] != 'degeri' or line[3] != 'olsun':
                syntax_error()

            if line[2] == '_aterm':
                avar.append(line[0])
            elif line[2] == '_lterm':
                lvar.append(line[0])
            else:
                syntax_error()

        if parsingStage == 2:
            line = replace_numerals(line)
            line = replace_logicals(line)
            line = [line[0]] + pull_variables(line[1:])
            line = search_illegal_vars(line)
            line = calculations(line)

            if len(line) != 4 or line[0] not in var or line[1] != 'degeri' or line[3] != 'olsun':
                syntax_error()

            if line[2] == '_aexp':
                avar.append(line[0])
            elif line[2] == '_lexp':
                lvar.append(line[0])
            else:
                syntax_error()

        if parsingStage == 3:
            line = replace_numerals(line)
            line = replace_logicals(line)
            line = pull_variables(line)
            line = calculations(line)

            if len(line) != 1 or line[0] not in ('_aexp', '_lexp'):
                syntax_error()

            parsingStage = 4

if parsingStage < 3:
    syntax_error()

with open('calc.out', 'w') as out:
    out.write('Here Comes the Sun')
