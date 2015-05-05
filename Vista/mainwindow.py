from PyQt4 import uic
from PyQt4 import QtCore, QtGui

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""
    
    solucion =[]
    contador_sln=0

    def __init__ ( self, parent = None , ambiente= None):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.ui.tbAmbiente.setEnabled(False)
        self.ambiente = ambiente
        self.inicializar_tabla()
        self.connect(self.ui.btSalir, QtCore.SIGNAL("clicked()"), self.salir_clicked)
        self.connect(self.ui.btSgte, QtCore.SIGNAL("clicked()"), self.sgte_clicked)
        
    def __del__ ( self ):
        self.ui = None

    def inicializar_tabla(self):
        self.ui.tbAmbiente.setRowCount(len(self.ambiente))
        self.ui.tbAmbiente.setColumnCount(len(self.ambiente))
        i=0
        for fila in self.ambiente:
            j=0
            for celda in fila:
                self.ui.tbAmbiente.setItem(i, j, QtGui.QTableWidgetItem())
                if celda==0:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(112,102,201))
                elif celda==1:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(147,147,147))
                elif celda==2:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(128,183,123))
                elif celda==3:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(128,183,0))
                elif celda==4:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(128,0,0))
                elif celda==5:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(255,0,0))
                elif celda==6:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(255,0,255))
                elif celda==7:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(255,255,0))
                j+=1
            i+=1
    
    def sgte_clicked(self):
        paso =self.solucion[self.contador_sln]
        self.ui.tbAmbiente.setItem(paso[0], paso[1], QtGui.QTableWidgetItem())
        self.ui.tbAmbiente.item(paso[0], paso[1]).setIcon(QtGui.QIcon("iconosIA/robot-1.png"))
        self.contador_sln+=1
    
    def salir_clicked(self):
        self.close()