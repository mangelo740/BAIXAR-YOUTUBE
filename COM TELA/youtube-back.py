import youtube_dl
from ui_untitled import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def main(ui):
    def executar():
        
        link = ui.lyoutube.text()
        
        with youtube_dl.YoutubeDL({}) as ydl:
            ydl.download([link])

            
    ui.bdownload.clicked.connect(executar)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())