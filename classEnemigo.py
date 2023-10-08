import classPersonaje

class Enemigo(classPersonaje.Personaje):
    def __init__(self,nombre,vida,ataque):
        super().__init__(nombre,vida,ataque)