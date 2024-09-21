import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

class Dastur(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Note App")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.kirish_widget = QLineEdit()
        layout.addWidget(self.kirish_widget)

        self.tugma_widget = QPushButton("Matnni Saqlash")
        self.tugma_widget.clicked.connect(self.matnni_saqlash)
        layout.addWidget(self.tugma_widget)

        self.matn_maydoni_widget = QTextEdit()
        layout.addWidget(self.matn_maydoni_widget)

    def matnni_saqlash(self):
        eslatma = self.kirish_widget.text()
        self.matn_maydoni_widget.append(eslatma)
        self.kirish_widget.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dastur()
    window.show()
    sys.exit(app.exec_())