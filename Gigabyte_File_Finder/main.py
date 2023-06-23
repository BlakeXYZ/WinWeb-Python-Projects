## Clickable Hyperlink Import
from PyQt5.QtCore import QEvent, QUrl
from PyQt5.QtGui import QDesktopServices
##
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.uic import loadUi
import sys, os

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), 'main.ui')
        loadUi(ui_path, self)
        self.setWindowTitle("Gigabyte File Finder")

        ## Register Search button
        self.searchBtn.clicked.connect(self.show_folder_sizes)
        self.clearBtn.clicked.connect(self.reset_text)


        ## Set Tool Tips
        self.searchBtn.setToolTip("Click to Search for Files larger than 1 gb inside Path you have pasted above")
        self.clearBtn.setToolTip("Clears Input and Output Text")
        self.myOutputText.setToolTip("Click on Hyperlinks to Reveal in File Explorer!")




    def show_folder_sizes(self):                                                            ## SHOW FOLDER SIZES

        pathToWalk = os.path.abspath(self.myInputText.text())

        ##  set up output text in a string variable
        output_text = f"Output:<br> Searching in... {pathToWalk}<br><br>"
        text_added = False


        for dirpath, dirnames, filenames in os.walk(pathToWalk):
            # Set File Size Var
            byte_size = 0

            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                byte_size += os.path.getsize(file_path)
                
            
            kb_size = round(byte_size / 1024, 2)
            mb_size = round(kb_size / 1024, 2)
            gb_size = round(mb_size / 1024, 2)

            if gb_size >= 1:
                ##  accumulate the output text in a string variable
                output_text += f'<a href="{dirpath}" style="color: #11A8CD"; cursor: pointer;>{dirpath}</a><br>--- <b> contains {gb_size} gb</b> <br> <br>'
                text_added = True
                
            elif mb_size >= 1:
                #output_text += f"{dirpath}: {mb_size} mb\n"
                continue
            elif kb_size >= 1:
                # print(f"{dirpath}: {kb_size} kb")
                continue
            else:
                # print(f"{dirpath}: {byte_size} bytes")
                continue

        # Check if no text was added from gb_size >= 1
        if not text_added:
            output_text += '--- <b>No Folders or Files greater than 1 gb!</b> ---'
            
        ## ADD output_text string into "myOutputText" Widget
        self.myOutputText.setHtml(output_text)
        
        ## Capture and handle specific events that occur within the QTextEdit widget
        ### In this case, we want to handle mouse button press events 
        ### on the QTextEdit widget to detect when a link is clicked.
        self.myOutputText.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        ## check if the target object of the event is
        # viewport of self.myOutputText and if event type is MouseButtonPress. 
        if obj == self.myOutputText.viewport() and event.type() == QEvent.MouseButtonPress:
            anchor = self.myOutputText.anchorAt(event.pos())
            if anchor:
                QDesktopServices.openUrl(QUrl.fromLocalFile(anchor))


        return super().eventFilter(obj, event)


    def reset_text(self):                                                                   ## RESET BUTTON
        self.myInputText.clear()
        self.myOutputText.clear()

if __name__ == '__main__':
    print('\n ** \n *** \n Launching')
    print(" _____ _             _           _        ______ _ _       ______ _           _           \n"
        "|  __ (_)           | |         | |       |  ___(_| |      |  ___(_)         | |          \n"
        "| |  \/_  __ _  __ _| |__  _   _| |_ ___  | |_   _| | ___  | |_   _ _ __   __| | ___ _ __ \n"
        "| | __| |/ _` |/ _` | '_ \| | | | __/ _ \ |  _| | | |/ _ \ |  _| | | '_ \ / _` |/ _ | '__|\n"
        "| |_\ | | (_| | (_| | |_) | |_| | ||  __/ | |   | | |  __/ | |   | | | | | (_| |  __| |   \n"
        " \____|_|\__, |\__,_|_.__/ \__, |\__\___| \_|   |_|_|\___| \_|   |_|_| |_|\__,_|\___|_|   \n"
        "          __/ |             __/ |     ______           ______                             \n"
        "         |___/             |___/     |______|         |______|                            \n *** \n **")

    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec()
    