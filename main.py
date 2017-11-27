import sys

from PyQt5.QtWidgets import QApplication
from ModelView import ModelView

def main():
    app = QApplication(sys.argv)
    ModelView.initial()
    sys.exit(app.exec_())

main()