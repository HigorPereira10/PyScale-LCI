import sys
from PyQt6.QtWidgets import QApplication
from src.views.gui import EmergyGUI

def main():
    app = QApplication(sys.argv)
    window = EmergyGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()