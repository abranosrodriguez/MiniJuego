# This is a sample Python script.
import eventos
from Interfaz.mainWindow import *
from Interfaz.datosHeroe import *
from Interfaz.datosEnemigo import *
import classEnemigo
import classHeroe
import var, sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_mainWindow()
        var.ui.setupUi(self) #encargado de generar la interfaz
        var.datosHeroe = DatosHeroe()
        var.datosEnemigo = DatosEnemigo()
        #Zona de eventos
        var.ui.btnDatosHeroe.clicked.connect(eventos.Eventos.datosHeroe)
        var.ui.btnDatosEnemigo.clicked.connect(eventos.Eventos.datosEnemigo)

class DatosHeroe(QtWidgets.QDialog):
    def __init__(self):
        super(DatosHeroe,self).__init__()
        var.datosHeroe = Ui_dlgDatosHeroe()
        var.datosHeroe.setupUi(self)

        #Create de data of the hero
        heroe = classHeroe.Heroe('adri', 10, 5)
        #Put the values on the hero interface
        var.datosHeroe.lblNombreHeroe.setText(heroe.nombre)
        var.datosHeroe.lblVidaHeroe.setText(str(heroe.vida))
        var.datosHeroe.lblAtaqueHeroe.setText(str(heroe.ataque))

class DatosEnemigo(QtWidgets.QDialog):
    def __init__(self):
        super(DatosEnemigo,self).__init__()
        var.datosEnemigo = Ui_dlgDatosEnemigo()
        var.datosEnemigo.setupUi(self)
        enemigo = classEnemigo.Enemigo('esqueleto', 5, 2)
        print("Nombre:", enemigo.nombre, "Vida:", enemigo.vida, "Ataque:", enemigo.ataque)
        var.datosEnemigo.lblNombreEnemigo.setText(enemigo.nombre)
        var.datosEnemigo.lblVidaEnemigo.setText(str(enemigo.vida))
        var.datosEnemigo.lblAtaqueEnemigo.setText(str(enemigo.ataque))



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
