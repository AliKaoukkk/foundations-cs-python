import json
def sumTuples(tpl_1, tpl_2):
  if (len(tpl_1) != (len(tpl_2))):
    raise ValueError ('length of tuples are not the same')
  else:
    result = zip(tpl_1, tpl_2)
    final_result = tuple(map(sum,result))
    return final_result

def dictJson(dictionary, filename):
    with open(filename, 'w') as file:
        file.write("{\n")
        for key, value in dictionary.items():
            file.write('  "{}": '.format(key))
            if isinstance(value, (str, int, float)):
                file.write(json.dumps(value))
            else:
                file.write(json.dumps(value, indent=2))
            file.write(',\n')
        file.write("}\n")

def readJson(filename):
    with open(filename, 'r') as file:
        data = file.read()
    dictionary = eval(data)
    if not isinstance(dictionary, dict):
        raise TypeError("Invalid JSON file")
    return dictionary



def mainMenu():
  print(" 1.Sum Tuples:\n", "2.import Json:\n", "3.Export Json:\n", "4.Exit:")
  print("-" *20)

def mainFunction():
  mainMenu()
  choice = int(input('enter a choice: '))
  while (choice != 4):
      if (choice == 1):
        tpl_1 = tuple(map(int, input('enter a tuple').split()))
        tpl_2 = tuple(map(int, input('enter a tuple').split()))
        result_1 = sumTuples(tpl_1, tpl_2)
        print(result_1)
        mainMenu()
        choice = int(input('enter a choice: '))
      elif (choice == 2):
        dictionary = eval(input("Enter the dictionary: "))
        filename = input("Enter the filename: ")
        print('file created', dictJson(dictionary, filename))
        mainMenu()
        choice = int(input('enter a choice: '))
      elif (choice == 3):
        filename = input("Enter the JSON filename: ")
        result = readJson(filename)
        print("List of dictionaries:", result)
        mainMenu()
        choice = int(input('enter a choice: '))
      else:
        print('invalid input')
  print('thanks for using my rpogram you exited')

mainFunction()