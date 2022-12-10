from modules.lists import list_numButtons, list_num_functions,list_Symbols_Button,list_sym_functions
# кнопки цифр
for num in range(10):
    list_numButtons[num].clicked.connect(list_num_functions[num])
# кнопки +, -, *, /
for sym in range(3,7):
    list_Symbols_Button[sym].clicked.connect(list_sym_functions[sym-3])
# кнопка =
list_Symbols_Button[7].clicked.connect(list_sym_functions[4])
#
list_Symbols_Button[0].clicked.connect(list_sym_functions[5])

list_Symbols_Button[1].clicked.connect(list_sym_functions[6])

list_Symbols_Button[2].clicked.connect(list_sym_functions[7])

list_Symbols_Button[-1].clicked.connect(list_sym_functions[8])