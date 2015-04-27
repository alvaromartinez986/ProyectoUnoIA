__author__ = 'alvaro'


class Ambiente:

   
    def __init__(self, ruta):

        self.initPos = []
        self.metaPos = []
        archi=open(ruta,'r')
        linea = archi.readline()
        self.tamano= int(linea)
        self.matriz = [[0 for x in range(self.tamano)] for x in range(self.tamano)]
        print linea
        for i in range(0, self.tamano):
            linea=archi.readline()
            splitLinea = linea.split(' ')
            print(splitLinea)
            for j in range(0, self.tamano):
                self.matriz[i][j]= int(splitLinea[j])
		if((int(splitLinea[j]))==0):
			self.initPos.append(0)
			self.initPos.append(i)
			self.initPos.append(j)
			self.initPos.append('')
		if((int(splitLinea[j]))==7):
			self.metaPos.append(i)
			self.metaPos.append(j)
			
        archi.close()

    def posIniRobotConNivel(self):
		return self.initPos[:3]

    def posIniRobotConCosto(self):
		return self.initPos

    def posMeta(self):
		return self.metaPos


    def getPosition(self, x, y):
        '''
         Metodo para retornar el valor del ambiente en la posicion x , y
         x valor de la fila del ambiente
         y valor de la columna del ambiente
        '''
        if(x<0):
            return -1
        if(y<0):
            return -1
        if(x>self.tamano-1):
            return -1
        if (y>self.tamano-1):
            return -1
        else:
            return self.matriz[x][y]

    def getCosto(self, x, y):
	'''
         Metodo para retornar el costo del ambiente en la posicion x , y
         x valor de la fila del ambiente
         y valor de la columna del ambiente
        '''
	if(self.getPosition(x, y)==2):
	    return 1
        elif(self.getPosition(x,y)==3):
	    return 3
	elif(self.getPosition(x,y)==4):
	    return 4
	elif(self.getPosition(x, y)==5):
	    return 6
	elif(self.getPosition(x, y)==6):
	    return 5
	else:
	    return 0



'''
Prueba de lectura de archivo
print 'hola'
miAmb = Ambiente('archivo.txt')
'''
'''
Prueba de getPosition
miAmb = Ambiente('archivo.txt')
print miAmb.getPosition(-1, 1)
print miAmb.getPosition(3,3)
'''



