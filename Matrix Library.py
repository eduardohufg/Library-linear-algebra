#Eduardo Chavez Martin A01799595


class Matriz:
    """Instancias de esta clase representan una matriz matemática
    con un cierto número de renglones y columnas.
    """
    
    def __init__(self, inicial):
        """Inicializa una instancia de esta clase con un valor inicial,
        el cual debe ser una lista de listas del mismo tamaño y que 
        contienen números que corresponden a los elementos de la matriz.
        """
        self.__info = inicial
        self.__renglones = len(inicial)
        self.__columnas = len(inicial[0])
        
    @classmethod
    def ceros(cls, renglones, columnas):
        """Método de clase que crea una nueva instancia del tamaño
        establecido por sus argumentos y que contiene solamente ceros.
        """
        return Matriz([[0 for j in range(columnas)]
                       for i in range(renglones)])
    
    @classmethod
    def identidad(cls, dimension):
        """Metodo de clase que crea una nueva matriz identidad de la
        dimension especificada."""
        identidad = Matriz.ceros(dimension, dimension)
        for i in range(dimension):
            identidad[i, i] = 1
        return identidad
    
    @property
    def renglones(self):
        """Propiedad que devuelve el número de renglones de esta 
        matriz.
        """
        return self.__renglones
    
    @property
    def columnas(self):
        """Propiedad que devuelve el número de columnas de esta 
        matriz.
        """
        return self.__columnas
    @property
    def getmatriz(self):
        """regresa la matriz"""
        return self.__info

    
    def __getitem__(self, indices):
        """Devuelve el elemento de esta matriz indicado por indices, el
        cual debe ser una tupla con el renglón y la columna deseada.
        """
        renglon, columna = indices
        return self.__info[renglon][columna]    
    
    def __setitem__(self, indices, valor):
        """Establece valor como el nuevo elemento de esta matriz en indices, 
        el cual debe ser una tupla con el renglón y la columna deseada.
        """
        renglon, columna = indices
        self.__info[renglon][columna] = valor

    def __str__(self):
        """Devuelve una cadena con la representación informal de esta 
        matriz.
        """
        nums_como_cadenas = [str(n) for n in sum(self.__info, [])]
        nums_como_cadenas.sort(key=len, reverse=True)
        tam_max = len(nums_como_cadenas[0])
        return '\n'.join([' '.join([f'{n:{tam_max}}' for n in renglon])
                         for renglon in self.__info]) + '\n'
    
    def __repr__(self):
        """Devuelve una cadena con la representación formal de esta matriz,
        usando el formato: 'Matriz(lista_de_listas)'
        """
        return f'Matriz({self.__info})'

    def __eq__(self, otro):
        """Devuelve True si esta matriz es igual a otro, elemento por 
        elemento, o False en caso contrario.
        """
        if self.renglones == otro.renglones and self.columnas == otro.columnas:
            for i in range(self.renglones):
                for j in range(self.columnas):
                    if self[i, j] != otro[i, j]:
                        return False
            return True
        else:
            return False
        
        
    def transpuesta(self):
        """Devuelve el resultado de transponer esta matriz."""
        matriz = []
        for i in range(self.columnas):
            matriz.append([])
            for n in range(self.renglones):
                matriz[i].append(self[n,i])
        return Matriz(matriz)
        
    
    def diagonal(self):
        """Devuelve un vector con la diagonal de esta matriz."""
        diagonal = []
        if self.renglones >= self.columnas:
            a = self.columnas
        else: 
            a = self.renglones
    
        for i in range(a):
            diagonal.append(self[i,i])
        return diagonal
        
    
    def es_cuadrada(self):
        """Devuelve verdadero si la matriz es cuadrada"""
        if self.renglones ==self.columnas:
            return True
        else:
            return False
        
        
    def es_triangular_superior(self):
        """Devuelve verdadero si la matriz es triangular superior"""
    
        return True
    
        for i in range(self.renglones-1):
            for n in range(i+1):
                if self[i+1,n] == 0:
                    continue
                else:
                    return False
        return True
        
        
    def es_triangular_inferior(self):
        """Devuelve verdadero si la matriz es triangular inferior"""
        for i in range(self.columnas-1):
            for n in range(i+1):
                if self[n,i+1] == 0:
                    continue
                else:
                    return False
                
    def __mul__(self, escalar):
        """Devuelve el resultado de multiplicar cada elemento de esta 
        matriz por escalar.
        """
        matriz = []
        for i in range(self.renglones):
            m =[]
            for n in range(self.columnas):
                m.append(self[i,n]*escalar)
            matriz.append(m)
        return Matriz(matriz)
    
    def __truediv__(self, escalar):
        """Devuelve el resultado de dividir cada elemento de esta
        matriz entre escalar."""
        
        matriz = []
        for i in range(self.renglones):
            m =[]
            for n in range(self.columnas):
                m.append(self[i,n]/escalar)
            matriz.append(m)
        return Matriz(matriz)
        
    def __neg__(self):
        """Devuelve el resultado de cambiar de signo cada elemento de
        esta matriz.
        """
        matriz = []
        for i in range(self.renglones):
            m =[]
            for n in range(self.columnas):
                m.append(self[i,n]*-1)
            matriz.append(m)
        return Matriz(matriz)
        
         
    def __add__(self, otro):
        """Devuele el resultado de sumar esta matriz más otro."""
        if self.renglones == otro.renglones and self.columnas == otro.columnas:
            suma = Matriz.ceros(self.renglones, self.columnas)
            for i in range(suma.renglones):
                for j in range(suma.columnas):
                    suma[i, j] = self[i,j] + otro[i,j]
            return suma
        
    
    def __sub__(self, otro):
        """Devuele el resultado de restar esta matriz menos otro."""
        if self.renglones == otro.renglones and self.columnas == otro.columnas:
            matriz = []
            for i in range(self.renglones):
                r = []
                for n in range(self.columnas):
                    r.append(self[i,n] - otro[i,n])
                matriz.append(r)
            return Matriz(matriz)
        else:
            return "no se puede"
            
    
    def __matmul__(self, otro):
        """Devuele el resultado del producto de esta matriz multiplicada
        por otro."""
        if self.columnas == otro.renglones:
            matriz = Matriz.ceros(self.renglones, otro.columnas)
            for i in range(self.renglones):
                for j in range(otro.columnas):
                    for n in range(otro.renglones):
                        matriz[i,j] = matriz[i,j] + self[i,n] * otro[n,j]
            return matriz
 
    
    def menor_asociado(self, renglon, columna):
        """Regresa una nueva matriz resultante de eliminar
        el renglon y la columna."""
        
        matrizn = []
        for n in range(self.renglones):
            r =[]
            for i in range(self.columnas):
                r.append(self[n,i])
            matrizn.append(r)
            
        for n in range(self.columnas):
            matrizn[n].pop(columna)
        matrizn.pop(renglon)
        
        return Matriz(matrizn)
        
        #primer intento
        """
        matrizn = []
        matriz = []
        for n in range(self.renglones):
            r =[]
            for i in range(self.columnas):
                r.append(self[n,i])
            matrizn.append(r)
        for i in range(self.renglones):
            matrizn[renglon][i] = 0
        for n in range(self.columnas):
            matrizn[n][columna] = 0
        for i in range(self.renglones):
            k = []
            for n in range(self.columnas):
                if matrizn[i][n] != 0: 
                    k.append(matrizn[i][n])
                else:
                    continue
            matriz.append(k)
        for i in range(len(matriz)-1):
            if len(matriz[i]) == 0:
                matriz.pop(i)
            else:
                continue
        n = matriz[0:len(matrizn)-1]
        return n
        """
    
    def determinante(self):
        """Calcula el valor del determinante de la matriz."""
        #Lo hice por el metodo de gauss, se me hizo mas facil
        matrizn = []
        for q in range(self.renglones):
            r =[]
            for w in range(self.columnas):
                r.append(self[q,w])
            matrizn.append(r)
        
        for i in range(len(matrizn)-1):
            for n in range(i+1, len(matrizn)):
                x = matrizn[n][i]/matrizn[i][i]
                for r in range(i, len(matrizn)):
                    matrizn[n][r] -= matrizn[i][r]*x
        a = 1
        for l in range(len(matrizn)):
            a = a * matrizn[l][l]
        return a
        
        
        #intento con el metodo de euler
        """
        for i in range(self.renglones-1):
            for n in range(i+1):
                if self[i+1,n] == 0:
                    continue
                else:
                    return False
        return True
        """
        
        """
        matrizn = []
        for n in range(self.renglones):
            r =[]
            for i in range(self.columnas):
                r.append(self[n,i])
            matrizn.append(r) 
        
        m = Matriz(matrizn)
        det= 0
        cont = 1
        for i in range(len(matrizn)):
            a = m.menor_asociado(i,0)
            p = Matriz(a)
            det = det + cont * matrizn[i][0] * p.determinante()
        return det
        
        """
        
    def adjunta(self):
        """Regresa la matriz adjunta."""
        mult = 1
        acum = 0
        matrizn = []
        for n in range(self.renglones):
            r =[]
            for i in range(self.columnas):
                r.append(self[n,i])
            matrizn.append(r)
             
        mat = Matriz.ceros(len(matrizn),len(matrizn))
        #matr = []
        for i in range(len(matrizn)):
            #r = []
            for n in range(len(matrizn)):
                x = Matriz(matrizn)
                y = x.menor_asociado(i,n)
                z = y.determinante()
                mat[i, n] = z * mult
                mult = mult*-1
                #r.append(z)
            #matr.append(r)
        return mat
        #return matr
    
            
        

    def inversa(self):
        """Regresa la matriz inversa."""
        m = Matriz(self.__info)
        a = m.adjunta()
        c = a.transpuesta()
        x = Matriz(self.__info)
        d = x.determinante()
        result = c.__truediv__(d)
        return result
        
        
        
        
    
    def es_simetrica(self):
        """Regresa verdadero si la matriz es simetrica."""
        m = Matriz(self.__info)
        if self.__info == m.transpuesta():
            return True
        else:
            return False
    
    def es_antisimetrica(self):
        """Regresa verdadero si la matriz es antisimetrica."""
        m = Matriz(self.__info)
        if m.transpuesta()== m.__neg__():
            return True
        else:
            return False
    
        

"""
A1 = Matriz([[3,-1,4,2]])
B1 = Matriz([[6,0,-1,4]])
C1 = Matriz([[-2,3,1,5]])

print("1a) A+C = ", A1+C1)
print("1b) -2B = ", B1*-2)
print("1c) C-B-2A = ", C1-B1-A1*2)


A2 = Matriz([[1,-1,2],[3,4,5],[0,1,-1]])
B2 = Matriz([[0,2,1],[3,0,5],[7,-6,0]])
C2 = Matriz([[0,0,2],[3,1,0],[0,-2,4]])

print("2a) A-2B =", A2 - B2*2, sep='\n')
print("2b) 4C-2B+3A =", C2*4-B2*2+A2*3, sep='\n')
print("2c) C-A-B =", C2-A2-B2, sep='\n')
print("2d) 3A-C =", A2*3-C2, sep='\n')


A3 = Matriz([[1],[-2],[4]])
B3 = Matriz([[0],[-3.],[-7]])
C3 = Matriz([[4],[-1],[5]])
D3 = Matriz([[6,0,-5],[6,2,7]])

print("3a) (2A).(3B) =", (A3*2).transpuesta()@(B3*3))
print("3b) (A-C).(3B-4A) =", (A3-C3).transpuesta()@(B3*3-A3*4))
print("3c) D(3A-5B+C) =", D3@(A3*3-B3*5+C3), sep='\n')



A4 = Matriz([[2,4,6],[4,5,6],[3,1,-2]])

print("4a) Inversa de A =", A4.inversa(), sep='\n')
print("4b) A^-1A =", A4.inversa()@A4, sep='\n')
print("4c) AA^-1 =", A4@A4.inversa(), sep='\n')
"""
