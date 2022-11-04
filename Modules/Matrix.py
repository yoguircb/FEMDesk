import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QGridLayout, QMessageBox, QDialog
from PyQt5 import QtCore, Qt
from PyQt5 import QtGui
from dialogMatrix import *
import EF
from interfaz import Ui_Interfaz
from Modules.Dictionary.DMatrix import *
from Modules.Dictionary.DFiles import *
import Modules.ManageFiles.ManageFiles

class allNewMatrix():
        diffusionM = np.empty([1,1], dtype= 'U256')
        absorptionM = np.empty([1,1], dtype='U256')
        sourceM = np.empty(1, dtype='U256')
        massM = np.empty([1,1], dtype='U256')
        damMassM = np.empty([1,1], dtype='U256')
        cFluxM = np.empty([1,1], dtype='U256')
        convectionM = np.empty([1,1], dtype='U256')
        cSourceM = np.empty(1, dtype='U256')
        n = 1
#Clase para Crear la matrix de N dimensiones y darle las funciones para insertar, editar y eliminar datos en cada coordenada
class dialogMatrix(QDialog):
    def __init__(self, n):
        QDialog.__init__(self)
        self.ui = Ui_Matrix()
        self.ui.setupUi(self)
        self.setWindowTitle('Matriz ' + str(n) + 'x' + str(n))
        self.setMinimumSize(QtCore.QSize(500,500))
        self.setMaximumSize(QtCore.QSize(1000,700))
        self.setWindowFlags(QtCore.Qt.Popup)
        
        #Mandar a llamar la función n veces para poder crear la matriz
            #Rows
        for x in range(0, n):
            #Columns
            for y in range(0, n):
                self.createMatrix(x, y)

    """def mouseReleaseEvent(self, QEvent):
        if QApplication.widgetAt(QEvent.pos()) == self.fullWidget:
            self.close()"""

      #Función que genera la matriz de n dimensiones con sus caracteristicas
    def createMatrix(self, row, column):
        self.lineEdit = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents)
        self.lineEdit.setMinimumSize(QtCore.QSize(70, 70))
        #self.lineEdit.setMaximumSize(QtCore.QSize(300, 70))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit" + str(row + 1) + "X" + str(column + 1) + "Y")
        self.lineEdit.setEnabled(False)
        self.ui.gridLayout.addWidget(self.lineEdit, row, column, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
        self.ui.verticalLayout.addWidget(self.ui.scrollArea)


    #Función para mandar a llamar otra función que inserte los datos en una coordenada específico, además de marcar su casilla
    def marklineEdit(self, comb, comb1, n, arraylEdit, pos, diffusionComb):
        for x in range(0, n):
            for y in range(0, n):
                self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(x + 1) + "X" + str(y + 1) + "Y")
                self.cell.setStyleSheet("")
                self.namecell = self.cell.objectName()
                if self.namecell == ("lineEdit" + str(comb.currentIndex() + 1) + "X" + str(comb1.currentIndex() + 1) + "Y"):
                    self.cell.clear()

                    if pos == 1:
                        if diffusionComb.currentIndex() == 0:
                         #try:
                            ar = []
                            ar.append(float(arraylEdit[0][0].text()))
                            ar.append(float(arraylEdit[0][0].text()))
                            ar.append(float(arraylEdit[0][0].text()))
                            ar.append(float(arraylEdit[0][0].text()))
                            ar.append(diffusionComb.currentIndex())
                            allNewMatrix.diffusionM[x,y] = str(ar)
                            print(allNewMatrix.diffusionM)
                            self.insertMatrix(allNewMatrix.diffusionM)
                         #except Exception:
                            #QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                            #return
                        else:
                         try:
                                ar = []
                                ar.append(float(arraylEdit[0][1].text()))
                                ar.append(float(arraylEdit[0][2].text()))
                                ar.append(float(arraylEdit[0][3].text()))
                                ar.append(float(arraylEdit[0][4].text()))
                                ar.append(diffusionComb.currentIndex())
                                allNewMatrix.diffusionM[x,y] = str(ar)
                                print(allNewMatrix.diffusionM)
                                self.insertMatrix(allNewMatrix.diffusionM)
                         except Exception:
                                QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                                return

                    if pos == 2:
                      try:
                        data = float(arraylEdit[1][0].text())
                        allNewMatrix.absorptionM[x,y] = data
                        self.insertMatrix(allNewMatrix.absorptionM)
                      
                      except Exception:
                        QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                        return
                    if pos == 4:
                      try:
                        data = float(arraylEdit[3][0].text())
                        allNewMatrix.massM[x,y] = str(data)
                        self.insertMatrix(allNewMatrix.massM)
                      except Exception:
                        QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                        return
                    if pos == 5:
                      try:
                        data = float(arraylEdit[4][0].text())
                        allNewMatrix.damMassM[x,y] = str(data)
                        self.insertMatrix(allNewMatrix.damMassM)
                      except Exception:
                        QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                        return
                    if pos == 6:
                      try:
                        ar = []
                        ar.append(float(arraylEdit[5][0].text()))
                        ar.append(float(arraylEdit[5][1].text()))
                        allNewMatrix.cFluxM[x,y] = str(ar)
                        self.insertMatrix(allNewMatrix.cFluxM)
                      except Exception:
                        QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                        return
                    if pos == 7:
                      try:
                        ar = []
                        ar.append(float(arraylEdit[6][0].text()))
                        ar.append(float(arraylEdit[6][1].text()))
                        allNewMatrix.convectionM[x,y] = str(ar)
                        self.insertMatrix(allNewMatrix.convectionM)
                      except Exception:
                        QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                        return
        Modules.ManageFiles.ManageFiles.FileData.checkUpdateFile(self)
        QMessageBox.about(self, "Important message", "Información insertada con éxito")

  
    def showMeDiffusion(self, matrix):
        self.clearMatrix()
        for x in range(allNewMatrix.n):
            for y in range(allNewMatrix.n):
                self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(x + 1) + "X" + str(y + 1) + "Y")
                if matrix[x][y] == "None" or matrix[x][y] == '':
                 self.cell.clear()
                else:
                 arrMatrix = matrix[x][y]
                 arrMatrix = arrMatrix.replace(" ","")
                 arrMatrix = arrMatrix.strip('[]')
                 arrMatrix = arrMatrix.split(',')
                 floatMatrix = ['{0:g}'.format(float(i))  for i in arrMatrix]
                 floatMatrix = floatMatrix[:-1]
                 self.cell.insert(str(floatMatrix))

                 text = self.cell.text()
                 fm = QtGui.QFontMetrics(self.cell.font())
                 pixelsWide = fm.width(text)
                 self.cell.setFixedSize(QtCore.QSize(pixelsWide + 12, 70))
        self.showdialog()

                 
     #Función para limpiar la casilla especifica e insertarle los datos
    def insertMatrix(self, matrix):
        self.clearMatrix()
        for x in range(allNewMatrix.n):
            for y in range(allNewMatrix.n):
                self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(x + 1) + "X" + str(y + 1) + "Y")
                if matrix[x][y] != "None":
                 self.cell.insert(matrix[x][y])
                else:
                 self.cell.clear()

    #Función para mandar a llamar otra función que muestre la matriz de la sección seleccionada por el usuario
    def showMe(self, matrix):
        self.clearMatrix()
        for x in range(allNewMatrix.n):
            for y in range(allNewMatrix.n):
                self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(x + 1) + "X" + str(y + 1) + "Y")
                if matrix[x][y] != "None":
                 self.cell.insert(matrix[x][y])
                 text = self.cell.text()
                 fm = QtGui.QFontMetrics(self.cell.font())
                 pixelsWide = fm.width(text)
                 self.cell.setFixedSize(QtCore.QSize(pixelsWide + 12, 70))
                else:
                 self.cell.clear()
        self.showdialog()

    #Función que muestra una matriz
    def showdialog(self):
        self.show()

    #Función para limpiar todas los QLineEdit de la matrix a mostrar
    def clearMatrix(self):
        for row in range(allNewMatrix.n):
            for column in range(allNewMatrix.n):
             self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(row + 1) + "X" + str(column + 1) + "Y")
             self.cell.setStyleSheet("")
             self.cell.setFixedSize(QtCore.QSize(70, 70))
             self.cell.clear()  
    #Función para limpiar los datos de la matrix almacenada
    def clearMatrixData(self, matrix):
        dialog = QMessageBox.question(self, 'Importante', '¿Seguro que quieres reiniciar la matriz? Todos los datos se perderán', QMessageBox.Cancel | QMessageBox.Yes)
        if dialog == QMessageBox.Yes:
         matrix.fill('')
         Modules.ManageFiles.ManageFiles.FileData.checkUpdateFile(self)
        else:
            print("Operación Cancelada")


#Clase para Crear el vector de N dimensiones y darle las funciones para insertar, editar y eliminar datos en cada coordenada
class dialogVector(QDialog):
    def __init__(self, n):
        QDialog.__init__(self)
        self.ui = Ui_Matrix()
        self.ui.setupUi(self)
        self.setWindowTitle('Vector ' + str(n))
        #Rows
        for x in range(0, n):
            #Columns
                self.createVector(x)

    #Función que genera el vector de n dimensiones con sus caracteristicas
    def createVector(self, row):
        self.lineEdit = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents)
        self.lineEdit.setMinimumSize(QtCore.QSize(70, 70))
        self.lineEdit.setMaximumSize(QtCore.QSize(70, 70))
        self.lineEdit.setObjectName("lineEdit" + str(row + 1) + "X" + "1Y")
        self.lineEdit.setEnabled(False)
        self.ui.gridLayout.addWidget(self.lineEdit, row, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
        self.ui.verticalLayout.addWidget(self.ui.scrollArea)

    #Función para mandar a llamar otra función que inserte los datos en una coordenada específico, además de marcar su casilla
    def marklineEdit(self, comb, n, arraylEdit, pos):
        for x in range(0, n):
            self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(x + 1) + "X" + "1Y")
            self.cell.setStyleSheet("")
            self.namecell = self.cell.objectName()

            if self.namecell == ("lineEdit" + str(comb.currentIndex() + 1) + "X" + "1Y"):
                    self.cell.setStyleSheet("QLineEdit { background-color: yellow}")
                    self.cell.clear()

                    if pos == 3:
                     try:
                        self.cell.insert(float(arraylEdit[2][0].text()))
                        allNewMatrix.sourceM[x] = arraylEdit[2][0].text()
                        self.insertVector(allNewMatrix.sourceM)
                     except Exception:
                        QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                        return

                    if pos == 8:
                     try:
                        ar = []
                        ar.append(float(arraylEdit[7][0].text()))
                        ar.append(float(arraylEdit[7][1].text()))
                        self.cell.insert(str(ar))
                        allNewMatrix.cSourceM[x] = str(ar)
                        self.insertVector(allNewMatrix.cSourceM)
                     except Exception:
                        QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
                        return
        Modules.ManageFiles.ManageFiles.FileData.checkUpdateFile(self)
        QMessageBox.about(self, "Important message", "Información insertada con éxito")

     #Función para limpiar la casilla especifica e insertarle los datos
    def insertVector(self, matrix):
        self.clearVector()
        for x in range(allNewMatrix.n):
                self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(x + 1) + "X" + "1Y")
                if matrix[x] != "None":
                 self.cell.insert(matrix[x])
                else:
                 self.cell.clear()

    #Función para mandar a llamar otra función que muestre el vector de la sección seleccionada por el usuario
    def showMe(self, matrix):
        self.clearVector()
        for x in range(allNewMatrix.n):
                self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(x + 1) + "X" + "1Y")
                if matrix[x] != "None":
                 self.cell.insert('{0:g}'.format(float(matrix[x])))
                else:
                 self.cell.clear()
        self.showdialog()

    #Función que muestra un vector
    def showdialog(self):
        self.show()


    #Función para limpiar todas las casillas del vector
    def clearVector(self):
        for row in range(allNewMatrix.n):
             self.cell = self.findChild(QtWidgets.QLineEdit, "lineEdit" + str(row + 1) + "X" + "1Y")
             self.cell.setStyleSheet("")
             self.cell.clear()


#Clase para definir la dimension de las matrices encargadas de guardar la información en la memoria del programa
#Estas matrices sirven como un intermediario para intercambiar información entre el programa y los archivos EXCEL
class Matrix():
 def newMatrix(self):
    dialog = QMessageBox.question(self, 'Importante', '¿Seguro que quieres cambiar el numero de variables dependientes? Harán cambios en todas las matrices', QMessageBox.Cancel | QMessageBox.Yes)
    if dialog == QMessageBox.Yes:
     try:
        n = int(self.inputDepedentVarial.text())
        if n == '':
            n = 1
        self.dMatrix = dialogMatrix(n)
        self.dVector = dialogVector(n)
        initialValues["noVariables"] = n
        allNewMatrix.diffusionM = np.empty([n,n], dtype='U256')
        allNewMatrix.absorptionM = np.empty([n,n], dtype='U256')
        allNewMatrix.sourceM = np.empty(n, dtype='U256')
        allNewMatrix.massM = np.empty([n,n], dtype='U256')
        allNewMatrix.damMassM = np.empty([n,n], dtype='U256')
        allNewMatrix.cFluxM = np.empty([n,n], dtype='U256')
        allNewMatrix.convectionM = np.empty([n,n], dtype='U256')
        allNewMatrix.cSourceM = np.empty(n, dtype='U256')
        allNewMatrix.n = n

        #Actualizar el combobox según el numero de variables dependientes
        for index, item in enumerate(self.CoefficientCheckBoxArray):
                for j, item in enumerate(self.arrayCmbRowColumns[index]):
                        self.arrayCmbRowColumns[index][j].clear()

                for j, item in enumerate(self.arrayCmbRowColumns[index]):
                    for i in range(1, n + 1):
                        self.arrayCmbRowColumns[index][j].addItem(str(i))
        self.cmbInitialValues.clear()

        for i in range(1, n + 1):
            self.cmbInitialValues.addItem("u" + str(i))

        Modules.ManageFiles.ManageFiles.FileData.checkUpdateFile(self)

     except Exception:
            QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
            return

    else:
        print("Operacion Cancelada")

 def resetMatrix(self):
    dialog = QMessageBox.question(self, 'Importante', '¿Seguro que quieres reiniciar el numero de variables dependientes? Esto reiniciará todas las matrices', QMessageBox.Cancel | QMessageBox.Yes)
    if dialog == QMessageBox.Yes:
        n = 1
        self.dMatrix = dialogMatrix(n)
        self.dVector = dialogVector(n)
        initialValues["noVariables"] = n
        allNewMatrix.diffusionM = np.empty([n,n], dtype='U256')
        allNewMatrix.absorptionM = np.empty([n,n], dtype='U256')
        allNewMatrix.sourceM = np.empty(n, dtype='U256')
        allNewMatrix.massM = np.empty([n,n], dtype='U256')
        allNewMatrix.damMassM = np.empty([n,n], dtype='U256')
        allNewMatrix.cFluxM = np.empty([n,n], dtype='U256')
        allNewMatrix.convectionM = np.empty([n,n], dtype='U256')
        allNewMatrix.cSourceM = np.empty(n, dtype='U256')
        allNewMatrix.n = n
        print("Imprimir matriz diffusion")
        print(allNewMatrix.diffusionM)
        print("Imprimir matriz absorption")
        print(allNewMatrix.absorptionM)

        Matrix.currentInitialVariable(self)
        
        #Actualizar el combobox según el numero de variables dependientes
        for index, item in enumerate(self.CoefficientCheckBoxArray):
                for j, item in enumerate(self.arrayCmbRowColumns[index]):
                        self.arrayCmbRowColumns[index][j].clear()

                for j, item in enumerate(self.arrayCmbRowColumns[index]):
                    for i in range(1, n + 1):
                        self.arrayCmbRowColumns[index][j].addItem(str(i))
        self.cmbInitialValues.clear()

        for i in range(1, n + 1):
            self.cmbInitialValues.addItem("u" + str(i))

        Modules.ManageFiles.ManageFiles.FileData.checkUpdateFile(self)

    else:
        print("Operacion Cancelada")

 def currentInitialVariable(self):
        noVar = "{}".format(allNewMatrix.n)
        self.inputDepedentVarial.setText(noVar)

