#Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, 
# tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

 #realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;

#mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
#determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
#indicar cuál es la nave que requiere mayor cantidad de tripulación;
#mostrar todas las naves que comienzan con AT;
#listar todas las naves que pueden llevar seis o más pasajeros;
# mostrar toda la información de la nave más pequeña y la más grande


class Nave:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre=nombre
        self.largo=largo
        self.tripulacion=tripulacion
        self.pasajeros=pasajeros
    def __str__(self):
        return "EL nombre de la nave es:{}, mide {} de largo, tiene: {} tripulacion, tiene: {} pasajeros".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)

nave1=Nave("Halcón Milenario",200, 20, 75)
nave2=Nave("Estrella de la muerte", 150, 15, 60)
nave3=Nave("Luna llena", 100, 30, 200)
nave4= Nave("ATestrellas fugaces", 250, 80, 400)
nave5=Nave("PEqueñanave", 50, 2, 5)
nave6=Nave("Starwars", 50, 8, 20)


print("La información del Halcón Milenario es:", nave1)
print("La información de la Estrella de la Muerte es:", nave2)

lista_nave=[]
lista_nave.append(nave1)
lista_nave.append(nave2)
lista_nave.append(nave3)
lista_nave.append(nave4)
lista_nave.append(nave5)
lista_nave.append(nave6)


def nombre (lista_nave):
    lista_AT=[]
    for n in lista_nave:
        nombre=n.nombre
        if nombre[:2]=="AT":
            lista_AT.append(n)
    for i in lista_AT:
        print("La nave que comienza con AT:", i)
nombre(lista_nave)   


def nave_grande(lista_nave, tamaño=250):
    if tamaño ==-1:
        for n in lista_nave:
            print("La clase es:", type(n).__name__)
            print("Los atributos:", n)
    else:
        g_tamaño=[]
        for i in lista_nave:
            tamaño_r=i.largo
            if tamaño_r==tamaño:
                g_tamaño.append(i)
        print("Se han encontrado {} nave con {} de largo, que es la más grande".format(len(g_tamaño), tamaño))
        for r in g_tamaño:
            print(r)

nave_grande(lista_nave)        
def nave_pequeña(lista_nave, tamaño=50):
    if tamaño ==-1:
        for n in lista_nave:
            print("La clase es:", type(n).__name__)
            print("Los atributos:", n)
    else:
        g_tamaño=[]
        for i in lista_nave:
            tamaño_r=i.largo
            if tamaño_r==tamaño:
                g_tamaño.append(i)
        print("Se han encontrado {} nave con {} de largo, que son las más pequeñas".format(len(g_tamaño), tamaño))
        for r in g_tamaño:
            print(r)

nave_pequeña(lista_nave) 

def num_tripulacion(lista_nave, cant_trip=80):
    if cant_trip ==-1:
        for n in lista_nave:
            print("La clase es:", type(n).__name__)
            print("Los atributos:", n)
    else:
        c_tripul=[]
        for i in lista_nave:
            e_tripul=i.tripulacion
            if e_tripul==cant_trip:
                c_tripul.append(i)
        print("Se han encontrado {} naves con {} tripulantes, que es la que más tripulantes requiere".format(len(c_tripul), cant_trip))
        for c in c_tripul:
            print(c)

num_tripulacion(lista_nave)        



