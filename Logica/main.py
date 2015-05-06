import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainwindow import MainWindow

from Ambiente import Ambiente

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'proyectoIa1' )

    ambiente = Ambiente("archivo.txt").matriz

    # create widget
    w = MainWindow(None, ambiente)
    w.setWindowTitle( 'proyectoIa1' )
    w.show()

    solucion = []



    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
