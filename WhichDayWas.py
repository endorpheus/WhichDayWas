import sys
import os
from PySide6.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, 
                               QLineEdit, QSystemTrayIcon, QMenu, 
                               QDialog, QVBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction, QPixmap, QPainter, QFont

VERSION = "1.0.1"
TRANSPARENCY = 0.92  # 1 = full opacity

class WhichDayWas(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # set window slightly transparent
        self.setWindowOpacity(TRANSPARENCY)

        # Set the custom background and text color
        self.setStyleSheet("""
            QWidget {
                background-color: #60154B;  /* Background color */
                color: #E9C8D4;             /* Text color */
            }
            QLineEdit {
                background-color: black;   /* Input box background */
                color: white;              /* Input box text color */
                border: 1px solid #E9C8D4; /* Border color matching the text */
            }
        """)

        grid = QGridLayout()
        self.setLayout(grid)

        year_label = QLabel("Year")
        month_label = QLabel("Month")
        day_label = QLabel("Day")

        self.year_entry = QLineEdit()
        self.month_entry = QLineEdit()
        self.day_entry = QLineEdit()

        self.year_entry.textChanged.connect(self.calculate_day)
        self.month_entry.textChanged.connect(self.calculate_day)
        self.day_entry.textChanged.connect(self.calculate_day)

        grid.addWidget(year_label, 0, 0)
        grid.addWidget(self.year_entry, 0, 1)
        grid.addWidget(month_label, 1, 0)
        grid.addWidget(self.month_entry, 1, 1)
        grid.addWidget(day_label, 2, 0)
        grid.addWidget(self.day_entry, 2, 1)

        # Get the correct path for the icon if it exists
        icon_path = os.path.join(os.path.dirname(__file__), "icons/Sun.png")

        if os.path.exists(icon_path):
            # Icon file exists, load the icon
            icon = QIcon(icon_path)
            pixmap = QPixmap(icon_path)  # Load the QPixmap directly
            print("Icon loaded successfully")
        else:
            # Icon file doesn't exist, create a fallback icon
            print("Icon file not found, creating fallback icon")
            pixmap = QPixmap(64, 64)
            pixmap.fill(Qt.transparent)  # Make the pixmap transparent
            painter = QPainter(pixmap)
            font = QFont("Arial", 48)
            painter.setFont(font)
            painter.drawText(pixmap.rect(), Qt.AlignCenter, "☼")  # Draw the sun symbol
            painter.end()
            icon = QIcon(pixmap)
            #save the created icon in the icons folder
            pixmap.save(os.path.join(os.path.dirname(__file__), "icons/Sun.png"))

        # Set window title and icon
        self.setWindowTitle("Which Day Was")
        self.setWindowIcon(icon)

        # Tray Icon Setup
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(icon)

        # Tray menu setup
        self.tray_menu = QMenu(self)

        # Add "About" option to the menu
        self.about_action = QAction("About", self)
        self.about_action.triggered.connect(self.show_about_dialog)
        self.tray_menu.addAction(self.about_action)  # Add above the Quit option

        # Add "Quit" option to the menu
        self.quit_action = QAction("Quit", self)
        self.quit_action.triggered.connect(QApplication.quit)
        self.tray_menu.addAction(self.quit_action)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        self.tray_icon.show()

        self.resize(270, 90)  # Set the geometry of the window
        self.centerOnScreen(self)
        self.hide()  # Hide the main window

    def on_tray_icon_activated(self, reason):
        # Check if the left mouse button was clicked
        if reason == QSystemTrayIcon.Trigger:  # Left-click
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def show_about_dialog(self):
        about_dialog = QDialog(self)
        about_dialog.setWindowOpacity(TRANSPARENCY)
        src_img = os.path.join(os.path.dirname(__file__), "icons/Sun.png")
        label = QLabel(f"""
            <center>
                <h2>Which Day Was</h2>
                <p>Version: <b>{VERSION}</b></p>
                <p>Developed by <b>Ryon Shane Hall</b></p>
                <p>endorpheus@gmail.com</p>
                <p><a href="https://github.com/endorpheus">My GitHub</a></p>
                <p>Find out the day your ancestors were born, and thank them!</p>
                <p>
                    <img src="{src_img}" width="64" height="64"/>                </p>
            </center>
        """, about_dialog)

        layout = QVBoxLayout()
        layout.addWidget(label)
        about_dialog.setLayout(layout)
        self.centerOnScreen(about_dialog)

        about_dialog.show()

    def zeller_congruence(self, year, month, day):
        if month < 3:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

        day_of_week = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
        weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        return weekdays[day_of_week]

    def calculate_day(self):
        try:
            year = int(self.year_entry.text())
            month = int(self.month_entry.text())
            day = int(self.day_entry.text())

            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError("Month should be between 1-12 and day should be between 1-31.")

            weekday = self.zeller_congruence(year, month, day)

            self.setWindowTitle(f"{month}/{day}/{year} is a {weekday}")
        except ValueError:
            pass

    def centerOnScreen(self, window):
        screen_geometry = QApplication.screens()[0].availableGeometry()
        window.move((screen_geometry.width() / 2) - (window.frameSize().width() / 2),
                    (screen_geometry.height() / 2) - (window.frameSize().height() / 2))

    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WhichDayWas()
    sys.exit(app.exec())
