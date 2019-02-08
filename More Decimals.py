lst = [0.1, 0.2, 0.3]


def more_decimals(data: list):

    l2 = []

    for number in data:
        for i in range(10):
            decimal = float(format(i / 100, '.2f'))
            l2.append(float(format(number + decimal, '.2f')))

    l2.append(l2[-1] + 0.01)
    return l2
