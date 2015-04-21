__author__ = 'alvaro'


class Ambiente:


    global tamano
    global matriz

    def __init__(self, ruta):
        global tamano
        global matriz
        print 'hola'
        archi=open(ruta,'r')
        linea = archi.readline()
        tamano= int(linea)
        matriz = [[0 for x in range(tamano)] for x in range(tamano)]
        print linea
        for i in range(0, tamano):
            linea=archi.readline()
            splitLinea = linea.split(' ')
            print(splitLinea)
            for j in range(0, tamano):
                matriz[i][j]= splitLinea[j]
        archi.close()



    def getPosition(self, x, y):
        '''
         Metodo para retornar el valor del ambiente en la posicion x , y
         x valor de la fila del ambiente
         y valor de la columna del ambiente
        '''
        global tamano
        global matriz
        if(x<0):
            return -1
        if(y<0):
            return -1
        if(x>tamano):
            return -1
        if (y>tamano):
            return -1
        else:
            return matriz[x][y]



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



