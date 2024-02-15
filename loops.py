"""
for some_varibale in iterable:
    statements
    .
    .
    .
"""
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# string = "i love football"


# def func(st):
#     print(st)


# for i in nums:
#     print(i)

# for i in range(10):
#     print(nums[i])


# fruits = "banana apple orange".split()

# # enum_fruits = list(enumerate(fruits))
# # print(enum_fruits)

# for index, item in enumerate(fruits):
#     print(index, item)

# num = 0
# while num < 20:
#     num = num + 0.01
#     print(num)

websites = ["https://git.com", "www.youtube.com", "real estate"]
for site in websites:
    if site.endswith("com"):
        print(True)
    else:
        print(False)
