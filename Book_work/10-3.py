# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

user_input = input("please type your name: ")

filename = "guest.txt"

with open(filename, 'w') as file_object:
    file_object.write(user_input)

