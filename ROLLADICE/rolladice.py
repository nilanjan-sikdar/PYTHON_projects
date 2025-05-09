# import random
# print("welcome")
# while True:
#     bol = input("enter (y/n): ")
#     if bol == "y":
#         randomnumber1 = random.randint(1,6)
#         randomnumber2 = random.randint(1,6)
#         print(randomnumber1,randomnumber2)
#     elif bol == "n":
#         break;
#     elif bol != "n" or bol != "y":
#         print("invalid input")

import random
while True:
    print("welcome to a rock paper scissor game: ")
    bol=input("play")
    items=["rock","paper","scissor"]
    random.shuffle(items)
    print("combot",items[0])
    if bol=="end":
        break

