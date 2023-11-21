#Guessing game
# secret_word = "clarity"
# guess = ""
# cnt = 0
# while guess != secret_word:
#     if cnt == 3:
#         print("You lost")
#         break
#     else:
#         guess = input("Enter your guess: ")
#         if(guess != secret_word and cnt < 3):
#             cnt += 1
#             print("No u wrong")
#             if cnt < 3: print("Try again")
#         else:
#             print("You won!")
#             break

# for letter in "Hust Student":
#     print(letter)

# friends = ["Jone", "Yasui", "Henry"]
# for fr in friends:
#     print(fr)

# for i in range(len(friends)): #not including 10
#     print(friends[i]) 

# def raise_to_power(base_num, pow_num):
#     res = 1
#     for i in range(pow_num):
#         res = res * base_num
#     return res
# base = input("Input base number: ")
# power = input("Input pow number: ")

# print("Result is: " + str(raise_to_power(int(base), int(power))))

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# print(number_grid[0][2])

# for row in number_grid:
#     for col in row:
#         print(col)

# change vowels into letter "g"
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aiueo":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a word: ")))

# try:
#     # value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)