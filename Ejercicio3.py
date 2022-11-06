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
        return "nombre{}, {} largo, {} tripulacion, {} pasajeros".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)

nave1=Nave("Halcón Milenario",200, 20, 75)
nave2=Nave("Estrella de la muerte", 150, 15, 60)
nave3=Nave("Luna llena", 100, 30, 200)
nave4= Nave("ATestrellas fugaces", 250, 80, 400)
nave5=Nave("PEqueñanave", 50, 2, 5)
nave6=Nave("Starwars", 50, 8, 20)





