from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import os,time,pafy,sys


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Download")

        self.setWindowTitle("AUDIO DOWNLOAD")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.additem)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Enter URL")
        self.pbar=QProgressBar()
        self.pbar.setGeometry(30,40,200,25)

        layout.addWidget(self.nameinput)
        layout.addWidget(self.pbar)
        

       
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def additem(self):
        try :
            url =""
            url = self.nameinput.text()
            result=pafy.new(url)
            best_quality_audio = result.getbestaudio()
            print(best_quality_audio)
            self.pbar.setValue(best_quality_audio.download())

        except:
            print("NO URL")

        
    	
        



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("Password Generator")

        self.setMinimumSize(800, 600)

        adduser_action = QAction(QIcon("icon/add.png"),"New Generate", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)

    def insert(self):
            dlg = InsertDialog()
            dlg.exec_()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
