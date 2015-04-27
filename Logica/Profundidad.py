from Ambiente import Ambiente
class Profundidad:

	

    def __init__(self):
		self.miAmbiente = Ambiente("archivo.txt")
		self.buscarProfundidad()

	#posicion a expandir 
	#nivel de los nodos creados
    def getExpandibles(self, pos, nivel):
    	#abajo, derecha, izquierda, arriba
		hijos =[]
	    #arriba
		print "arriba"
		print self.miAmbiente.getPosition(pos[0]-1,pos[1])
	    #si entrega -1 o 1, no existe la posicion o hay una pared respectivamente
		if(abs(self.miAmbiente.getPosition(pos[0]-1,pos[1]))!=1):
			hijos.append([pos[0]-1,pos[1], nivel])
		#izquierda
		print "izq"
		print self.miAmbiente.getPosition(pos[0],pos[1]-1)
		if(abs(self.miAmbiente.getPosition(pos[0],pos[1]-1))!=1):
			hijos.append([pos[0],pos[1]-1, nivel])
		#derecha
		print "der"
		print self.miAmbiente.getPosition(pos[0],pos[1]+1)
		if(abs(self.miAmbiente.getPosition(pos[0],pos[1]+1))!=1):
			hijos.append([pos[0],pos[1]+1, nivel])
		#abajo
		print "aba"
		print self.miAmbiente.getPosition(pos[0]+1,pos[1])
		if(abs(self.miAmbiente.getPosition(pos[0]+1,pos[1]))!=1):
			hijos.append([pos[0]+1,pos[1], nivel])

		return hijos
    

    def buscarProfundidad(self):

		nivel = 0

		posicionActual = self.miAmbiente.posIniRobotConNivel()
		posicionMeta = self.miAmbiente.posMeta()

		pila = [posicionActual]

		solucion = []
		#abajo, derecha, izquierda, arriba
		while (posicionActual[0:2]!=posicionMeta):
			posicionActual = pila.pop()
			nivel= posicionActual[2]
			print "posicionActual: "
			print posicionActual
			if (len(solucion)>nivel):
				solucion[nivel] = posicionActual[0:2]
			else:
				solucion.append(posicionActual[0:2])

			hijos = self.getExpandibles(posicionActual, nivel+1)

			if(len(hijos)!=0):
				pila.extend(hijos)
				print hijos

		#la solucion se filtra en el nivel de la meta
		print "solucion ",solucion 
		return solucion[0:nivel]

profund = Profundidad()
