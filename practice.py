"""
1. Factorial Finder: Calculate the factorial of a given number (e.g., 5! = 120).
n=3, 3 * 2* 1 = 6
n=5, 5*4*3*2*1 = 120

n, n*(n-1)*(n-2)*...*2*1
"""
# n = int(input("enter a number: "))
# factorial = 1
# for loop
# for num in range(1, n + 1):
#     factorial = num * factorial

# while loop
# num = 1
# while num <= n:
#     print(num, factorial)
#     factorial = num * factorial
#     num = num + 1

# print("factorial is:", factorial)

"""
2. Vending Machine Simulator: Simulate a simple vending machine that accepts money, dispenses items, and gives change.
requirements -> 
list of products, price, quantity | each product's id is its index
inputs -> cash, what product
outputs -> if quantity available, product dispense, change | product not available, "not available", our cash
"""
# [ name, price, quantity]
products = [
    ["thumps up", 40, 10],
    ["sprite", 40, 10],
    ["limca", 20, 10],
    ["lays", 5, 0],
    ["cheetos", 10, 10],
]

for id, item in enumerate(products):
    print(id, item[0:2])

cash = int(input("\nInsert cash: "))
prod_id = int(input("\nselect a product id: "))

name, price, quantity = products[prod_id]

if quantity > 0:
    if cash >= price:
        print(name, cash - price)
        products[prod_id][2] -= 1
    else:
        print("Not enough money", cash)
else:
    print("Not Available", cash)


for id, item in enumerate(products):
    print(id, item)
