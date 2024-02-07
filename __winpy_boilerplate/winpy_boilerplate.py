from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
import sys, os

class ValidationError(Exception):
    pass

class winpy_boilerplate(QtWidgets.QMainWindow):

    """
    Create a default tool window.
    """
    window = None

    def __init__(self, parent = None):
        """
        Initialize class.
        """
        super(winpy_boilerplate, self).__init__(parent = parent)

        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_dir = os.path.join(script_dir, 'winpy_boilerplate.ui')

        #load the created UI widget
        self.mainWidget = QtUiTools.QUiLoader().load(ui_dir)

        #attach the widget to the instance of this class (aka self)
        self.mainWidget.setParent(self)

        # Set the initial size of the main window to match the size of the loaded .ui file
        self.resize(self.mainWidget.size())

        ###
        ###
        # find interactive elements of UI
        self.btn_01 = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_01')
        self.btn_02 = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_02')

        ###
        ###
        # assign clicked handler to buttons
        self.btn_01.clicked.connect(self.print_to_log)
        self.btn_02.clicked.connect(self.closeWindow)
        
    
    """
    Code goes here
    """

    def print_to_log(self):

        print('btn_01 pressed')


    """
    BASE FUNCTIONS
    """
            
    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
        """
        self.mainWidget.resize(self.width(), self.height())
        
    def closeWindow(self):
        """
        Close window.
        """
        print ('closing window')
        self.close()  # Close the window
        QtWidgets.QApplication.quit()  # Quit the application

if __name__ == '__main__':
    print('\n ** \n *** \n Launching')
    app = QtWidgets.QApplication(sys.argv)
    window = winpy_boilerplate()
    window.show()
    sys.exit(app.exec_())
    