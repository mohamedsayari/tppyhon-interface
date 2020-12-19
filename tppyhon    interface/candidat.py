import sys
import mysql.connector

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from untitled import *

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
        sql = "INSERT INTO `candidat`( `nom`, `prenom`, `tel`, `niveau`) VALUES (%s, %s,%s,%s)"
        val = (self.ui.n.text(),self.ui.p.text(),self.ui.t.text(),str(self.ui.n_2.currentText()))
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
        mycursor.execute("SELECT * FROM candidat")
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
        self.ui.n.setText('')  
        self.ui.p.setText('')  
        self.ui.t.setText('')    
      

    
        

            
        
if __name__=="__main__":   

    app = QApplication(sys.argv)

    w = User()

    w.show()

    sys.exit(app.exec_())
    
