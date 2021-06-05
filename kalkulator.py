print("....:::::CALCULATOR::::....")


def menu():
    print("::MENU::\n")
    print("1 - addition\n")
    print("2 - subtraction\n")
    print("3 - multiplication\n")
    print("4 - division\n") 
    print("5 - integer division\n")
    print("6 - exponentiation\n")
    print("7 - end\n")
    print("0 - menu\n")
info = 'Error: "{0}" is not a valid value!'  


def get_number(prompt='give me a number ', parse=float):
    while True:
        try:
            out = parse(input(prompt))
        except ValueError:
            print (info.format(out))
        else:
            return out
first = " The first number:  "   
second = " The second number:  "


def addition():
    addition = get_number(first, float) + get_number(second, float)
    return addition   


def subtraction():
    subtraction = get_number(first, float) - get_number(second, float)
    return subtraction


def multiplication():
    multiplication = get_number(first, float) * get_number(second, float)
    return multiplication


def division():
    division = get_number(first, float) / get_number(second, float)
    return division 


def integer_division():
    integer_division = get_number(first, int) / get_number(second, int)
    return integer_division


def exponentiation():
    exponentiation = get_number(first, float) ** get_number(second, float)
    return exponentiation


def error():
    return 'Error'


def end():
    return 'end'
print (menu())
operation = input("What will you choose ? ") 
functions = {'1': addition, 
             '2': subtraction, 
             '3': multiplication, 
             '4': division, 
             '5': integer_division, 
             '6': exponentiation,
             '7': end, 
             '0': menu}
function_names = {'1': 'addition', 
                  '2': 'subtraction', 
                  '3': 'multiplication', 
                  '4': 'division', 
                  '5': 'integer division', 
                  '6': 'exponentiation',
                  '7': 'end', 
                  '0': 'menu'} 

while operation != "7":
    function = functions.get(operation, error)
    selected_function = function_names.get(operation, error)
    text = ":::You chose {name}::::\n The result is: {result}" 
    print(text.format(name=selected_function, result=function()))
    operation = input("What will you choose ? ") 