import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QTextBrowser

class UserInfoForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Foydalanuvchi ma'lumotlari shakli")

        nameLabel = QLabel("Ism:")
        self.nameEdit = QLineEdit()
        emailLabel = QLabel("Elektron pochta manzili:")
        self.emailEdit = QLineEdit()
        bioLabel = QLabel("Qisqacha tarjimai hol:")
        self.bioEdit = QTextEdit()

        submitButton = QPushButton("Yuborish")
        submitButton.clicked.connect(self.submitForm)

        self.readOnlyTextArea = QTextBrowser()
        self.readOnlyTextArea.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(nameLabel)
        layout.addWidget(self.nameEdit)
        layout.addWidget(emailLabel)
        layout.addWidget(self.emailEdit)
        layout.addWidget(bioLabel)
        layout.addWidget(self.bioEdit)
        layout.addWidget(submitButton)
        layout.addWidget(self.readOnlyTextArea)

        self.setLayout(layout)

    def submitForm(self):
        name = self.nameEdit.text()
        email = self.emailEdit.text()
        bio = self.bioEdit.toPlainText()

        self.readOnlyTextArea.setText(f"Ism: {name}\nElektron pochta manzili: {email}\nQisqacha tarjimai hol: {bio}")

        self.nameEdit.setDisabled(True)
        self.emailEdit.setDisabled(True)
        self.bioEdit.setDisabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = UserInfoForm()
    form.show()
    sys.exit(app.exec_())