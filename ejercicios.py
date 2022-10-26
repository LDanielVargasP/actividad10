def max(num1, num2):
    if num1 > num2:
        r = num1
    else:
        r = num2
    print("max -> " + str(r))

def max_de_tres(num1,num2,num3):
    arr = [num1,num2,num3]
    inter = True
    while inter:
        inter = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                inter=True
    print("max de tres -> " + str(arr[2]))

def longitud(cadena):
    r = 0
    for x in cadena:
        r += 1
    print("longitud -> " + str(r))

def es_vocal(v):
    v = v.lower()
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
        print("vocal -> " + 'True')
    else:
        print("vocal -> " + 'False')

def sum(lista):
    r = 0
    for x in lista:
        r += x
    print("suma de la lista es -> " + str(r))

def multi(lista):
    r = 1
    for x in lista:
        r *= x
    print("los valores multiplicados son -> " + str(r))

def inversa(cadena):
    r = ''
    for x in cadena[::-1]:
        r += x
    print("inversa -> " + r) 

def es_palindromo(cadena):
    cadena = cadena.lower()
    r = ''
    for x in cadena[::-1]:
        r += x
    if cadena == r:
        print("palindromo -> " + 'true')
    else:
        print("palindormo -> " + 'false')


def superposicion(lista1, lista2):
    for x in lista1:
        for y in lista2:
            if x == y:
                print("superposicion -> " + 'true')
                break

def generar_n_caracteres(cant, caracter):
    r = caracter * cant
    print("generar n caracteres -> " + r)

if __name__=='__main__':
    max(8,8)
    max_de_tres(2,7,10)
    longitud("palindromo")
    es_vocal('a')
    sum([1,2,3,4,5])
    multi([1,2,3,4,5])
    inversa("madres")
    es_palindromo("radar")
    superposicion([1,2,3,4,5],[6,7,1,9,0])
    generar_n_caracteres(5,'x')