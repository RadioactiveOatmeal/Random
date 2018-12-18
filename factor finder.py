number = int(input("Enter a positive number: "))

numbers = []
highest_number = number + 1
factors = []

# add numbers lower than inputted number to list 'numbers'
for i in range(1, highest_number):
    numbers.append(i)

# print every number from list 'numbers' that is a factor of inputted number
for num in numbers:
    if number % num == 0:
        factors.append(num)

if len(factors) == 2:
    print("Prime number - "
          "Factors: {}".format(factors))

elif len(factors) > 2:
    factors.remove(1)
    print("Not prime - "
          "Factors: {}".format(factors))

else:
    print("1 is not a prime number, as prime numbers should "
          "be divisible by 2 positive integers")
