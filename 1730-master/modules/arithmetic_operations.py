from modules.lists import list_input
from modules.labels import label

def arithmetic_operation():
    if list_input[1] == "+":
        number = int(list_input[0]) + int(list_input[2])
    elif list_input[1] == "-":
        number = int(list_input[0]) - int(list_input[2])
    elif list_input[1] == "*":
        number = int(list_input[0]) * int(list_input[2])
    elif list_input[1] == "%":
        number = int(list_input[0]) * 0.01 * int(list_input[2])
    elif list_input[1] == "/":
        try:
            number = int(list_input[0]) / int(list_input[2])   
        except:
            number = "Can`t divide by zero"
    return number   

def percent_operation():
    number = int(list_input[0]) /100
    return number   