########################################################################################################################
# module_main
########################################################################################################################


from package_gui.module_mainwindow import Mainwindow
import sys
from PyQt5.QtWidgets import QApplication


def main():
    # This is the main function:
    print("The function 'main' has been called!")

    app = QApplication(sys.argv)

    # Note: Mainwindow needs an instance 'mainwindow', otherwise the window will be deleted immediately!
    mainwindow = Mainwindow()

    sys.exit(app.exec_())


if __name__ == "__main__":

    main()


