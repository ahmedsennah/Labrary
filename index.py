from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import MySQLdb



MainUI, _ = loadUiType('main.ui')


class Main(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Db_Connect()
        self.Handel_Bouttons()
        self.UI_Changes()
        self.Open_Daily_Movment_Tab()
        self.Show_all_Category()






    def UI_Changes(self):
        ## UI  Change In loginpip اي تفيير فى اللود
        self.tabWidget.tabBar().setVisible(False)

    def Db_Connect(self):
        ## Database Connection
        self.db = MySQLdb.Connect(host='localhost',user='root', password='112233sa',
                                db='library')
        self.cur = self.db.cursor()
        #print('connection Accpeted')



    def Handel_Bouttons(self):
        ## Handel Button
        self.CmdToday.clicked.connect(self.Open_Daily_Movment_Tab)
        self.CmdBook.clicked.connect(self.Open_Book_Tab)
        self.CmdClient.clicked.connect(self.Open_Client_Tab)
        self.CmdDashBoard.clicked.connect(self.Open_DashBordTab)
        self.CmdHistory.clicked.connect(self.Open_History_Tab)
        self.CmdReport.clicked.connect(self.Open_Report_Tab)
        self.CmdSetting.clicked.connect(self.Open_Setting_Tab)

        self.CmdAddBook.clicked.connect(self.Handel_Today_Work)
        self.CmdAddBranch.clicked.connect(self.Add_Branch)
        self.CmdAddPuplisher.clicked.connect(self.Add_Puplisher)
        self.CmdAddAuthar.clicked.connect(self.Add_Author)
        self.CmdAddctegory.clicked.connect(self.Add_Category)





        


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
## Clients
#########################################
    def show_All_Clients(self):
        ## Show All Clients
        pass

    def Add_New_Clients(self):
        ## Add New Clients
        pass

    def Edit_Clients(self):
        ## Edit Clients
        pass


    def Delete_Clients(self):
        ## Delete Clients from DB
        pass

###############################################
## History
#########################################

    def Show_Hisrory(self):
        ## Show History
        pass

###############################################
## Report
#########################################    
    def All_Books_Report(self):
        ## All Books Report
        pass

    def Books_Filter_report(self):
        ## books Show With Filter
        pass

    def Book_Export_Report(self):
        ## Export Books Data To Excel file
        pass

    def All_Client_Report(self):
        ## All Client Report
        pass

    def Client_Filter_report(self):
        ## Client Show With Filter
        pass

    def Client_Export_Report(self):
        ## Export Client Data To Excel file
        pass
#########################################
## Monthly Report
########################################
    def Monthly_Report(self):
        ## Show Monthly Report
        pass

    def Monthly_Report_Export(self):
        ## Monthly Report Export To Excel file
        pass

#########################################
## Setting
########################################
    def Add_Branch(self):
        ## Add New Branch
        Branch_Name = self.TXTBranchName.text()
        Banch_Code = self.TXTBranchCode.text()
        Branch_Location = self.TXTBranchLocation.text()
        self.cur.execute(''' 
        INSERT INTO branch
        (name , code , Location)
        VALUES(%s, %s, %s)
        ''',(Branch_Name, Banch_Code, Branch_Location))
        self.db.commit()
        print('add sucsessfuly')

    
    def Add_Category(self):
        ## Add Category
        Category_Name = self.TXTCategoryName.text()
        Pearint_Category = 1
        self.cur.execute('''
        INSERT INTO category
        (Category_name , parent_Category)
        VALUES(%s, %s)
        ''', (Category_Name, Pearint_Category))
        self.db.commit()
        self.Show_all_Category(
        )

    def Add_Puplisher(self):
        ## Add Puplisher
        Puplisher_Name = self.TXTpuplisherName.text()
        Puplisher_Location = self.TXTpuplisherLocation.text()
        self.cur.execute('''
        INSERT INTO puplisher
        (name, location)
        VALUES(%s, %s)
        ''', (Puplisher_Name, Puplisher_Location))
        self.db.commit()
    
    def Add_Author(self):
        ## Add Author
        Author_Name = self.TXTAuthorName.text()
        Author_Location = self.TXTAuthorLocation.text()
        self.cur.execute('''
        INSERT INTO author
        (name , location)
        VALUES(%s, %s)
        ''', (Author_Name, Author_Location))
        self.db.commit()


    def Show_all_Category(self):
        self.comboBox_Category.clear()
        self.cur.execute('''
        SELECT Category_name  FROM category
        ''')

        categores = self.cur.fetchall()
        
        for category in categores :
            self.comboBox_Category.addItem(str(category[0]))

 








#########################################
## Employee Users User
########################################

    def Add_Employee(self):
        ## Add User
        pass

    def Edit_Employee_Data(self):
        ## Edit Employee Data
        pass
    
#########################################
## Employee Users User Permissons
########################################
    
    def Add_Employee_permissions(self):
        ## Add User permissions
        pass

    def Admin_Report(self):
        ## Send Report To  Admin 
        pass


    ###############################
    ##############################

    def Open_Login_Tab(self):
        self.tabWidget.setCurrentIndex(0)


    def Open_ResetPassword_Tab(self):
        self.tabWidget.setCurrentIndex (1)


    def Open_Daily_Movment_Tab(self):
        self.tabWidget.setCurrentIndex (2)
    
    def Open_Book_Tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
    
    def Open_Client_Tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)

    def Open_DashBordTab(self):
        self.tabWidget.setCurrentIndex(5)
    
    def Open_History_Tab(self):
        self.tabWidget.setCurrentIndex(6)

    def Open_Report_Tab(self):
        self.tabWidget.setCurrentIndex(7)
        self.tabWidget_5.setCurrentIndex(0)
    
    def Open_Setting_Tab(self):
        self.tabWidget.setCurrentIndex(8)
        self.tabWidget_4.setCurrentIndex(0)












def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()








