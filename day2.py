# phrase = "HUST Lmao"
# print(phrase.lower().islower())
# print(phrase[0])
# print(phrase.index("ST"))
# print(phrase.replace("HUST", "lllmao"))
# from math import *
# print(max(-4, -3))
# print(round(3.8754))
# print(floor(3.8754)) #floor là làm tròn xuống, ceil là làm tròn lên

# name = input("Enter your name: ")
# print("Hello " + name + "!")

# color = input("Enter color: ")
# plural_noun = input("Enter a plural noun: ")
# celeb = input("Enter a celeb: ")

# print("Roses are "+ color)
# print(plural_noun + " are blue")
# print("I love " + celeb)

# lucky_numbers = [4, 5, 2, 6, 8, 1, 76]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Naru"]
# friends[1] = "Mike"
# friends.extend(lucky_numbers)
# friends.append("Creep")
# friends.insert(1, "Kelly")
# friends.remove("Jim")
# friends.pop()
# print(friends)
# lucky_numbers.sort()
# friends2 = friends.copy()
# print(lucky_numbers)
# print(friends2)

#tuple's elements cannot be modified, be added or be erased
# coordinates = (4, 5)
# print(coordinates[1])

# def sayhi(name):
#     print("Hello User " + name)

# sayhi("Mike")

# def cube(num):
#     return num*num*num
# num = input("Enter a number: ")
# result = cube(int(num))
# print(result)

is_male = True
is_tall = False
#and/or
if is_male and is_tall:
    print("You're a man or tall or both")
elif is_male and not(is_tall):
    print("You're a short man")
else:
    print("Coffee")