
import  sys
import PyQt5.QtWidgets
import PyQt5
from PyQt5.QtWidgets import  QApplication, QMainWindow, QWidget,QLabel, QDoubleSpinBox, QPushButton,QGridLayout,QListView,QTextEdit,QLineEdit,QMessageBox,QListWidget
import ModelView

class profil(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.btnOK = QPushButton("OK")
        self.btnCansel = QPushButton("Отмена")
        self.box = QGridLayout(self)
        self.name = QLineEdit("Имя Пользователя")
        self.password = QLineEdit()

        self.GUI()
        self._initSignals()

    def GUI(self):
        self.btnOK= QPushButton("OK")
        self.btnCansel=QPushButton("Отмена")

        self.password.setEchoMode(QLineEdit.Password)
        self.box.addWidget(self.btnOK,0,0)
        self.box.addWidget(self.btnCansel,1,0)
        self.box.addWidget(self.name,0,1)
        self.box.addWidget(self.password,1,1)

        self.setLayout(self.box)

    def _initSignals(self):
        self.btnOK.clicked.connect(self.Onclick_conn)
        self.btnCansel.clicked.connect(self.Onclic_cansel)
    def Onclic_cansel(self):
        self.hide()

    def Onclick_conn(self):
        if self.name.text() is None or self.password.text() is None or self.name.text()!="Имя Пользователя" :
            ModelView.ModelView.auntification(self.name.text(),self.password.text())

            self.close()
        else:
            p=QMessageBox()
            p.setText("Введите имя и пароль")
            p.exec_()




class Windows (QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self._increment = True
        self.labelmsg=QLabel("Собщение:")
        self.msg = QLineEdit()
        self.btnCancel = QPushButton('Cansel')
        self.btnPUSH = QPushButton('PUSH')


        self.a=QTextEdit("ответы сервера:")
        self.GUI()
        # self.listview = QListView()
        self._initSignals()




    def GUI(self):
        # self.resize(400,300)
        # self.setMinimumSize(300, 200)
        # self.setMaximumSize(600, 400)

        label = QLabel("""Twised Client плохая паралейность, Twised написан на питоне 2,6 и С
кучу всяких проблем. есть 3 способа попасть в основной поток реактора
использование потоков, планирование, и Использование процессов
 Все эти процесс позволяют попасть в поток после его запуска. 
 Использование процессов не работает Windows(не во всех протоколах! ).
Планирование процесс выполняться с отрочкой , после начала выполнения основного потока.
Использование потоков. (я использую потоки)
 
  
"""
                       )


        hbox = QGridLayout()
        # hbox.addStretch(1)
        hbox.addWidget(self.labelmsg,0,0)
        hbox.addWidget(self.btnCancel,1,2)
        hbox.addWidget(self.btnPUSH,1,1)
        hbox.addWidget(self.msg,0,1)
        hbox.addWidget(self.a,0,2)
        # hbox.addWidget(self.listview, 0, 2)
        hbox.addWidget(label,2,2)




        self.setLayout(hbox)


        self.show()

    def _initSignals(self):

        self.btnCancel.clicked.connect(self.CloseWin)
        self.btnPUSH.clicked.connect(self.PUSH)
    def Onclick(self):

        self.p.show()
    def CloseWin(self):
        ModelView.ModelView.g.flag=0
        self.close()
    # окно auntificacii
    def PUSH(self):
        if self.msg.text() is not None:
            ModelView.ModelView.g.MSG=self.msg.text()
            self.msg.setText("")
            ModelView.ModelView.g.flag = 1
            ModelView.ModelView.g.sendData()
            import time
            time.sleep(1)
            self.a.append(ModelView.ModelView.g.MSG +">>"+ModelView.ModelView.g.OUTMSG)




if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = Windows()
    w.show()
    sys.exit(app.exec_())