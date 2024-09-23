import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['!', '#', '$', '%', '&', '*', '(', ')', '/', '?', '>', '<']
print("Generate your password here!")
max_charc = int(input("How many characters do you want to generate?\n"))
num_of_alph = int(max_charc/2)
num_of_num = int(max_charc/4)
num_of_chac = int(max_charc/4)

password = []
for char in range(1, num_of_alph + 1) :
    password += random.choice(alphabet)

for char in range(1, num_of_num + 1) :
    password += random.choice(number)   

for char in range(1, num_of_chac + 1) :
    password += random.choice(characters)
random.shuffle(password)

password_ = ""
for char in password:
    password_ += char
print(f"Your password is {password_}")