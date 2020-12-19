import sys
import mysql.connector

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from gestionse import *

class User(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)
        self.resr()
        self.ui.aj.clicked.connect(self.add)
        self.show()
    def add(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="tppyhton"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO `session`(`formation`, `description`, `duree`, `prix`)  VALUES (%s, %s,%s,%s)"
        val = (self.ui.f.text(),self.ui.d.text(),self.ui.du.text(),self.ui.p.text())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        self.resr()
        self.Vider()
    def resr(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="tppyhton"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM session")
        myresult = mycursor.fetchall()
       
        self.ui.res.setRowCount(len(myresult)) ##set number of rows
        
        self.ui.res.setColumnCount(5)
        i=0 ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns
        for x in myresult:
            print(x[0])
            self.ui.res.setItem(i,0, QTableWidgetItem(x[0]))
            self.ui.res.setItem(i,1, QTableWidgetItem(x[1]))
            self.ui.res.setItem(i,2, QTableWidgetItem(x[2]))
            self.ui.res.setItem(i,3, QTableWidgetItem(x[3]))
            self.ui.res.setItem(i,4, QTableWidgetItem(x[4]))

            i+=1

    def Vider(self):
        self.ui.f.setText('')  
        self.ui.d.setText('')  
        self.ui.du.setText('')    
        self.ui.p.setText('')
      

    
        

            
        
if __name__=="__main__":   

    app = QApplication(sys.argv)

    w = User()

    w.show()

    sys.exit(app.exec_())
    
