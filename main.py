from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox


app = QApplication([])
window = QWidget()
window.resize(400, 200)
window.setWindowTitle("Рандом")


ans1 = QRadioButton("1")
ans2 = QRadioButton("2")
ans3 = QRadioButton("3")
ans4 = QRadioButton("4")
ans5 = QRadioButton("5")

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()


layoutH1.addWidget(ans1, alignment = Qt.AlignCenter)
layoutH1.addWidget(ans2, alignment = Qt.AlignCenter)
layoutH2.addWidget(ans3, alignment = Qt.AlignCenter)
layoutH3.addWidget(ans4, alignment = Qt.AlignCenter)
layoutH3.addWidget(ans5, alignment = Qt.AlignCenter)
layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
window.setLayout(layout_main)


def win():
    text = QMessageBox()
    text.setText("Верно!")
    text.exec_()

def lose():
    lost = QMessageBox()
    lost.setText("Ошибка!")
    lost.exec_()

ans1.clicked.connect(win)
ans2.clicked.connect(lose)
ans3.clicked.connect(lose)
ans4.clicked.connect(lose)
ans5.clicked.connect(lose)
window.show()
app.exec_()
