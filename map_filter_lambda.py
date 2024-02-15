"""
lambda functions/ anonymous functions --> nameless, defined on the spot
map
filter

map(function, iterable)

filter(criteria_function, iterable)
"""


# def foo(x):
#     return int(x)


# greeter = lambda a: f"hello {a}"

# arr = input().split()

# arr = list(map(int, arr))

# for i in range(len(arr)):
#     arr[i] = int(arr[i])

# print(arr)


# def isEven(a):
#     return a % 2 == 0


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums = list(filter(lambda a: a % 2 != 0, nums))

# print(nums)

# fruits = ["apple", "banana", "grapes", "orange", "mango"]

# food_items = ["cucumber", "apple", "carrot", "beetroot", "mango", "banana"]

# result = list(filter(lambda item: item in fruits, food_items))

# print(result)

# from functools import reduce

# nums = [1, 2, 3, 4, 5]
# result = reduce(lambda a, b: a + b, nums)
# print(result)

"""
os module -> contains all the operations/commands related to operating system
"""
import os

# list all the python files in a directory
files = os.listdir("./")
result = []
# for file in files:
#     if file.endswith('.py'):
#         result.append(file)
result = list(filter(lambda file: file.endswith(".py"), files))
print(result)
