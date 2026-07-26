import random
import string

print("===================================")
print(" Secure Random Password Generator ")
print("===================================")

length = int(input("Enter password length (minimum 4): "))

if length < 4:
    print("Password length should be at least 4.")
else:

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = ""

    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    for i in range(length - 4):
        remaining += random.choice(all_characters)

    password_list = list(
        uppercase + lowercase + digit + special + remaining
    )

    random.shuffle(password_list)

    password = "".join(password_list)

    print("\nGenerated Password:")
    print(password)