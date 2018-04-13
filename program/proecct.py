from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QHBoxLayout
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit,QMainWindow,QGridLayout
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon

class User(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):

        self.window1 = QWidget() 
        grid = QGridLayout()
        self.knopka = QPushButton("Начать")
        self.knopka.clicked.connect(self.next)
        

        
        self.nameText = QLabel('Введите имя', self)
        self.nameInput = QLineEdit(self)
        self.surnameText = QLabel('Введите фамилию', self)
        self.surnameInput = QLineEdit(self)
        self.button = QPushButton('Зарегистрироваться',self)
        self.button.clicked.connect(self.setForm)


       
        self.nameText1 = QLabel('Введите имя', self)
        self.nameInput1 = QLineEdit(self)
        self.surnameText1 = QLabel('Введите фамилию', self)
        self.surnameInput1 = QLineEdit(self)
        self.button1 = QPushButton('Войти',self)
        
        self.button1.clicked.connect(self.sedForm)
        grid.addWidget(self.button1,1,2,2,2)
        grid.addWidget(self.button,1,1,2,1)
        grid.addWidget(self.nameText1,2,2,1,1)
        grid.addWidget(self.nameInput1,3,2,1,1)
        grid.addWidget(self.surnameText1,4,2,1,1)
        grid.addWidget(self.surnameInput1,5,2,1,1)
        grid.addWidget(self.nameInput,3,1,1,1)
        grid.addWidget(self.nameText,2,1,1,1)
        grid.addWidget(self.surnameInput,5,1,1,1)
        grid.addWidget(self.surnameText,4,1,1,1)
        grid.addWidget(self.knopka,0,1,2,2)
        
        


        
        self.window1.setLayout(grid)

        self.window2 = QWidget()
        grid = QGridLayout()
        
        self.window2.setLayout(grid)
        
        
        self.s1 = QPushButton('Урок№1')
        
        self.s2 = QPushButton('Урок№2')
       
        self.s3 = QPushButton('Урок№3')
       
        self.s4 = QPushButton('Урок№4')
        
        self.s5 = QPushButton('Урок№5')
       
        self.s6 = QPushButton('Урок№6')
        
        grid.addWidget(self.s1, 1, 0)
        grid.addWidget(self.s2, 1, 1)
        grid.addWidget(self.s3, 2, 0)
        grid.addWidget(self.s4, 2, 1)
        grid.addWidget(self.s5, 3, 0)
        grid.addWidget(self.s6, 3, 1)
        self.s1.clicked.connect(self.next2)
        self.window3 = QWidget()
        grid = QGridLayout()
        self.window3.setLayout(grid)
        self.b1 = QLabel("""25525""")
        self.g1 = QPushButton("Тест")
        
        grid.addWidget(self.g1, 1, 0)
        grid.addWidget(self.b1, 0, 0)


        
        self.setCentralWidget(self.window1)

        self.setGeometry(100, 100, 700, 700)
        self.show()
        
        
    def next(self):
        self.setCentralWidget(self.window2)
    def next2(self):
        self.setCentralWidget(self.window3)

    def sedForm(self):
        f = open('User list.txt')
        user_info = self.nameInput1.text() + ' ' + self.surnameInput1.text() + ';'
        text = f.read()
        if user_info in text:
            print('Добро пожаловать')
            self.knopka.setEnabled(True)
        else:
            print('Вас нет в списке')
        f.close()
        self.nameInput.setText('')
        self.surnameInput.setText('') 

    def setForm(self):
        f = open('User list.txt', 'a')
        f.write(self.nameInput.text() + ' ' + self.surnameInput.text() + ';\n')
        f.close()
        self.nameInput.setText('')
        self.surnameInput.setText('')

app = QApplication(sys.argv)
my_window = User()
sys.exit(app.exec_())