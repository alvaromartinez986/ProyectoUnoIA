__author__ = 'alvaro'


class Ambiente:


   
    def __init__(self, ruta):

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
                self.matriz[i][j]= splitLinea[j]
		if((int(splitLinea[j]))==0):
			self.initPos =[i, j]
		if((int(splitLinea[j]))==7):
			self.metaPos = [i, j]
			
        archi.close()

    def posIniRobot(self):
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
        if(x>self.tamano):
            return -1
        if (y>self.tamano):
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



