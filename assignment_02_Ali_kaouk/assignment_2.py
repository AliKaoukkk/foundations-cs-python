def countDigits(number):
    if (number < 10):
        return 1
    else:
        return 1 + countDigits(number // 10)


def maximumNumber(lst):
    if (len(lst) == 0):
        return 0
    elif (len(lst) == 1):
        return lst[0]
    else:
        total_max = maximumNumber(lst[1:])
        return lst[0] if lst[0] > total_max else total_max


def displayMenu():
    print("1-count digits\n" + "2-Find Max\n" + "3-Exit")
    print('-' * 20)


def mainFunction():
    displayMenu()
    choice = int((input('choose a number')))
    while (choice != 3):
        if (choice == 1):
            number = int((input('enter a number to count digit')))
            max_digits = countDigits(number)
            print('number of digits', max_digits)
        elif (choice == 2):
            lst_1 = (input('choose numbers seperated with spaces'))
            lst_result = list(map(int, lst_1.split()))
            max_number = maximumNumber(lst_result)
            print(max_number)
        else:
            print('invalid input')
        displayMenu()
        choice = int(input('choose a number'))
    print('thanks for using my program')


mainFunction()