#En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una plataforma de bronce 
#sobre la cual había tres agujas de diamante. En la primera aguja estaban apilados setenta y cuatro discos de oro,
#cada una ligeramente menor que la que estaba debajo. A los sacerdotes se les encomendó la tarea de pasarlos todos desde 
# la primera aguja a la tercera, con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse 
# encima de otro más pequeño. Se dijo a los sacerdotes que, cuando hubieran terminado de mover los discos, llegaría el fin del mundo.
#  Resolver este problema de la Torre de Hanói.

class nodoCola(object):
    info, sig = None, None

class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamano=0
    def arribo(cola, dato):
        nodo=nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente=nodo
        else:
            cola.final.sig=nodo
        cola.final=nodo
        cola.tamano += 1

    def atencion(cola):
        dato=cola.frente.info
        cola.frente =cola.frente.sig
        if cola.frente is None:
            cola.final=None
        cola.tamano -= 1
        return dato
        
                

