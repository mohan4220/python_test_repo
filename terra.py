"""
List -> collection of data of same or different datatypes
    mutable -> can be modified after creation
    each item has an address called index
    some methods that can be used to perform some operation on its data

    .append()  |
    .insert()  | to add data to a list
    .extend()  |

    .pop()      |
    .remove()   | to remove data

    .index()    | to find the index of an element in the list

    ====================================
    id() -> gives you the address of the object in memory

    copy -> shallow and deep copy
"""

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums2 = nums.copy()  # --> creates a new list with same elements

# print(nums, id(nums))
# print(nums2, id(nums2))

# nums2[9] = 22

# print(nums)
# print(nums2)
# "== is" # == --> evaluates values , is --> checks if the two variables points to or looking at same object in memory
# num1 = [1, 2]
# num2 = [1, 2]

# print(id(num1), id(num2))
# print(num2 is num1)

"""
Loops -> for loop and while loop

for condition:
    statements
    .
    .
    .

range(start, end, step)

"""
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for index in range(len(nums)):  # range(10) -> [0,1,2,3,4,5,6,7,8,9]
#     nums[index] = nums[index] * 2

# print(nums)

# elems = []
# total = 0
# for index in range(5):
#     num = int(input("enter number: "))
#     elems.append(num)

# # for index in range(5):
# #     total = total + elems[index]

# total = min(elems)
# print(total)

# total = 0
# for index in range(5):
#     total = total + int(input("enter number: "))
# print(total)

# elems = []
# max = 0
# for num in range(5):
#     elems.append(int(input()))

# for num in range(5):
#     print(max, elems[num])
#     inp_num = int(input())
#     if elems[num] > max:
#         max = elems[num]


# print(max)


# fruits = ["apple", "banana", "orange", "apple", "apple"]
# print(fruits.count("banana"))

"""
list revise
remove()
extend()

== vs is

for loop
range()

list.count()

how to find maximum value in a list using for loop
"""
num1 = [1, 2, 3, 4, 5]

result = []

# find the pairs of numbers in both lists where the sum is greater than 6

for i in num1:
    for j in num1:
        if i + j > 6:
            result.append([i, j])

print(result)
