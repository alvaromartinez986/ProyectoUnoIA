class Profundidad:

	

	def __init__(self):
		buscarProfundidad()

	#posicion a expandir 
	#nivel de los nodos creados
	def getExpandibles(self, pos, nivel):
    	#abajo, derecha, izquierda, arriba
	    hijos =[]
	    #arriba
	    #si entrega -1 o 1, no existe la posicion o hay una pared respectivamente
	    if(abs(self.miAmbiente.getPosition(pos[0]-1,pos[1]))!=1):
	        hijos.append(pos[0]-1,pos[1], nivel)
	    #izquierda
	    if(abs(self.miAmbiente.getPosition(pos[0],pos[1]-1))!=1):
	        hijos.append(pos[0],pos[1]-1, nivel)
	    #derecha
	    if(abs(self.miAmbiente.getPosition(pos[0],pos[1]+1))!=1):
	        hijos.append(pos[0],pos[1]+1, nivel)
	    #abajo
	    if(abs(self.miAmbiente.getPosition(pos[0]+1,pos[1]))!=1):
	        hijos.append(pos[0]+1,pos[1], nivel)
	        
	    return hijos
    

	def buscarProfundidad(self):
	
	    nivel = 0
	
	    posicionActual = self.miAmbiente.posIniRobot().append(nivel)
	    posicionMeta = self.miAmbiente.posMeta()
	    
	    pila = [posicionActual]
	    
	    solucion = []
	    #abajo, derecha, izquierda, arriba
	    while (posicionActual[0:1]!=posicionMeta):
	        posicionActual = pila.pop()
	        nivel= posicionActual[2]
	        solucion[nivel] = posicionActual[0:1]
	        hijos = getExpandibles(posicionActual, nivel+1)
	        
	        if(len(hijos)!=0):
	            pila.extend(hijos)
	        
	        
	    #la solucion se filtra en el nivel de la meta
	    return solucion[0:nivel]

