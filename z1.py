def parsing_number(number):
    hundreds = int(number/100)
    dozens = int(number % 100/10)
    one = int(number % 100 % 10)
    dictionary = {
        'h': hundreds,
        'd': dozens,
        'o': one
    }
    return dictionary


def print_hundreds(number):
    strings = {
        '1': "one hundred ",
        '2': "two hundreds ",
        '3': "three hundreds ",
        '4': "four hundreds ",
        '5': "five hundreds ",
        '6': "six hundreds ",
        '7': "seven hundreds ",
        '8': "eight hundreds ",
        '9': "nine hundreds "
    }
    return strings[str(number)]


def print_dozens(number):
    strings = {
        '2': "twenty ",
        '3': "thirty ",
        '4': "fourty ",
        '5': "fifty ",
        '6': "sixty ",
        '7': "seventy ",
        '8': "eighty ",
        '9': "ninety "
    }
    return strings[str(number)]


def print_one(number):
    strings = {
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine"
    }
    try:
        return strings[str(number)]
    except KeyError as e:
        return -1


def print_dozens_w8_numbers(number):
    strings = {
        '10': "ten",
        '11': "eleven",
        '12': "twelve",
        '13': "thirteen",
        '14': "fourteen",
        '15': "fifteen",
        '16': "sixteen",
        '17': "seventeen",
        '18': "eighteen",
        '19': "nineteen"
    }
    return strings[str(number)]


def main():
    while (True):
        number = int(input())
        if (number == 0):
            print("zero")
            continue
        if (number > 9 and number < 20):
            print(print_dozens_w8_numbers(number))
            continue
        string = ""
        if (number > -1 and number < 1000):
            # h - hundreds, d - dozens, o - one
            number = parsing_number(number)
        else:
            continue
        if (number['h'] != 0):
            string += print_hundreds(number['h'])
        if (number['d'] > 1):
            string += print_dozens(number['d'])
        if (print_one(number['o']) != -1):
            string += print_one(number['o'])
        print(string)


if __name__ == "__main__":
    main()
