import string
import random


def generate_pass(num):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    punctuation = string.punctuation

    password = ''

    for i in range(num):
        temp = random.randint(1,4)

        if temp == 1:
            password += random.choice(lowercase)

        elif temp == 2:
            password += random.choice(uppercase)

        elif temp == 3:
            password += random.choice(numbers)

        else:
            password += random.choice(punctuation)

    return "Your password is {}".format(password)


num_char = int(input("Password length: "))
print(generate_pass(num_char))
