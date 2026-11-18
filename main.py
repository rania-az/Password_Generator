
import random
import string

print(" PASSWORD GENERATOR ")

length = int(input("How many characters should the password have? "))

if length <= 0:
    print("Error! Password length must be positive.")

else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nYour password is:", password)
