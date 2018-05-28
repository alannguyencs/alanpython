


def num2String(number):
    number = str(number)
    while(len(number) < 6):
        number = "0" + number
    return number