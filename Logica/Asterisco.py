from Queue import PriorityQueue
from Ambiente import Ambiente

class Asterisco:



    def __init__(self):
        self.queuePrio = PriorityQueue()
        self.miAmbiente = Ambiente("archivo.txt")
        self.nodosCread = 0

    #tipo de heuristica: 1 para distanciaL y 2 para distanciaLsobreCarga
    def getExpandiblesAsterisco(self, pos, costo, carga, tipoHeur):
        #abajo, derecha, izquierda, arriba
        #arriba
        #si entrega -1 o 1, no existe la posicion o hay una pared respectivamente
        if(abs(self.miAmbiente.getPosition(pos[0]-1,pos[1]))!=1):
            self.nodosCread+=1
            if tipoHeur==1:
                self.queuePrio.put([self.getDistanciaL(pos[0]-1,pos[1]) + costo+self.miAmbiente.getCosto(pos[0]-1,pos[1]), costo+self.miAmbiente.getCosto(pos[0]-1,pos[1]), pos[0]-1,pos[1], carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')', pos[4]+1])
            elif tipoHeur==2:
                self.queuePrio.put([self.getLSobreCarga(pos[0]-1,pos[1], carga-1) + costo+self.miAmbiente.getCosto(pos[0]-1,pos[1]), costo+self.miAmbiente.getCosto(pos[0]-1,pos[1]), pos[0]-1,pos[1], carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')', pos[4]+1])
        #izquierda
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]-1))!=1):
            self.nodosCread+=1
            if tipoHeur==1:
                self.queuePrio.put([self.getDistanciaL(pos[0], pos[1]-1) + costo+ self.miAmbiente.getCosto(pos[0],pos[1]-1), costo+self.miAmbiente.getCosto(pos[0],pos[1]-1), pos[0],pos[1]-1, carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')', pos[4]+1])
            elif tipoHeur==2:
                self.queuePrio.put([self.getLSobreCarga(pos[0], pos[1]-1, carga-1) + costo+ self.miAmbiente.getCosto(pos[0],pos[1]-1), costo+self.miAmbiente.getCosto(pos[0],pos[1]-1), pos[0],pos[1]-1, carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')', pos[4]+1])
        #derech
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]+1))!=1):
            self.nodosCread+=1
            if tipoHeur==1:
                self.queuePrio.put([self.getDistanciaL(pos[0], pos[1]+1) + costo+ self.miAmbiente.getCosto(pos[0],pos[1]+1), costo+self.miAmbiente.getCosto(pos[0],pos[1]+1), pos[0],pos[1]+1, carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')', pos[4]+1])
            elif tipoHeur==2:
                self.queuePrio.put([self.getLSobreCarga(pos[0], pos[1]+1, carga-1) + costo+ self.miAmbiente.getCosto(pos[0],pos[1]+1), costo+self.miAmbiente.getCosto(pos[0],pos[1]+1), pos[0],pos[1]+1, carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')', pos[4]+1])
        #abajo
        if(abs(self.miAmbiente.getPosition(pos[0]+1,pos[1]))!=1):
            self.nodosCread+=1
            if tipoHeur==1:
                self.queuePrio.put([self.getDistanciaL(pos[0]+1, pos[1]) + costo+ self.miAmbiente.getCosto(pos[0]+1,pos[1]), costo+self.miAmbiente.getCosto(pos[0]+1,pos[1]), pos[0]+1,pos[1], carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')', pos[4]+1])
            elif tipoHeur==2:
                self.queuePrio.put([self.getLSobreCarga(pos[0]+1, pos[1], carga-1) + costo+ self.miAmbiente.getCosto(pos[0]+1,pos[1]), costo+self.miAmbiente.getCosto(pos[0]+1,pos[1]), pos[0]+1,pos[1], carga-1, pos[3] + ' (' + str(pos[0]) + ',' + str(pos[1])+ ')', pos[4]+1])

    #calcula la distancia en l a la meta a partir de un punto x, y hasta una meta
    def getDistanciaL(self, x, y):
        return abs(self.meta[0]-x)+abs(self.meta[1]-y)

    def getLSobreCarga(self, x, y, carga):
        if [x,y]==self.meta:
            res = 0 #la distancia en L es 0, por ende la division es 0
        else:
            if carga>0:
                res = self.getDistanciaL(x,y)/carga #en el unico caso en que no seria admisible es cuando la carga es 0, porque la heuristica seria infinito, pero ps el costo a la meta no se cual seria como por ahi no se puede llegar a la meta
            else:
                res = float("inf")
        return res


    def buscarAsterico(self):
        posicionActual = self.miAmbiente.posIniRobotConSln()
        self.meta = self.miAmbiente.posMeta()

        cargaMax = 6
        tipoHeur=1
        if tipoHeur ==1:
            pos_ac_costo_heur= [self.getDistanciaL(posicionActual[0], posicionActual[1])]+ [0] + posicionActual + [cargaMax] + [''] + [0]
        elif tipoHeur ==2:
            pos_ac_costo_heur= [self.getLSobreCarga(posicionActual[0], posicionActual[1], cargaMax)]+ [0] + posicionActual + [cargaMax] + [''] + [0]

        self.queuePrio.put(pos_ac_costo_heur)
        self.nodosCread+=1
        posicionActual  = pos_ac_costo_heur[2:]

        limitacion = pow(self.miAmbiente.tamano, 2)

        nodosExp=0

        nivelMax = 0
        
        while (posicionActual[0:2]!=self.meta)& (not (self.queuePrio.empty())):
            nodosExp+=1
            pos_ac_costo_heur = self.queuePrio.get()
            #print pos_ac_costo_heur
            posicionActual = pos_ac_costo_heur[2:]
            nivel = posicionActual[4]
            carga = posicionActual[2]

            #nivel maximo
            if(nivel>nivelMax):
                nivelMax=nivel
                
            if self.miAmbiente.getPosition(posicionActual[0],posicionActual[1])== 6:
                carga =cargaMax

            if (limitacion>nivel) & (carga >0):
                self.getExpandiblesAsterisco(posicionActual, pos_ac_costo_heur[1],carga,tipoHeur)


        #la solucion se filtra en el nivel de la meta
        solucion = posicionActual[3].split(' ') + [('('+ str(self.meta[0]) + ',' + str(self.meta[1]) + ')')]
        if posicionActual[0:2]!=self.meta:
            solucion=['']

        ramificacion = self.nodosCread**(1/float(nivelMax))
        
        #solucion como lista, no string
        solucion_estructurada = self.estructurarSln(solucion)

        print "nodos Creados", self.nodosCread
        print "costo ", pos_ac_costo_heur[1]
        print "nodos expandidos ", nodosExp
        print "ramificacion ", ramificacion
        print "solucion ",solucion_estructurada



        return solucion_estructurada

    def estructurarSln(self, sln):
        solucion_estructurada = []
        for sln_u in sln[1:]:
            sln_u_div = sln_u.split(',')
            x = int(sln_u_div[0][1:])
            y = int(sln_u_div[1][:len(sln_u_div[1])-1])
            solucion_estructurada.append([x,y])
        return  solucion_estructurada

