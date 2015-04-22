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
			self.initPos.append(i)
			self.initPos.append(j)
			self.initPos.append(0)
			self.initPos.append(0)
		if((int(splitLinea[j]))==7):
			self.metaPos.append(i)
			self.metaPos.append(j)
			
        archi.close()

    def posIniRobotConNivel(self):
		return self.initPos[:2]

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



