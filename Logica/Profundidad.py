from Ambiente import Ambiente
class Profundidad:

    

    def __init__(self):
        self.miAmbiente = Ambiente("archivo.txt")
        self.buscarProfundidad



    #posicion a expandir 
    #nivel de los nodos creados
    def getExpandibles(self, pos, nivel, carga):
        #abajo, derecha, izquierda, arriba
        hijos =[]
        #arriba
        #print "arriba"
        #print self.miAmbiente.getPosition(pos[0]-1,pos[1])
        #si entrega -1 o 1, no existe la posicion o hay una pared respectivamente
        if(abs(self.miAmbiente.getPosition(pos[0]-1,pos[1]))!=1):
            hijos.append([pos[0]-1,pos[1], nivel, carga])
        #izquierda
        #print "izq"
        #print self.miAmbiente.getPosition(pos[0],pos[1]-1)
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]-1))!=1):
            hijos.append([pos[0],pos[1]-1, nivel, carga])
        #derecha
        #print "der"
        #print self.miAmbiente.getPosition(pos[0],pos[1]+1)
        if(abs(self.miAmbiente.getPosition(pos[0],pos[1]+1))!=1):
            hijos.append([pos[0],pos[1]+1, nivel, carga])
        #abajo
        #print "aba"
        #print self.miAmbiente.getPosition(pos[0]+1,pos[1])
        if(abs(self.miAmbiente.getPosition(pos[0]+1,pos[1]))!=1):
            hijos.append([pos[0]+1,pos[1], nivel, carga])

        return hijos
    

    @property
    def buscarProfundidad(self):

        nivel = 0

        posicionActual = self.miAmbiente.posIniRobotConNivel()
        posicionMeta = self.miAmbiente.posMeta()
        
        limitacion = pow(self.miAmbiente.tamano, 2)

        pila = [posicionActual]

        solucion = []
        #abajo, derecha, izquierda, arriba
        while (posicionActual[0:2]!=posicionMeta)&(len(pila)!=0):
            hijos=[]
            posicionActual = pila.pop()
            nivel= posicionActual[2]
            carga = posicionActual[3]

            if self.miAmbiente.getPosition(posicionActual[0],posicionActual[1])== 6:
                carga =6
            print carga
            if len(solucion)>nivel:
                solucion[nivel] = posicionActual[0:2]
            else:
                solucion.append(posicionActual[0:2])


            if (limitacion>nivel) & (carga >0):
                hijos = self.getExpandibles(posicionActual, nivel+1, carga-1)

            if len(hijos)!=0:
                pila.extend(hijos)
                #print hijos
            #print pila


        if posicionActual[0:2]!=posicionMeta:
            solucion=[]


        #la solucion se filtra en el nivel de la meta
        print "solucion ",solucion[0:nivel+1]
        return solucion[0:nivel]

profund = Profundidad()