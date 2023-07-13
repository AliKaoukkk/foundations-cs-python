def digitCount(n):
  if n < 10:
    return 1
  else:
    return 1 + digitCount(n / 10)
def recursiveMax(a):
  if len(a) == 1:
    return a[0]
  else:
    return a[0] if a[0] > recursiveMax(a[1:]) else recursiveMax(a[1:])
def displayMenu():
  print("1-Count Digits\n" + "2-Find Max\n" + "3-Exit")
def mainFunction():
  displayMenu()
  choice = int(input('enter a number'))
  while (choice != 3):
    if (choice == 1):
      n = int(input('enter a number'))
      digitCount(n)
    elif (choice == 2):
      user_input = input('enter a number')
      a = list(map(int, user_input.split()))
      recursiveMax(a)
    else:
      print('invalid input')
  print('thanks for using my program')

mainFunction()