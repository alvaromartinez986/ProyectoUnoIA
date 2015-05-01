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
            self.queuePrio.put([costo+self.miAmbiente.getCosto(pos[0]-1,pos[1]), pos[0]-1,pos[1], pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #izquierda
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]-1))!=1):
            self.queuePrio.put([costo+ self.miAmbiente.getCosto(pos[0],pos[1]-1), pos[0],pos[1]-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #derech
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]+1))!=1):
            self.queuePrio.put([costo+ self.miAmbiente.getCosto(pos[0],pos[1]+1), pos[0],pos[1]+1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #abajo
        if(abs(self.miAmbiente.getPosition(pos[0]+1,pos[1]))!=1):
            self.queuePrio.put([costo+ self.miAmbiente.getCosto(pos[0]+1,pos[1]) , pos[0]+1,pos[1], pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')'])

    #calcula la distancia en l a la meta a partir de un punto x, y hasta una meta
    def getDistanciaL(self, x, y, meta):
        res  = abs(meta[0]-x)+abs(meta[1]-y)
        return res


    def buscarAsterico(self):


        nivel = 0

        posicionActual = self.miAmbiente.posIniRobotConSln()
        posicionMeta = self.miAmbiente.posMeta()

        print posicionActual

        self.queuePrio.put(posicionActual)
        posicionActual  = posicionActual[1:]


        #abajo, derecha, izquierda, arriba
        while (posicionActual[0:2]!=posicionMeta):
            posicionAcConCosto = self.queuePrio.get()
            print posicionAcConCosto
            posicionActual = posicionAcConCosto[1:]


            self.getExpandiblesAsterisco(posicionActual, posicionAcConCosto[0])


        #la solucion se filtra en el nivel de la meta
        print posicionActual[2].split(' ')
        return posicionActual[2].split(' ')


obj = Asterisco()