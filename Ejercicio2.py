#Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma iterativa
matriz=[]
def creamatriz(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz        

    
def det(n):
    sarrus=((n[0][0]*n[1][1]*n[2][2])+(n[0][1]*n[1][2]*n[2][0])+(n[0][2]*n[1][0]*n[2][1])-(n[2][0]*n[1][1]*n[0][2])+(n[2][1]*n[1][2]*n[0][0])+(n[2][2]*n[1][0]*n[0][1]))
   
    return sarrus

n=int(input("Matriz:"))

det(n)
