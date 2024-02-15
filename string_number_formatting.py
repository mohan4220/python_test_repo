"""
formatting strings in python

string formatting:
-> %

-> .format()

-> f strings

username is from user_village, he is of user_age, he likes to play usersport
"""
name = "mohan"
village = "ongole"
age = 28
sport = "cricket"
# greeting = (
#     name
#     + " is from "
#     + village
#     + ", he is of "
#     + str(age)
#     + ", he likes to play "
#     + sport
# )

greeting1 = "%s is from %s, he is of %s, he likes to play %s" % (
    name,
    village,
    age,
    sport,
)
print("youtube")
greeting2 = "{} is from {}, he is of {}, he likes to play {}".format(
    name, village, age, sport
)

greeting3 = "{username} is from {uservillage}, he is of {userage}, he likes to play {usersport}".format(
    username=name, uservillage=village, userage=age, usersport=sport
)

greeting4 = f"{name} is from {village}, he is of {age}, he likes to play {sport}"

print(greeting4)
