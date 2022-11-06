#Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma iterativa
matriz=[]
def creamatriz(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz

def multiplicar(n):
    n1= int(n[0][0]*n[1][1]*n[2][2])
    n2= int(n[1][0]*n[2][1]*n[0][2])
    n3= int(n[2][0]*n[0][1]*n[1][2])   
    ntotal=n1+n2+n3
    return ntotal

def invers(n):
    inversa=[]
    for i in n:
        t=i[::-1]
        inversa.append(t)
    return inversa

def det(n):
    matriz=creamatriz(n)
    matinvers=invers(matriz)
    determinante=multiplicar(matriz) - multiplicar(matinvers)     
    return determinante

n=[3,5,8]
det(n)    


