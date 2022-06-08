'''
1 - Crear una clase de cálculo con un constructor predeterminado (sin parámetros) que permita realizar
varios cálculos en números enteros.
2 - Crear un método llamado Factorial() que permita calcular el factorial de un entero. Pruebe el método
instanciando la clase.
3 - Crear un método llamado Suma() que permita calcular la suma de los primeros n enteros 1 + 2 + 3 + ..
+ n. Pruebe este método.
4 - Cree un método llamado testPrimo() en la clase cálculo para probar la primalidad de un entero dado.
Pruebe este método.
4 - Crear un método llamado testPrimos() que permita probar si dos números son primos entre ellos.
5 - Cree un método tableMult() que cree y muestre la tabla de multiplicar de un entero dado. Luego cree
un método TablaMultiplicar() para mostrar todas las tablas de multiplicar de enteros 1, 2, 3, ..., 9.
6 - Cree un método estático listDiv() que obtenga todos los divisores de un entero dado en una nueva
lista llamada Ldiv. Cree otro método listDivPrim() que obtenga todos los divisores primos de un entero
dado.
'''

class Calculo():
    """
    Una clase que realiza varia operaciones matematicas
    haciendo uso de los metodos de factorial , sumatoria, entre otros.
    ...
    Atributos
    ----------
    Metodos
    -------
    _init_(self, nombre, salario, proyecto):
        Construye todos los atributos necesarios para el objeto PersonalAcademico.
    Factorial(n):

    Suma(n):

    testPrimo(n):

    testPrimos():

    tableMult(n):
    
    TablaMultiplicar():

    listDiv():

    listDivPrim():
    
    """
     
    def __init__(self):
        ''' 
        Construye todos los atributos necesarios para el objeto Empleado.
        
        Parametros
        ----------
        '''
        
    def Factorial(n):
        if n == 0:
            return 1
        prod = 1
        for i in range(1, n+1):
            prod = prod * i
        return prod
    
    def Suma(n):
        for i in range(n,0,-1):
            prod = prod + i
        return prod

    def testPrimo(n):
        for i in range(2, n):
            if n % i == 0:
                print("No es primo", i, "es divisor")
                return False
        print("Es primo")
        return True

    def testPrimos():
        ''''''

    def tableMult(n):
        for i in range(1, 12):
        producto=n*i
        print(n,"*",i,"=",producto)
        
    def TablaMultiplicar():
        for i in range(1, 12):
            for j in range(1, 12):
                producto=j*i
            print(j,"*",i,"=",producto)
        print("")

    def listDiv():
        ''''''

    def listDivPrim():
        ''''''

operaciones = Calculo()









