number = int(input("How many?: "))


def fibonacci(x):
    fib = [1, 1]
    i = 1

    if x == 1:
        return fib[0]
    elif x == 2:
        return fib
    else:

        while i < (x - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
        return fib


print(fibonacci(number))
