from Queue import PriorityQueue
from Ambiente import Ambiente

class Asterisco:



    def __init__(self):
        self.queuePrio = PriorityQueue()
        self.miAmbiente = Ambiente("archivo.txt")
        self.buscarAsterico()


    def getExpandiblesAsterisco(self, pos, costo, carga):
        #abajo, derecha, izquierda, arriba
        #arriba
        #si entrega -1 o 1, no existe la posicion o hay una pared respectivamente
        if(abs(self.miAmbiente.getPosition(pos[0]-1,pos[1]))!=1):
            self.queuePrio.put([self.getDistanciaL(pos[0]-1,pos[1]) + costo+self.miAmbiente.getCosto(pos[0]-1,pos[1]), costo+self.miAmbiente.getCosto(pos[0]-1,pos[1]), pos[0]-1,pos[1], carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #izquierda
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]-1))!=1):
            self.queuePrio.put([self.getDistanciaL(pos[0], pos[1]-1) + costo+ self.miAmbiente.getCosto(pos[0],pos[1]-1), costo+self.miAmbiente.getCosto(pos[0],pos[1]-1), pos[0],pos[1]-1, carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #derech
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]+1))!=1):
            self.queuePrio.put([self.getDistanciaL(pos[0], pos[1]+1) + costo+ self.miAmbiente.getCosto(pos[0],pos[1]+1), costo+self.miAmbiente.getCosto(pos[0],pos[1]+1), pos[0],pos[1]+1, carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')'])
        #abajo
        if(abs(self.miAmbiente.getPosition(pos[0]+1,pos[1]))!=1):
            self.queuePrio.put([self.getDistanciaL(pos[0]+1, pos[1]) + costo+ self.miAmbiente.getCosto(pos[0]+1,pos[1]), costo+self.miAmbiente.getCosto(pos[0]+1,pos[1]), pos[0]+1,pos[1], carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')'])

    #calcula la distancia en l a la meta a partir de un punto x, y hasta una meta
    def getDistanciaL(self, x, y):
        return abs(self.meta[0]-x)+abs(self.meta[1]-y)


    def buscarAsterico(self):



        posicionActual = self.miAmbiente.posIniRobotConSln()
        self.meta = self.miAmbiente.posMeta()

        pos_ac_costo_heur= [self.getDistanciaL(posicionActual[0], posicionActual[1])]+ [0] + posicionActual + [6] + ['']

        self.queuePrio.put(pos_ac_costo_heur)
        posicionActual  = pos_ac_costo_heur[2:]

        while (posicionActual[0:2]!=self.meta)& (not (self.queuePrio.empty())):
            pos_ac_costo_heur = self.queuePrio.get()
            print pos_ac_costo_heur
            posicionActual = pos_ac_costo_heur[2:]

            carga = posicionActual[2]

            if self.miAmbiente.getPosition(posicionActual[0],posicionActual[1])== 6:
                carga =6

            if carga >0:
                self.getExpandiblesAsterisco(posicionActual, pos_ac_costo_heur[1],carga)

        if posicionActual[0:2]!=self.meta:
            solucion=['']

        #la solucion se filtra en el nivel de la meta
        solucion = posicionActual[3].split(' ') + [('('+ str(self.meta[0]) + ',' + str(self.meta[1]) + ')')]
        print solucion
        return solucion


obj = Asterisco()