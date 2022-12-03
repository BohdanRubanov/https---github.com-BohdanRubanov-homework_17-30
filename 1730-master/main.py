import time
from modules.windows import *
from modules.lists import *
from modules.number_functions import *
# from modules.symbol_functions import *
from modules.layouts import *
from modules.buttons import *
from modules.clicked_connect import *
from modules.settings_button import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

#
add_buttons()
#
addToLayout()
#
win.setLayout(main_V)    
#
customize_buttons()

win.show()
#
app.exec_()





