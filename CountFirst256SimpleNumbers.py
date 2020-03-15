'''Задание #2 на собеседование в AngelsIT. Вывести 256-ое простое число из диапазона от 1000 до 10000.'''


def main():
    counter = 0
    for number in range (1000,10000):
        if(isSimpleNumber(number) == True):
            counter += 1
        if (counter == 256):
            print ('256: ',number)
            break


def isSimpleNumber(number):
    for divisor in range(2,int(pow(number,0.5))+1):
            if (number % divisor == 0):
                return False
    return True


if __name__ == "__main__":
    main()