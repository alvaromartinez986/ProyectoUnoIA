__author__ = 'alvaro'

from Queue import PriorityQueue
from Ambiente import Ambiente

class Asterisco:



    def __init__(self):
        self.queuePrio = PriorityQueue()
	self.miAmbiente = Ambiente("archivo.txt")


    def getExpandiblesAsterisco(self, pos, nivel, costo):
        #abajo, derecha, izquierda, arriba
        #arriba
        #si entrega -1 o 1, no existe la posicion o hay una pared respectivamente
        if(abs(self.miAmbiente.getPosition(pos[0]-1,pos[1]))!=1):
            self.queuePrio.put((costo+self.miAmbiente.getCosto(self.miAmbiente.getPosition(pos[0]-1,pos[1], pos[0]-1,pos[1], nivel))))
        #izquierda
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]-1))!=1):
            self.queuePrio.put((costo+ self.miAmbiente.getCosto(self.miAmbiente.getPosition(pos[0],pos[1]-1), pos[0],pos[1]-1, nivel)))
        #derecha
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]+1))!=1):
            self.queuePrio.put((costo+ self.miAmbiente.getCosto(self.miAmbiente.getPosition(pos[0],pos[1]+1)), pos[0],pos[1]+1, nivel))
        #abajo
        if(abs(self.miAmbiente.getPosition(pos[0]+1,pos[1]))!=1):
            self.queuePrio.put(((costo+ self.miAmbiente.getCosto(self.miAmbiente.getPosition(pos[0]+1,pos[1])) , pos[0]+1,pos[1], nivel)))



    def buscarAsterico(self):


        nivel = 0

        posicionActual = self.miAmbiente.posIniRobot().append(nivel)
        posicionMeta = self.miAmbiente.posMeta()

        self.queuePrio.put((0, posicionActual))

        solucion = []
        #abajo, derecha, izquierda, arriba
        while (posicionActual[0:1]!=posicionMeta):
            posicionActual = self.queuePrio.get()[1:]
            nivel= posicionActual[2]
            solucion[nivel] = posicionActual[0:1]
            self.getExpandibles(posicionActual, nivel+1)


        #la solucion se filtra en el nivel de la meta
        return solucion[0:nivel]


