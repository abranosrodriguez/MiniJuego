# Form implementation generated from reading ui file 'datosHeroe.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgDatosHeroe(object):
    def setupUi(self, dlgDatosHeroe):
        dlgDatosHeroe.setObjectName("dlgDatosHeroe")
        dlgDatosHeroe.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dlgDatosHeroe.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=dlgDatosHeroe)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 90, 181, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblNombreHeroe = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lblNombreHeroe.setObjectName("lblNombreHeroe")
        self.verticalLayout_3.addWidget(self.lblNombreHeroe)
        self.lblVidaHeroe = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lblVidaHeroe.setObjectName("lblVidaHeroe")
        self.verticalLayout_3.addWidget(self.lblVidaHeroe)
        self.lblAtaqueHeroe = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lblAtaqueHeroe.setObjectName("lblAtaqueHeroe")
        self.verticalLayout_3.addWidget(self.lblAtaqueHeroe)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtNombreHeroe = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.txtNombreHeroe.setObjectName("txtNombreHeroe")
        self.verticalLayout_2.addWidget(self.txtNombreHeroe)
        self.txtVidaHeroe = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.txtVidaHeroe.setObjectName("txtVidaHeroe")
        self.verticalLayout_2.addWidget(self.txtVidaHeroe)
        self.txtAtaqueHeroe = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.txtAtaqueHeroe.setEnabled(True)
        self.txtAtaqueHeroe.setObjectName("txtAtaqueHeroe")
        self.verticalLayout_2.addWidget(self.txtAtaqueHeroe)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(dlgDatosHeroe)
        QtCore.QMetaObject.connectSlotsByName(dlgDatosHeroe)

    def retranslateUi(self, dlgDatosHeroe):
        _translate = QtCore.QCoreApplication.translate
        dlgDatosHeroe.setWindowTitle(_translate("dlgDatosHeroe", "Dialog"))
        self.lblNombreHeroe.setText(_translate("dlgDatosHeroe", "TextLabel"))
        self.lblVidaHeroe.setText(_translate("dlgDatosHeroe", "TextLabel"))
        self.lblAtaqueHeroe.setText(_translate("dlgDatosHeroe", "TextLabel"))
        self.txtNombreHeroe.setText(_translate("dlgDatosHeroe", "Nombre:"))
        self.txtVidaHeroe.setText(_translate("dlgDatosHeroe", "Vida:"))
        self.txtAtaqueHeroe.setText(_translate("dlgDatosHeroe", "Ataque:"))