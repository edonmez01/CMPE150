import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

_filepath = 'main.py'  # Change this line.
subtask = ['B', 'C', 'D', 'E', 'F', 'G', 'X']

with open(_filepath, 'r') as f:
    _code = f.read()

for task in subtask:
    for _i in range(0, 100):
        idx = str(_i)
        if len(idx) == 1:
            idx = '0' + idx
        with open('correct_cases/' + task + '.' + idx + ".in", "r") as f:
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
        except:
            temp = h.readline()
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            sys.stdin = sys.__stdin__
            print('System Error or Wrong Answer! Input: ' + task + '.' + idx + '.in')
            print('Your Output: ' + temp)
            print('Desired Output: ' + 'Here Comes the Sun')
            print('System error: ', sys.exc_info())
            sys.exit()
        temp = h.readline()
        # _code_out = codeOut.getvalue()
        if temp.strip() != 'Here Comes the Sun':
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            sys.stdin = sys.__stdin__
            print('Wrong Answer!')
            print('Input: ' + task + '.' + str(_i) + ".in")
            print('Your output: "' + temp + '"')
            print('Desired output: "' 'Here Comes the Sun' '"')
            sys.exit()
        else:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            sys.stdin = sys.__stdin__
            print(task + '.' + idx + '.in', 'passed.')
        codeOut.close()
        codeErr.close()

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
sys.stdin = sys.__stdin__

print('Accepted')
print('Your code passed all tests')
