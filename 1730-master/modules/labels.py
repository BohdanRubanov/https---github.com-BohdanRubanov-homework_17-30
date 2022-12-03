from PyQt5.QtWidgets import QLabel
from modules.fonts import font1
#
label = QLabel("_")
#
label.setFont(font1)
label.setStyleSheet('''
    color: rgb(255,255,255);
''')