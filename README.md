# pybyte2ast

Translate python byte-code into an AST.

## Examples

As no code is yet written, the examples below are aspirational.

    def func(x):
        return x + 1

    import pybyte2ast
    print (pybyte2ast.decode(func))
    # 'add(x, 1)'

## Python Version Information

The Python bytecode is an 'implementation detail' of CPython. As a result, it can change arbitrarily from version to version. This has been tested on a range of python versions:

    3.7.1

By tested we mean the test cases found in the `tests` directory all pass.

## Acknowledgments

This work has been supported in part by XXX IRIS-HEP XXX.