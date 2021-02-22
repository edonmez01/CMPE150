import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

_filepath = r'C:\Users\Eren\PycharmProjects\hw4\main.py'

with open(_filepath, 'r') as f:
    _code = f.read()


for _i in range(1, 300):
    with open('test_cases/input' + str(_i) + ".txt", "r") as f:
        _inp = f.read()
    with open('test_cases/output' + str(_i) + ".txt", "r") as f:
        _out = f.read()
    codeOut = StringIO()
    codeErr = StringIO()
    codeInp = StringIO(_inp)

    sys.stdout = codeOut
    sys.stderr = codeErr
    sys.stdin = codeInp
    try:
        exec(_code)
    except:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        sys.stdin = sys.__stdin__
        print('There was an error when trying the input: input' + str(_i) + '.txt')
        print('Your code outputted: ', codeOut.getvalue())
        print('Your code gave an error: ', codeErr.getvalue())
        print('This is the system error: ', sys.exc_info())
        exit()

    _code_out = codeOut.getvalue()
    if _code_out != _out:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        sys.stdin = sys.__stdin__
        print('Wrong Answer!')
        print('For the input: input' + str(_i) + ".txt" )
        print('Your code gave output:"' + _code_out + '"')
        print('But the desired output was:"' + _out + '"')
        exit()
    else:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        sys.stdin = sys.__stdin__
        print(_i, 'passed.')
    codeOut.close()
    codeErr.close()

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
sys.stdin = sys.__stdin__

print('Accepted')
print('Your code passed all 299 tests')
