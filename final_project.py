from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set the window title
        self.setWindowTitle("PySide6 Example")
        
        # Create a label and set it as the central widget
        label = QLabel("Hello, PySide6!")
        self.setCentralWidget(label)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
