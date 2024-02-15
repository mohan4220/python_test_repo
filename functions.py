"""
a block of code that has a specific purpose or perform a specific operation
def function_name(arguments):
    statements
    .
    .
    .
    return some_value

"""

sentence = "I am from mars"
sentence2 = "he is a wild cat"
sentence3 = "doreamon is a good friend of nobitha"

# function without arguments and retun
# def space_remover():
#     print("space remover function")


# def func1(words):
#     print("the sentence is", words)


# func1(sentence)
# func1(sentence2)
# func1(sentence3)


# function with two arguments and return
# def adder(a, b):
#     total = a + b
#     return total


# num1, num2 = 34, 45

# adder_output = adder(num1, num2)

# print(adder_output)


# =================================================================================
# pass by reference
def list_adder(lt):
    for i in range(len(lt)):
        lt[i] = lt[i] + 2
    print("inside list adder", lt)


nums = [1, 2, 3, 4]

# print(nums)

# list_adder(nums)
# list_adder([4, 5, 6, 7, 8])

# print("outside list added", nums)

# ===================================================================================
# pass by value
num = 3


# def adder(a):
#     a = a + 2
#     print("inside added", a)


# print(num)

# adder(num)

# print("outside added", num)

# ====================================================================================
# keyword arguments/ default arguments


def incrementer(a, inc=0):
    return a + inc


def incrementer2(a, inc1=0, inc2=1):
    return a + inc1 + inc2


# output = incrementer(2, inc=3)
# print(output)
# output = incrementer2(2, 10, 5)
# output = incrementer2(2, inc2=5, inc1=10)
# print(output)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def operation_performer(a, b, operation=add):
    return operation(a, b)


# print(operation_performer(2, 3))

"""
variable number of arguments 
*args -> varibale number of positional arguments
**kwargs -> varibale number of keyword arguments
"""


def adder(*nums):
    return sum(nums)


# print(adder(num1=1, num2=2))
# print(adder(num1=1, num2=2, num3=3))
# print(adder(2, 3, 4, 2, 3, 5, 6, 78, 9, 0))

# returning multiple values


# def operations(a, b):  # add, sub, mul
#     return a + b, a - b, a * b


# c, d, e = operations(2, 3)

# print(c, d, e)


"""
defining/ creating functions
types of functions, with and without arguments and return
positional and keyword/default arguments
dynamic number of arguments
returning multiple values.
callback - passing function as arguments to other functions
"""

# swapping a ,b
# a = 5
# b = 10
# swapping using a third variable
# temp = a
# a = b
# b = temp

# swapping without a third variable -> swapping in place -> without using extra memory space
# b = a + b  # 15
# a = b - a  # 10
# b = b - a  # 5
# a, b = b, a

# print(a, b)
"""
b = ""
n = len()
for i in range(n)

using slicing and negative indexing
a = a[::-1]
"""
a = "apple"
# a = list(a)
# a.reverse()
# a = "".join(a)

pi = 3.14


def display():
    print(__name__)
    print(__file__)


if __name__ == "__main__":
    display()
    print(a)
