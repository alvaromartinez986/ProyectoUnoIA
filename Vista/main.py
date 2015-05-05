import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainwindow import MainWindow

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'proyectoIa1' )

    # create widget
    w = MainWindow(None, [[0, 1, 1], [2, 2, 2], [2, 2, 7]])
    w.solucion = [[0,0], [1,0], [1,1], [2, 1], [2, 2]]
    w.setWindowTitle( 'proyectoIa1' )
    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
