from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QHBoxLayout
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit,QMainWindow,QGridLayout,QToolTip
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
class Multi(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def form_1(self):
        self.win1 = QWidget(self)
        grid = QGridLayout()
        self.knopka = QPushButton("Начать",self.win1)
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
        
    
        self.win1.setLayout(grid)
        self.knopka.setEnabled(False)

        
        self.setWindowTitle('Learn Python')

    def form_2(self):
        self.win2 = QWidget(self)
        grid = QGridLayout()
        
        self.win2.setLayout(grid)

        self.but2 = QPushButton('Назад', self.win2)
        self.but2.clicked.connect(self.back)
        self.setWindowTitle('Learn Python')
        
        self.s1 = QPushButton('Урок№1')
        
        self.s2 = QPushButton('Урок№2')
       
        self.s3 = QPushButton('Урок№3')
       
        self.s4 = QPushButton('Урок№4')
  
        grid.addWidget(self.s1, 1, 0)
        grid.addWidget(self.s2, 1, 1)
        grid.addWidget(self.s3, 2, 0)
        grid.addWidget(self.s4, 2, 1)
        self.s1.clicked.connect(self.next2)
        self.s2.clicked.connect(self.next5_1)
        self.s3.clicked.connect(self.next7)
        self.s4.clicked.connect(self.next10)

    def form_3(self):
        self.win3 = QWidget(self)
        grid = QGridLayout()
        self.win3.setLayout(grid)
        pixmap = QPixmap("pp.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        grid.addWidget(lbl,1,1)

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('')
       
        self.btn = QPushButton('Тест', self)
        self.btn.setToolTip('В тесте 2 вопроса , за каждый ответ дается 1 балл')
        self.btn.resize(self.btn.sizeHint())
        grid.addWidget(self.btn,5,5)

    
        self.setWindowTitle('Learn Python')
        self.but3 = QPushButton('Назад', self.win3)
        self.but3.clicked.connect(self.back2)
        self.btn.clicked.connect(self.next3)
    def form_4(self):
        self.win4 = QWidget(self)
        grid = QGridLayout()
        self.win4.setLayout(grid)
        self.z = QLineEdit(self)
        self.z1 = QLineEdit(self)
        self.ma1 = QPushButton('Результаты', self)

        self.n1 = QLabel("""Python -
            1.Язык программирования
            2.Набор инструментов редактирования
            3.Среда разработки""", self)
        self.n2 = QLabel("""код python обрабатывается...
            1.Перед  выполнением
            2.Во время выполнения
            """, self)
        self.but43 = QPushButton('Назад', self.win3)
        self.but43.clicked.connect(self.back3)

        grid.addWidget(self.n2, 0, 1)
        grid.addWidget(self.n1, 0, 0)
        grid.addWidget(self.z, 1, 0)
        grid.addWidget(self.z1, 1, 1)
        grid.addWidget(self.ma1, 2,0)
        grid.addWidget(self.but43)
        
        self.setWindowTitle('Learn Python')
 
        self.ma1.clicked.connect(self.next4)
    def form_5(self):
        self.win5 = QWidget(self)
        grid = QGridLayout()
        self.win5.setLayout(grid)
       
        self.setWindowTitle('Learn Python')
    def form_6(self):
        self.win6 = QWidget(self)
        grid = QGridLayout()
        self.win6.setLayout(grid)
        pixmap1 = QPixmap("qq.jpg")
        lbl1 = QLabel(self)
        lbl1.setPixmap(pixmap1)
        grid.addWidget(lbl1,1,1)

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('')
        self.but24 = QPushButton('Назад', self.win6)
        self.but24.clicked.connect(self.back2)
        self.btn34 = QPushButton('Тест', self)
        self.btn34.setToolTip('В тесте 2 вопроса , за каждый ответ дается 1 балл')
        self.btn34.resize(self.btn34.sizeHint())
        
        grid.addWidget(self.btn34,5,5)
        grid.addWidget(self.but24,0,0)

    
        self.setWindowTitle('Learn Python')
        
        self.btn34.clicked.connect(self.next5)
       
        self.setWindowTitle('Learn Python')
    def form_7(self):
        self.win7= QWidget(self)
        grid = QGridLayout()
        self.win7.setLayout(grid)
        self.win7.setLayout(grid)
        self.l = QLineEdit(self)
        self.l1 = QLineEdit(self)
        self.l2 = QPushButton('Результаты', self)
        self.l3 = QLabel("""каким будет результат этой строки?
            >>>1 + 2 + 3""", self)
        self.l4 = QLabel("""каким будет результат этой строки?
            >>> 53 - (25 + 5) """, self)
        self.btn54 = QPushButton('Результаты', self)
        self.but53 = QPushButton('Назад', self.win7)
        self.but53.clicked.connect(self.back3)
        self.btn54.clicked.connect(self.next6)
        grid.addWidget(self.l3, 0, 1)
        grid.addWidget(self.l4, 0, 0)
        grid.addWidget(self.l, 1, 0)
        grid.addWidget(self.l1, 1, 1)
        grid.addWidget(self.btn54, 2,0)
        grid.addWidget(self.but53)

        self.setWindowTitle('Learn Python')
    def form_8(self):
        self.win8 = QWidget(self)
        grid = QGridLayout()
        self.win8.setLayout(grid)
        self.setWindowTitle('Learn Python')
    def form_9(self):
        self.win9 = QWidget(self)
        grid = QGridLayout()
        self.win9.setLayout(grid)
        pixmap2 = QPixmap("rr.jpg")
        lbl23 = QLabel(self)
        lbl23.setPixmap(pixmap2)
        grid.addWidget(lbl23,1,1)

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('')
        self.but244 = QPushButton('Назад', self.win9)
        self.but244.clicked.connect(self.back2)
        self.btn344 = QPushButton('Тест', self)
        self.btn344.setToolTip('В тесте 2 вопроса , за каждый ответ дается 1 балл')
        self.btn344.resize(self.btn344.sizeHint())
        self.btn344.clicked.connect(self.next8)
        
        grid.addWidget(self.btn344,5,5)
        grid.addWidget(self.but244,0,0)

    
        self.setWindowTitle('Learn Python')
        
        self.btn344.clicked.connect(self.next8)
    def form_10(self):
        self.win10= QWidget(self)
        grid = QGridLayout()
        self.win10.setLayout(grid)
        self.win10.setLayout(grid)
        self.l2 = QLineEdit(self)
        self.l12 = QLineEdit(self)
        self.l22 = QPushButton('Результаты', self)
        self.l32 = QLabel("""Каким будет результат этого выражения?
        >>> print("print("print") """, self)
        self.l42 = QLabel("""Каким будет результат этого выражения?
            >>> print "4" + "2" """, self)
        self.btn542 = QPushButton('Результаты', self)
        self.but532 = QPushButton('Назад', self.win10)
        self.but532.clicked.connect(self.back4)
        self.btn542.clicked.connect(self.next9)
        grid.addWidget(self.l32, 0, 1)
        grid.addWidget(self.l42, 0, 0)
        grid.addWidget(self.l2, 1, 0)
        grid.addWidget(self.l12, 1, 1)
        grid.addWidget(self.btn542, 2,0)
        grid.addWidget(self.but532)
    def form_11(self):
        self.win11 = QWidget(self)
        grid = QGridLayout()
        self.win11.setLayout(grid)
        self.setWindowTitle('Learn Python')
    def form_12(self):
        self.win12 = QWidget(self)
        grid = QGridLayout()
        self.win12.setLayout(grid)
        pixmap27 = QPixmap("ww.jpg")
        lbl237 = QLabel(self)
        lbl237.setPixmap(pixmap27)
        grid.addWidget(lbl237,1,1)

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('')
        self.but2447 = QPushButton('Назад', self.win12)
        self.but2447.clicked.connect(self.back2)
        self.btn3447 = QPushButton('Тест', self)
        self.btn3447.setToolTip('В тесте 2 вопроса , за каждый ответ дается 1 балл')
        self.btn3447.resize(self.btn3447.sizeHint())
        self.btn3447.clicked.connect(self.next11)
        
        grid.addWidget(self.btn3447,5,5)
        grid.addWidget(self.but2447,0,0)

    
        self.setWindowTitle('Learn Python')
    def form_13(self):
        self.win13= QWidget(self)
        grid = QGridLayout()
        self.win13.setLayout(grid)
        self.win13.setLayout(grid)
        self.l23 = QLineEdit(self)
        self.l123 = QLineEdit(self)
        self.l223 = QPushButton('Результаты', self)
        self.l323 = QLabel("""Какие из вариантов не являются числами с плавающей запятой?
        1)7.0
        2)7
        3)4.0 - 2.0 """, self)
        self.l423 = QLabel("""В каком из вариантов получится ответ с плавающей запятой
            1) 8 - 5
            2) 2  * 3
            3) 10 / 5""", self)
        self.btn5423 = QPushButton('Результаты', self)
        self.but5323 = QPushButton('Назад', self.win12)
        self.but5323.clicked.connect(self.back5)
        self.btn5423.clicked.connect(self.next12)
        grid.addWidget(self.l323, 0, 1)
        grid.addWidget(self.l423, 0, 0)
        grid.addWidget(self.l23, 1, 0)
        grid.addWidget(self.l123, 1, 1)
        grid.addWidget(self.btn5423, 2,0)
        grid.addWidget(self.but5323)
    def form_14(self):
        self.win14 = QWidget(self)
        grid = QGridLayout()
        self.win14.setLayout(grid)
        self.setWindowTitle('Learn Python')  

    def next(self):
        self.form_2()
        self.setCentralWidget(self.win2)

    def back(self):
        self.form_1()
        self.setCentralWidget(self.win1)
    def next2(self):
        self.form_3()
        self.setCentralWidget(self.win3)

    def back2(self):
        self.form_2()
        self.setCentralWidget(self.win2)
    def back3(self):
        self.form_3()
        self.setCentralWidget(self.win3)
    def back3(self):
        self.form_6()
        self.setCentralWidget(self.win6)
    def back4(self):
        self.form_9()
        self.setCentralWidget(self.win9)
    def back5(self):
        self.form_12()
        self.setCentralWidget(self.win12)
    
    def next3(self):
        self.form_4()
        self.setCentralWidget(self.win4)
    def next4(self):
        self.form_5()
        self.setCentralWidget(self.win5)
    def next5_1(self):
        self.form_6()
        self.setCentralWidget(self.win6)
    def next5(self):
        self.form_7()
        self.setCentralWidget(self.win7)
    def next6(self):
        self.form_8()
        self.setCentralWidget(self.win8)
    def next7(self):
        self.form_9()
        self.setCentralWidget(self.win9)
    def next8(self):
        self.form_10()
        self.setCentralWidget(self.win10)
    def next9(self):
        self.form_11()
        self.setCentralWidget(self.win11)
    def next10(self):
        self.form_12()
        self.setCentralWidget(self.win12)
    def next11(self):
        self.form_13()
        self.setCentralWidget(self.win13)
    def next12(self):
        self.form_14()
        self.setCentralWidget(self.win14)
  



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

    def initUI(self):
        self.setWindowIcon(QIcon('Python-3-Obzor.png'))
        self.setGeometry(100, 100, 700, 700)
        self.form_1()
        self.setCentralWidget(self.win1)
        self.show()

app = QApplication(sys.argv)
my_window = Multi()
sys.exit(app.exec_())

