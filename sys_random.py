"""
sys -> it contains variables and functions related to out python environment
"""
# import sys

# print(sys.version)

# print(sys.path)

# print(sys.executable)

# print(sys.platform)

# print(sys.argv)  # first element is always your current file,

"""
random -> it generates pseudo random numbers and sequences
random() -> generates random numbers between 0 and 1
randint() -> generates integer values between two given numbers
randrange() -> same as randint but with step
choice() -> returns a random element from a array
shuffle() -> shuffles a list randomly
sample() -> returns a sample list of elements from a bigger list
"""
import random

nums = list(range(0, 1000))

print(random.sample(nums, 5))
print(random.sample(nums, 2))
print(random.sample(nums, 10))
