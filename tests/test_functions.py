# Test that functions are properly decoded
from pybyte2ast.decode import decode_function

def func_test_one_line(x):
    return x + 1

def test_func():
    r = decode_function(func_test_one_line)
    assert str(r) == 'add(x,1)'
