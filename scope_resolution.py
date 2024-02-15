"""
Scope resolution: The part or area of a our code, where a variable is valid, is called its scope.

local
enclosed
global
builtin
"""


def adder():
    num1 = 34
    print(num1)


adder()
print(num1)
