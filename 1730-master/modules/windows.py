from PyQt5.QtWidgets import (
        QWidget, 
        QApplication
    )
#

win_width = 300
win_height = 400


app = QApplication([])
#
win = QWidget()
#
# win.resize(300, 400)

win.setStyleSheet(
    '''background-color: rgb(80,80,80);
    '''
)

win.setFixedSize(win_width, win_height)
#
win.setWindowTitle("Calculator")