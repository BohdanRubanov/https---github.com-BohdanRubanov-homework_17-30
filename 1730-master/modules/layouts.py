from ctypes import alignment
from modules.lists import list_HLayouts, list_all_button, list_numButtons, list_Symbols_Button
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from modules.labels import label
from PyQt5.QtCore import Qt


main_V = QVBoxLayout() #
# main_V.addStretch(0)
main_V.setSpacing(1)
#
main_V.addWidget(label, alignment = Qt.AlignRight)
#
for line in range(5):
    objectLayouts = QHBoxLayout()
    # objectLayouts.addStretch(1)
    list_HLayouts.append(objectLayouts)

def addToLayout():
    for button in list_all_button:
        #
        index = list_all_button.index(button)
        #
        for button1 in button:
            #
            list_HLayouts[index].addWidget(button1)
    #
    # list_numButtons[0].setContentsMargins(4, 0, 0 ,0)
    #
    list_HLayouts[-1].addWidget(list_numButtons[0])
    list_HLayouts[-1].addWidget(list_Symbols_Button[-1])
    list_HLayouts[-1].addWidget(list_Symbols_Button[-2])
    #
    for el in list_HLayouts:
        #
        main_V.addLayout(el)
    #

    