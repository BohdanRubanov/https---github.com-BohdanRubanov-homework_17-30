from modules.labels import label
from modules.fonts import font1
from modules.lists import list_input, list_num_functions, list_arithmetics_operations, list_sym_functions
from modules.arithmetic_operations import arithmetic_operation
# from modules.symbol_functions import stop_input
#
number = ""

def get_symbols(symbol):
    global number
    #
    if len(number) != 16:
        if symbol not in list_arithmetics_operations:
            if symbol != "=" and symbol != ",":
                number += str(symbol) #
                label.setText(number) #
    if symbol in list_arithmetics_operations and number != '' and symbol != "+/-":
        list_input.append(number)
        number = ""
        if len(list_input) == 1:
            list_input.append(symbol)
    if symbol == "=" and len(list_input) == 2:
        list_input.append(number)
        number = str(arithmetic_operation())
        label.setText(number)
        #
        if "C" in number:
            number = list_input[0]
        list_input.clear()
    if symbol == "AC":
        list_input.clear()
        number = "_"
        label.setText(number)
        number = ""
    if symbol == "+/-":
        number = int(number)
        number *= -1
        number = str(number)
        label.setText(number)
    if symbol == ",":
        number_for_comma = number
        number += str(symbol) 
        label.setText(number)
        number = number_for_comma
        if symbol not in list_arithmetics_operations and symbol != "=":
            number_for_comma_int = int(number)
            number.split()
            a = 10
            for i in number:
                if i == number[0]:
                    pass
                else:
                    number_for_comma_int += int(i) / a
                    print(number_for_comma_int)
                    a *= 10
            number = str(number_for_comma_int)
            print(number)
            list_input.clear
            list_input.append(number)
            print(list_input)
def add_zero():
    get_symbols(0)
def add_one():
    get_symbols(1)
def add_two():
    get_symbols(2)
def add_three():
    get_symbols(3)
def add_four():
    get_symbols(4)
def add_five():
    get_symbols(5)
def add_six():
    get_symbols(6)
def add_seven():
    get_symbols(7)
def add_eight():
    get_symbols(8)
def add_nine():
    get_symbols(9)
def add_plus():
    get_symbols("+")
def add_minus():
    get_symbols("-")
def add_multiply():
    get_symbols("*")
def add_division():
    get_symbols("/")
def add_equals():
    get_symbols("=")
def add_AC():
    get_symbols("AC")
def add_plus_minus():
    get_symbols("+/-")
def add_percent():
    get_symbols( "%")
def add_comma():
    get_symbols( ",")
#   
list_sym_functions.append(add_division)
list_sym_functions.append(add_multiply)
list_sym_functions.append(add_minus)
list_sym_functions.append(add_plus)
list_sym_functions.append(add_equals)
list_sym_functions.append(add_AC)
list_sym_functions.append(add_plus_minus)
list_sym_functions.append(add_percent)
list_sym_functions.append(add_comma)
#
list_num_functions.append(add_zero)
list_num_functions.append(add_one)
list_num_functions.append(add_two)
list_num_functions.append(add_three)
list_num_functions.append(add_four)
list_num_functions.append(add_five)
list_num_functions.append(add_six)
list_num_functions.append(add_seven)
list_num_functions.append(add_eight)
list_num_functions.append(add_nine)

