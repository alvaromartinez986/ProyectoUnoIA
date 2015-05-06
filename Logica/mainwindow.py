from PyQt4 import uic
from PyQt4 import QtCore, QtGui


from Asterisco import Asterisco
from Profundidad import Profundidad

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""
    
    solucion =[]
    contador_sln=0

    def __init__ ( self, parent = None , ambiente= None):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.ambiente = ambiente
        self.inicializar_tabla()
        self.ui.tbAmbiente.resize((len(self.ambiente))*50+10,(len(self.ambiente))*50+8)
        self.showMaximized()
        self.connect(self.ui.btSalir, QtCore.SIGNAL("clicked()"), self.salir_clicked)
        self.connect(self.ui.btSgte, QtCore.SIGNAL("clicked()"), self.sgte_clicked)
        self.ui.rbProf.toggled.connect(self.rbProf_clicked)
        self.ui.rbAs.toggled.connect(self.rbAs_clicked)
        
        
    def __del__ ( self ):
        self.ui = None

    def inicializar_tabla(self):
        self.ui.tbAmbiente.setRowCount(len(self.ambiente))
        self.ui.tbAmbiente.setColumnCount(len(self.ambiente))
        
        i=0
        for fila in self.ambiente:
            j=0
            self.ui.tbAmbiente.setColumnWidth(i,50)
            self.ui.tbAmbiente.setRowHeight(i,50)
            for celda in fila:
                self.ui.tbAmbiente.setItem(i, j, QtGui.QTableWidgetItem())
                self.ui.tbAmbiente.item(i, j).setFlags(QtCore.Qt.ItemIsEnabled )
                if celda==0:
                    self.ui.tbAmbiente.item(i, j).setIcon(QtGui.QIcon("iconosIA/robot-1.png"))
                elif celda==1:
                    self.ui.tbAmbiente.item(i, j).setIcon(QtGui.QIcon("iconosIA/pared.png"))
                elif celda==2:
                    self.ui.tbAmbiente.item(i, j).setBackgroundColor(QtGui.QColor(128,183,123))
                elif celda==3:
                    self.ui.tbAmbiente.item(i, j).setIcon(QtGui.QIcon("iconosIA/mojado.png"))
                elif celda==4:
                    self.ui.tbAmbiente.item(i, j).setIcon(QtGui.QIcon("iconosIA/gente.png"))
                elif celda==5:
                    self.ui.tbAmbiente.item(i, j).setIcon(QtGui.QIcon("iconosIA/restringido.png"))
                elif celda==6:
                    self.ui.tbAmbiente.item(i, j).setIcon(QtGui.QIcon("iconosIA/energia.png"))
                elif celda==7:
                    self.ui.tbAmbiente.item(i, j).setIcon(QtGui.QIcon("iconosIA/meta.png"))
                j+=1
            i+=1
    
    def sgte_clicked(self):
        if self.contador_sln<len(self.solucion):
            if self.contador_sln>0:
                pasoAnt =self.solucion[self.contador_sln-1]
                self.ui.tbAmbiente.setItem(pasoAnt[0], pasoAnt[1], QtGui.QTableWidgetItem())
                self.ui.tbAmbiente.item(pasoAnt[0], pasoAnt[1]).setIcon(QtGui.QIcon("iconosIA/robot-1.png"))
                self.ui.tbAmbiente.item(pasoAnt[0], pasoAnt[1]).setBackgroundColor(QtGui.QColor(255,255,255))
            paso =self.solucion[self.contador_sln]
            self.ui.tbAmbiente.setItem(paso[0], paso[1], QtGui.QTableWidgetItem())
            self.ui.tbAmbiente.item(paso[0], paso[1]).setIcon(QtGui.QIcon("iconosIA/robot-1.png"))
            self.ui.tbAmbiente.item(paso[0], paso[1]).setBackgroundColor(QtGui.QColor(0,0,0))
            self.contador_sln+=1

    def rbProf_clicked(self):
        self.solucion = Profundidad().buscarProfundidad()
        self.contador_sln= 0

    def rbAs_clicked(self):
        self.solucion = Asterisco().buscarAsterico()
        self.contador_sln= 0
    
    def salir_clicked(self):
        self.close()
