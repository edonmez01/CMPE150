import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

_filepath = 'main.py'  # Change this line.
subtask = ['X.', 'calc']

with open(_filepath, 'r') as f:
    _code = f.read()

for task in subtask:
    for _i in range(50):
        idx = str(_i)
        if task == 'X.' and len(idx) == 1:
            idx = '0' + idx
        with open('wrong_cases/' + task + idx + ".in", "r") as f:
            _inp = f.read()
        with open('calc.in', 'w') as f:
            f.write(_inp)
        codeOut = StringIO()
        codeErr = StringIO()
        codeInp = StringIO(_inp)

        sys.stdout = codeOut
        sys.stderr = codeErr
        sys.stdin = codeInp

        h = open('calc.out', 'r')
        try:
            exec(_code)
            temp = h.readline()
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            sys.stdin = sys.__stdin__
            if temp != 'Dont Let Me Down':
                print('Wrong Answer! Input: ' + task + idx + ".in")
                print('Your Output: ' + temp)
                print('Desired Output: ' + 'Dont Let Me Down')
                sys.exit()
        except:
            temp = h.readline()
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            sys.stdin = sys.__stdin__
            if sys.exc_info()[0] != SystemExit:
                print('System Error on Input: ' + task + idx + ".in")
                print('Your Output: ' + temp)
                print('Desired Output: ' + 'Dont Let Me Down')
                print('System error: ', sys.exc_info())
                sys.exit()
            elif temp != 'Dont Let Me Down':
                print('Wrong answer on input: ' + task + idx + ".in")
                print('Your Output: ' + temp)
                print('Desired Output: ' + 'Dont Let Me Down')
                sys.exit()

        # _code_out = codeOut.getvalue()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        sys.stdin = sys.__stdin__
        print(task + idx + ".in", 'passed.')
        codeOut.close()
        codeErr.close()

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
sys.stdin = sys.__stdin__

print('Accepted')
print('Your code passed all tests')
