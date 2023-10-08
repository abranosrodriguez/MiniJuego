import var, sys
import classHeroe

class Eventos():
    def datosHeroe(self):
        try:
            var.datosHeroe.show()
        except Exception as error:
            print("Error al mostrar los datos del heroe", error)
    def datosEnemigo(self):
        try:
            var.datosEnemigo.show()
        except Exception as error:
            print("Error al mostrar los datos del enemigo", error)
