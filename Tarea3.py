#Ejercicio 5

# El tamaño del arreglo incluye la celda cero
def generarArregloIndexado(arreglo, tamaño):
    # Validación de parámetros
    if not isinstance(arreglo, list):
        print("Error: el arreglo no es una lista")
        return None
    if not isinstance(tamaño, int):
        print("Error: el tamaño no es un entero")
        return None
    if tamaño < len(arreglo):
        print("Error: el tamaño específicado es menor que el número de elementos del arreglo")
        return None
    #Generar arreglo
    Arr = [None for x in range(tamaño)]
    for n in arreglo:
        if not isinstance(n, int):
            print("Error: hay elementos no enteros en la lista")
            return None
        p = n%(tamaño)
        while True:
            if Arr[p] != None:
                p = (p+1)%(tamaño)
                continue
            else:
                Arr[p] = n
                break
    return Arr

def recuperarPosicionEnArreglo(arreglo, numero):
    # validación de parámetros
    if not isinstance(arreglo, list):
        print("Error: el arreglo no es una lista")
        return None
    if not isinstance(numero, int):
        print("Error: el numero no es un entero")
        return None
    tamaño = len(arreglo) - 1
    p = numero%(tamaño+1)
    # Búsqueda en base a modulo p
    while True:
        if arreglo[p] != numero:
            p = (p+1)%(tamaño+1)
            if (p == numero%(tamaño+1)) or (arreglo[p] == None):
                print("Error: el número no se encuentra en el arreglo")
                return 
            continue
        else:
            return p

#Ejercicio 6

def arregloPseudoaleatorio(m, a, c, s, size = 10):
    # validación de parámetros
    if not (isinstance(m, int) and isinstance(a, int) and isinstance(c, int) and isinstance(s, int) and isinstance(size, int)):
        print("Error: los parametros no son enteros")
        return 
    if not (2<=a and 2 < m and 0 <= c and c < m and 0 <= s and s < m):
        print("Error: los parámetros no cumplen las desigualdades requeridas")
        return
    # Generar elementos en el arreglo
    n = [0 for x in range(size)]
    for i in range(size):
        if i == 0:
            n[i] = s
        else:
            n[i] = (a * n[i-1] + c)%m
    return n


# Ejercicios de prueba

N = [15, 558, 32, 132, 102, 5, 257]
A1 = generarArregloIndexado(N, 11)
print(A1)
print(recuperarPosicionEnArreglo(A1, 257))
N = [103, 32, 11, 35, 43, 80, 9003, 0]
A1 = generarArregloIndexado(N, 14)
print(A1)
print(recuperarPosicionEnArreglo(A1, 80))
# Casos de excepciones
recuperarPosicionEnArreglo(A1, 256) # Número inexistente
generarArregloIndexado(N, 3) # tamaño menor al arreglo
generarArregloIndexado(N, "h") #parámetro no numérico
recuperarPosicionEnArreglo(A1, "")
N.append("hola") #añadir objeto no numérico
generarArregloIndexado(N, 11)


print(arregloPseudoaleatorio(133, 113, 43, 103))
print(arregloPseudoaleatorio(131, 2, 1, 15, 25)) # ajuste de tamaño del arreglo
#Casos de excepciones
arregloPseudoaleatorio(90, 113, 43, 103) # desigualdades incorrectas
arregloPseudoaleatorio(133, 113, 43, "") #parámetro no entero

