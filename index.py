from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

import sys

MainUI, _ = loadUiType('main.ui')


class Main(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


    def UI_Changes(self):
        ## UI  Change In login اي تفيير فى اللود
        pass

    def Db_Connect(self):
        ## Database Connection
        pass


    def Handel_Bouttons(self):
        ## Handel Button
        pass

    def Handel_Login(self):
        ##Handel Login
        pass

    def Handel_ResetPassword(self):
        ## Handel Reset Password
        pass


    def Handel_Today_Work(self):
        ## Handel Today Work Operation
        pass
    #########################################
    ###Books
    #########################################
    def show_All_Books(self):
        ## Show All Books
        pass

    def Add_New_Books(self):
        ## Add New Books
        pass

    def Edit_Books(self):
        ## Edit Books
        pass


    def Delete_Books(self):
        ## Delete Books
        pass

###############################################
## Cliens
#########################################
    def show_All_Cleins(self):
        ## Show All Books
        pass

    def Add_New_Books(self):
        ## Add New Books
        pass

    def Edit_Books(self):
        ## Edit Books
        pass


    def Delete_Books(self):
        ## Delete Books
        pass

###############################################

    
















def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()








