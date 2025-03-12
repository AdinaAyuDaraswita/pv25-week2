from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QComboBox, QGroupBox, QFormLayout
)
from PyQt5.QtGui import QFont
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        
        font = QFont("Calibri", 10)
        self.setFont(font)

        main_layout = QVBoxLayout()

        def add_section_with_spacing(title, widget):
            section_layout = QVBoxLayout()
            section_layout.addWidget(QLabel(title))
            section_layout.addWidget(widget)
            return section_layout
        
        # Identity Section
        identity_box = QGroupBox()
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Adina Ayu Daraswita"))
        identity_layout.addWidget(QLabel("Nim : F1D022030"))
        identity_layout.addWidget(QLabel("Kelas : D Pemrograman Visual"))
        identity_box.setLayout(identity_layout)
        main_layout.addLayout(add_section_with_spacing("Identitas (vertical box layout)", identity_box))
        
        # Navigation Section
        nav_box = QGroupBox()
        nav_layout = QHBoxLayout()
        
        home_button = QPushButton("Home")
        about_button = QPushButton("About")
        contact_button = QPushButton("Contact")

        # Ubah warna tombol jadi ungu
        for button in [home_button, about_button, contact_button]:
            button.setStyleSheet("background-color: purple; color: white; font-weight: bold; border-radius: 5px; padding: 5px;")

        nav_layout.addWidget(home_button)
        nav_layout.addWidget(about_button)
        nav_layout.addWidget(contact_button)
        nav_box.setLayout(nav_layout)
        main_layout.addLayout(add_section_with_spacing("Navigation (horizontal box layout)", nav_box))
        
        # Registration Form
        form_box = QGroupBox()
        form_layout = QVBoxLayout()
        form_container = QFormLayout()
        
        self.fullname_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select", "Indonesia", "Malaysia", "Singapore", "Thailand"])
        
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_container = QWidget()
        gender_container.setLayout(gender_layout)
        gender_container.setFixedWidth(200)

        for widget in [self.fullname_input, self.email_input, self.phone_input, self.country_combo]:
            widget.setFixedWidth(200)
            widget.setStyleSheet(
                "QLineEdit, QComboBox { border: 1px solid gray; padding: 5px; border-radius: 5px; }"
                "QLineEdit:hover, QComboBox:hover { border: 2px solid purple; }"
            )
        
        form_container.addRow(QLabel("Full Name:"), self.fullname_input)
        form_container.addRow(QLabel("Email:"), self.email_input)
        form_container.addRow(QLabel("Phone:"), self.phone_input)
        form_container.addRow(QLabel("Gender:"), gender_container)
        form_container.addRow(QLabel("Country:"), self.country_combo)
        
        centered_layout = QHBoxLayout()
        centered_layout.addStretch()
        centered_layout.addLayout(form_container)
        centered_layout.addStretch()
        
        form_layout.addLayout(centered_layout)
        form_box.setLayout(form_layout)
        main_layout.addLayout(add_section_with_spacing("User Registration (form layout)", form_box))
        
        # Actions Section
        actions_box = QGroupBox()
        actions_layout = QHBoxLayout()
        
        submit_button = QPushButton("Submit")
        cancel_button = QPushButton("Cancel")

        # Ubah warna tombol jadi ungu
        for button in [submit_button, cancel_button]:
            button.setStyleSheet("background-color: purple; color: white; font-weight: bold; border-radius: 5px; padding: 5px;")

        actions_layout.addWidget(submit_button)
        actions_layout.addWidget(cancel_button)
        actions_box.setLayout(actions_layout)
        main_layout.addLayout(add_section_with_spacing("Actions (horizontal box layout)", actions_box))
        
        # Set Layout
        self.setLayout(main_layout)
        self.setGeometry(100, 100, 400, 350)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())
