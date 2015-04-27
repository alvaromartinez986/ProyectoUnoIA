from Queue import PriorityQueue
from Ambiente import Ambiente

class Asterisco:



    def __init__(self):
        self.queuePrio = PriorityQueue()
        self.miAmbiente = Ambiente("archivo.txt")
        self.buscarAsterico()


    def getExpandiblesAsterisco(self, pos, costo):
        #abajo, derecha, izquierda, arriba
        #arriba
        #si entrega -1 o 1, no existe la posicion o hay una pared respectivamente
        if(abs(self.miAmbiente.getPosition(pos[0]-1,pos[1]))!=1):
            self.queuePrio.put([costo+self.miAmbiente.getCosto(pos[0]-1,pos[1]), pos[0]-1,pos[1], pos[2] + '(' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #izquierda
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]-1))!=1):
            self.queuePrio.put([costo+ self.miAmbiente.getCosto(pos[0],pos[1]-1), pos[0],pos[1]-1, pos[2] + '(' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #derech
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]+1))!=1):
            self.queuePrio.put([costo+ self.miAmbiente.getCosto(pos[0],pos[1]+1), pos[0],pos[1]+1, pos[2] + '(' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #abajo
        if(abs(self.miAmbiente.getPosition(pos[0]+1,pos[1]))!=1):
            self.queuePrio.put([costo+ self.miAmbiente.getCosto(pos[0]+1,pos[1]) , pos[0]+1,pos[1], pos[2] + '(' + str(pos[0]) + ',' + str(pos[1])+ ')'])


    def buscarAsterico(self):


        nivel = 0

        posicionActual = self.miAmbiente.posIniRobotConCosto()
        posicionMeta = self.miAmbiente.posMeta()

        self.queuePrio.put(posicionActual)
        posicionActual  = posicionActual[1:]
        print posicionActual
        solucion = []
        #abajo, derecha, izquierda, arriba
        while (posicionActual[0:2]!=posicionMeta):
            posicionAcConCosto = self.queuePrio.get()
            print posicionAcConCosto
            posicionActual = posicionAcConCosto[1:]
            nivel= posicionActual[2]
            if (len(solucion)>nivel):
                solucion[nivel] = posicionActual[0:2]
            else:
                solucion.append(posicionActual[0:2])

            self.getExpandiblesAsterisco(posicionActual, posicionAcConCosto[0])


        #la solucion se filtra en el nivel de la meta
        print solucion
        return solucion[0:nivel]


obj = Asterisco()