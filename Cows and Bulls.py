import random

print("Cows and bulls\n"
      "--------------")

rand = str(random.randint(1000, 9999))

guess = 0

while True:

    choice = str(input("Enter a Number: "))

    bulls, cows = 0, 0

    for char in range(4):
        if rand[char] == choice[char]:
            cows += 1
        elif choice[char] in rand and rand[char] == choice[char]:
            bulls += 1

    if cows == 4:
        break

    guess += 1

    print("{} cows : {} bulls".format(cows, bulls))


if guess == 0:
    print("First try! number: {}".format(rand))
else:
    print("Correct in {} guesses! number: {}".format(guess, rand))
