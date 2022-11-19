from PyQt5.QtWidgets import QMessageBox
from Modules.Dictionary.DConditionsPDE import *
from PyQt5 import QtCore
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QColor
from Modules.Dictionary.DConditionsPDE import domainsConditions
from Modules.Dictionary.DMatrix import initialValues

class ConditionsPDEMatrix():
    matrix3D = np.empty([1,1,1], dtype='U256')
    matrixCombobox = np.empty([1,1], dtype='U256')
    n = 1
    def changeMatrixDimensions(self, n, canvas):
            ConditionsPDEMatrix.matrix3D = np.empty([len(canvas.getEdges()),n, n], dtype='U256')
            print("Matrices de Conditions PDE")
            print(ConditionsPDEMatrix.matrix3D)
            print(len(canvas.getEdges()))
            
       
class ConditionsPDE():
    def createMatrix(self, canvas):
        try:
            n = int(self.inputDepedentVarial.text())
            ConditionsPDEMatrix.changeMatrixDimensions(self, n, canvas)
        except Exception:
             QMessageBox.warning(self, "Important message", "Solo puede ingresar valores numericos")
             return

    def addDimensionMatrixConditions(self, canvas, win):
        intLines = len(canvas.edgeList)
        ConditionsPDEMatrix.n = initialValues["noVariables"]
        ConditionsPDEMatrix.matrix3D = np.empty([intLines, ConditionsPDEMatrix.n, ConditionsPDEMatrix.n], dtype='U256')
        ConditionsPDEMatrix.matrixCombobox = np.empty([intLines, 2, ConditionsPDEMatrix.n], dtype='U256')
        for i in range(ConditionsPDEMatrix.n):
            win.cmbBAbsorColumn.addItem(str(i + 1))
        print('Matriz Conditions PDE')
        print(ConditionsPDEMatrix.matrix3D)

    def askforReset(self, intRow, lEdit):
         dialog = QMessageBox.question(self, 'Importante', '¿Seguro que quieres reiniciar la fila Todos los datos se perderan ', QMessageBox.Cancel | QMessageBox.Yes)
         if dialog == QMessageBox.Yes:
            ConditionsPDE.resetMatrixRow(self, intRow, lEdit)
         else: 
            return
    
    def resetMatrixRow(self, intRow, lEdit):
        lEdit.setText('')
        matrixShape = np.shape(ConditionsPDEMatrix.matrix3D)
        intColumns = matrixShape[1]
        if ConditionsPDEMatrix.matrix3D.size > 0:
            for i in range(intColumns):
                ConditionsPDEMatrix.matrix3D[domainsConditions["domain"]][intRow][i] = ''
        print('Fila reseteada')
        print(ConditionsPDEMatrix.matrix3D)
        
    def insertMatrixZeroFlux(self):
        try:
            strVariable = self.cmbZeroFlux.currentText()
            strVariable = strVariable.replace('u', '')
            intVariable = (int(strVariable) - 1)
            
            matrixShape = np.shape(ConditionsPDEMatrix.matrix3D)
            intColumns = matrixShape[1]
            if ConditionsPDEMatrix.matrix3D.size > 0:
                for i in range(intColumns):
                    ConditionsPDEMatrix.matrix3D[domainsConditions["domain"]][intVariable][i] = '0'
            print("Matriz3D Fila Zero Flux")
            print(ConditionsPDEMatrix.matrix3D)
        except Exception:
            QMessageBox.warning(self, "Important message", "Algo salio mal, es posible que falten datos, o los datos ingresados no son de tipo numerico")

    def insertMatrixDirichlet(self):
        try:
            strVariable = self.cmbDirichletCondition.currentText()
            strVariable = strVariable.replace('u', '')
            intVariable = (int(strVariable) - 1)
            
            matrixShape = np.shape(ConditionsPDEMatrix.matrix3D)
            intColumns = matrixShape[1]
            if ConditionsPDEMatrix.matrix3D.size > 0:
                for i in range(intColumns):
                    ConditionsPDEMatrix.matrix3D[domainsConditions["domain"]][intVariable][i] = self.lEditBoundaryCondition.text()
            print("Matriz3D Fila Dirichlet")
            print(ConditionsPDEMatrix.matrix3D)
        except Exception:
            QMessageBox.warning(self, "Important message", "Algo salio mal, es posible que falten datos, o los datos ingresados no son de tipo numerico")

    def insertMatrixBoundary(self):
        try:
            strVariable = self.cmbBoundaryFluxCondition.currentText()
            strVariable = strVariable.replace('u', '')
            intVariable = (int(strVariable) - 1)

            if ConditionsPDEMatrix.matrix3D.size > 0:
                ConditionsPDEMatrix.matrix3D[domainsConditions["domain"]][intVariable][self.cmbBAbsorColumn.currentIndex()] = self.lEditBoundaryFluxSorce.text() 
            print('Matriz Fila Boundary')
            print(ConditionsPDEMatrix.matrix3D)
        except Exception:
            QMessageBox.warning(self, "Important message", "Algo salio mal, es posible que falten datos, o los datos ingresados no son de tipo numerico")

    def changeBoundaryItemsConfigurations(self):
        print

    def currentElementSelectElementPDE(win, element, canvas, lblFigureSelected):
        # Obtener el index de la figura
        index = int(element.text())
        # Obtiene el numero de lados
        edges = canvas.getEdges()
        # La linea que esta en el momento --> con esta vas a trabajar
        line = edges[index-1]

        domainsConditions["domain"] = index - 1

        # Colores por defectos de las lineas
        LUBronze = QColor(156, 87, 20)
        defaultColor = QPen(LUBronze)
        defaultColor.setWidth(3)
        # Devuelve todos los colores de la figura
        for elem in edges:
            elem.setPen(defaultColor)
        # El color rojo para guardar 
        paint = QPen(Qt.red)
        paint.setWidth(5)
        # Poner el color en la linea
        line.setPen(paint)
        # Poner el numero de figura en el lbl 
        lblFigureSelected.setText("Lado " + str(index))

        # Cuando se muestre una ventana ocultar los elementos
        win.lblBFluxTitle.show()
        win.cmbZeroFlux.show()
        win.cmbTypeConditionPDE.show()
        win.lblTypeConditionTitlePDE.show()
        win.btnResetVariableConditions.show()
        win.btnApplyVariableConditions.show()
        win.toolBoxTypeOfCon.show()
        UpdateConditionPDE.UpdateBoundaryData(win)
        UpdateConditionPDE.UpdateComboboxes(win)


    def changeSelectionCondition(win):
        text = win.cmbSelectionPDE.currentText()
        lines = win.canvas.getEdges()

        if text == "All boundarys":
            # Si existen lineas
            if lines:
                win.lWBoundarysPDE.setEnabled(False)
                win.lblBFluxTitle.show()
                win.cmbZeroFlux.show()
                win.lblTypeConditionTitlePDE.show()
                win.cmbTypeConditionPDE.show()
                win.btnResetVariableConditions.show()
                win.btnApplyVariableConditions.show()
                win.toolBoxTypeOfCon.show()
                win.lblFigureSelected.setText("All boundarys")

            redColor = QPen(Qt.red)
            redColor.setWidth(5)

            for line in lines:
                line.setPen(redColor)

        if text == "Manual":
            #Si existen lineas
            if lines:
                win.lWBoundarysPDE.setEnabled(True)
                win.lblBFluxTitle.hide()
                win.cmbZeroFlux.hide()
                win.lblTypeConditionTitlePDE.hide()
                win.cmbTypeConditionPDE.hide()
                win.btnResetVariableConditions.hide()
                win.btnApplyVariableConditions.hide()
                win.toolBoxTypeOfCon.hide()
                win.lblFigureSelected.setText("")


            LUBronze = QColor(156, 87, 20)
            defaultColor = QPen(LUBronze)
            defaultColor.setWidth(3)
            for line in lines:
                line.setPen(defaultColor)

    def changeMatrixCoefficient(currentIndexRow, currentIndexColumn, Elements):
        indexDictionary = {
            "00": DC00,
            "01": DC01,
            "02": DC02,
            "10": DC10,
            "11": DC11,
            "12": DC12,
            "20": DC20,
            "21": DC21,
            "22": DC22
        }

        if (currentIndexRow == 0 and currentIndexColumn == 0):
            indexDictionary["00"](Elements)
        elif (currentIndexRow == 0 and currentIndexColumn == 1):
            indexDictionary["01"](Elements)
        elif (currentIndexRow == 0 and currentIndexColumn == 2):
            indexDictionary["02"](Elements)
        elif (currentIndexRow == 1 and currentIndexColumn == 0):
            indexDictionary["10"](Elements)
        elif (currentIndexRow == 1 and currentIndexColumn == 1):
            indexDictionary["11"](Elements)
        elif (currentIndexRow == 1 and currentIndexColumn == 2):
            indexDictionary["12"](Elements)
        elif (currentIndexRow == 2 and currentIndexColumn == 0):
            indexDictionary["20"](Elements)
        elif (currentIndexRow == 2 and currentIndexColumn == 1):
            indexDictionary["21"](Elements)
        elif (currentIndexRow == 2 and currentIndexColumn == 2):
            indexDictionary["22"](Elements)
    
    def activateIndexAlpha(alphaXData, alphaYData, currentIndexRow, currentIndexColumn ):

        indexDictionary = {
            "00": IndexA00,
            "01": IndexA01,
            "02": IndexA02,
            "10": IndexA10,
            "11": IndexA11,
            "12": IndexA12,
            "20": IndexA20,
            "21": IndexA21,
            "22": IndexA22
        }


        if (currentIndexRow == 0 and currentIndexColumn == 1):
            indexDictionary["01"](alphaXData, alphaYData)
        elif (currentIndexRow == 0 and currentIndexColumn == 2):
            indexDictionary["02"](alphaXData, alphaYData)
        elif (currentIndexRow == 1 and currentIndexColumn == 0):
            indexDictionary["10"](alphaXData, alphaYData)
        elif (currentIndexRow == 1 and currentIndexColumn == 1):
            indexDictionary["11"](alphaXData, alphaYData)
        elif (currentIndexRow == 1 and currentIndexColumn == 2):
            indexDictionary["12"](alphaXData, alphaYData)
        elif (currentIndexRow == 2 and currentIndexColumn == 0):
            indexDictionary["20"](alphaXData, alphaYData)
        elif (currentIndexRow == 2 and currentIndexColumn == 1):
            indexDictionary["21"](alphaXData, alphaYData)
        elif (currentIndexRow == 2 and currentIndexColumn == 2):
            indexDictionary["22"](alphaXData, alphaYData)

    # currentRowEdit
    def currentRowEdit(currentIndexRow, diffusionCoefElements):
        if currentIndexRow == 0:
            diffusionCoefElements[1].setEnabled(False)
            diffusionCoefElements[2].setEnabled(False)
        elif currentIndexRow == 1:
            diffusionCoefElements[1].setEnabled(True)
            diffusionCoefElements[2].setEnabled(False)
        elif currentIndexRow == 2:
            diffusionCoefElements[1].setEnabled(True)
            diffusionCoefElements[2].setEnabled(True)

    def disabledRowEdit(dataX, dataY, currentIndexRow):
        if currentIndexRow == 0:
            dataX[1].setEnabled(False)
            dataY[1].setEnabled(False)
            dataX[2].setEnabled(False)
            dataY[2].setEnabled(False)

        elif currentIndexRow == 1:
            dataX[1].setEnabled(True)
            dataY[1].setEnabled(True)
            dataX[2].setEnabled(False)
            dataY[2].setEnabled(False)
        elif currentIndexRow == 2:
            dataX[1].setEnabled(True)
            dataY[1].setEnabled(True)
            dataX[2].setEnabled(True)
            dataY[2].setEnabled(True)

    flagZeroFlux = False

    def saveVariable(self, matrixCombobox):
        if self.cmbZeroFlux.currentText() not in matrixCombobox:
            for index, item in enumerate(matrixCombobox):
                print(item)
                if item == '':
                    matrixCombobox[index] = self.cmbZeroFlux.currentText()
                    break
                else:
                    continue
            matrixCombobox = ConditionsPDE.formatandSortMatrixItems(self, matrixCombobox)
            print('Matriz de coordenadas')
            print(matrixCombobox)

    def formatandSortMatrixItems(self, matrixCombobox):
        tempCombobox = []
        print(matrixCombobox)
        for i, item in enumerate(matrixCombobox):
            if item != '':
                print(item.replace('u', ''))
                tempCombobox.append(int(item.replace('u', '')))
        tempCombobox.sort()
        print(tempCombobox)
        matrixCombobox.fill('')
        for index, item in enumerate(tempCombobox):
            matrixCombobox[index] = "u" + str(tempCombobox[index])
        return matrixCombobox

    def deleteItemMatrix(self, matrixCombobox):
        matrixCombobox = ConditionsPDE.formatandSortMatrixItems(self, matrixCombobox)
        print("Matriz con elemento borrado")
        print(matrixCombobox)


    def selectConditionMode(self, arrayConditionPDE):
        if self.cmbTypeConditionPDE.currentIndex() == 0:
            ConditionsPDE.tunOffZeroFlux(self, arrayConditionPDE)
        elif self.cmbTypeConditionPDE.currentIndex() == 1:
            ConditionsPDE.tunOffZeroFlux(self, arrayConditionPDE)
        else:
            ConditionsPDE.turnOnZeroFlux(self, arrayConditionPDE)

    def turnOnZeroFlux(self, arrayConditionPDE):
        ConditionsPDE.flagZeroFlux = True
        self.toolBoxTypeOfCon.setItemEnabled(1, False)
        self.toolBoxTypeOfCon.setItemEnabled(0, False)
        arrayConditionPDE[0].setEnabled(False)
        arrayConditionPDE[1].setEnabled(False)
    
    
    def tunOffZeroFlux(self, arrayConditionPDE):
        ConditionsPDE.flagZeroFlux = False
        self.toolBoxTypeOfCon.setItemEnabled(1, True)
        self.toolBoxTypeOfCon.setItemEnabled(0, True)
        arrayConditionPDE[0].setEnabled(True)
        arrayConditionPDE[1].setEnabled(True)

    def translateVariableCondition(self, cmbCondition, cmbAnotherCondition, matrixItems, anotherMatrixItems, lEdit):
      itemIndex = cmbAnotherCondition.findText(self.cmbZeroFlux.currentText(), QtCore.Qt.MatchFixedString)
      print(self.cmbZeroFlux.currentText())
      if itemIndex == -1:
        ConditionsPDE.applyConditionVariable(self, cmbCondition, matrixItems)
      else:
        dialog = QMessageBox.question(self, 'Importante', '¿Seguro que quieres cambiar la configuracion de la variable? Todos los datos de la fila se perderan ', QMessageBox.Cancel | QMessageBox.Yes)
        if dialog == QMessageBox.Yes:
            anotherMatrixItems[itemIndex] = ''
            ConditionsPDE.deleteItemMatrix(self, anotherMatrixItems)
            cmbAnotherCondition.removeItem(itemIndex)
            ConditionsPDE.resetMatrixRow(self, itemIndex, lEdit)
            ConditionsPDE.applyConditionVariable(self, cmbCondition, matrixItems)
        
        else:
            return

    def selectTypeConditionToolbox(self, cmbTypeCondition):
        itemsDirichlet = ConditionsPDEMatrix.matrixCombobox[domainsConditions["domain"]][0]
        itemsBoundary = ConditionsPDEMatrix.matrixCombobox[domainsConditions["domain"]][1]
        lEditD = self.lEditBoundaryCondition
        lEdiyB = self.lEditBoundaryFluxSorce
        print("Items Dirchlet")
        print(itemsDirichlet)
        if cmbTypeCondition.currentIndex() == 0:
            ConditionsPDE.translateVariableCondition(self, self.cmbDirichletCondition, self.cmbBoundaryFluxCondition, itemsDirichlet, itemsBoundary, lEditD)
        elif cmbTypeCondition.currentIndex() == 1:
            ConditionsPDE.translateVariableCondition(self, self.cmbBoundaryFluxCondition, self.cmbDirichletCondition, itemsBoundary, itemsDirichlet, lEdiyB)
        else: 
            ConditionsPDE.insertMatrixZeroFlux(self)

    def applyConditionVariable(self, comboboxCondition, matrixItems):
        arrayComboboxText = []
        if comboboxCondition.count() > 0:
            for i in range(comboboxCondition.count()):
             arrayComboboxText.append(int(comboboxCondition.itemText(i).replace('u', '')))
            ConditionsPDE.searchVariableinCombobox(self, 
            comboboxCondition, arrayComboboxText, matrixItems)
        else:
            ConditionsPDE.saveVariable(self, matrixItems)
            comboboxCondition.addItem(self.cmbZeroFlux.currentText())

    def searchVariableinCombobox(self, comboboxCondition, arrayComboboxText, matrixItems):
        if int(self.cmbZeroFlux.currentText().replace('u', '')) not in arrayComboboxText:
            updatedCombobox = ConditionsPDE.updateCombobox(self, 
            comboboxCondition, arrayComboboxText)
            ConditionsPDE.saveVariable(self, matrixItems)
            ConditionsPDE.putCurrentIndexCondition(self, updatedCombobox)
            

    def updateCombobox(self, comboboxCondition, arrayComboboxText):
            arrayComboboxText.append(int(self.cmbZeroFlux.currentText().replace('u', '')))
            arrayComboboxText.sort()
            comboboxCondition.clear()
            for i in range(len(arrayComboboxText)):
                comboboxCondition.addItem("u" + str(arrayComboboxText[i]))
            return comboboxCondition

    def putCurrentIndexCondition(self, updatedCombobox):
        index = updatedCombobox.findText(self.cmbZeroFlux.currentText(), QtCore.Qt.MatchFixedString)
        updatedCombobox.setCurrentIndex(index)

    
    def resetVariables(self):
        dialog = QMessageBox.question(self, 'Importante', '¿Seguro que quieres reiniciar las variables del boundary? Todos los datos se perderan para siempre', QMessageBox.Cancel | QMessageBox.Yes)
        if dialog == QMessageBox.Yes:
            self.cmbZeroFlux.setCurrentIndex(0)
            self.cmbTypeConditionPDE.setCurrentIndex(0)
            self.cmbBAbsorColumn.setCurrentIndex(0)
            self.cmbDirichletCondition.clear()
            self.cmbBoundaryFluxCondition.clear()
            self.lEditBoundaryCondition.setText('')
            self.lEditBoundaryFluxSorce.setText('')
            ConditionsPDEMatrix.matrix3D[domainsConditions["domain"]].fill('')
            print('Boundary Reseteado')
            print(ConditionsPDEMatrix.matrix3D)
        else:
            return


class UpdateConditionPDE():

    def UpdateComboboxes(self):
        self.cmbDirichletCondition.clear()
        self.cmbBoundaryFluxCondition.clear()
        matrix = ConditionsPDEMatrix.matrixCombobox[domainsConditions["domain"]]
        matrixShape = np.shape(ConditionsPDEMatrix.matrixCombobox[domainsConditions["domain"]])
        intColumns = matrixShape[1]
        print('numero de columnas')
        print(intColumns)
        for i in range(intColumns):
            if matrix[0][i] != '':
                self.cmbDirichletCondition.addItem(matrix[0][i])

            if matrix[1][i] != '':
                self.cmbBoundaryFluxCondition.addItem(matrix[1][i])

    def UpdateBoundaryData(self):
        UpdateConditionPDE.UpdateDirichlet(self)
        UpdateConditionPDE.UpdateBoundary(self)

    def UpdateDirichlet(self):
        strVariable = self.cmbDirichletCondition.currentText()
        if strVariable == '':
            return
        else:
            strVariable = strVariable.replace('u', '')
            intVariable = (int(strVariable) - 1)
            self.lEditBoundaryCondition.setText(ConditionsPDEMatrix.matrix3D[domainsConditions["domain"]][intVariable][0])
    
    def UpdateBoundary(self):
        strVariable = self.cmbBoundaryFluxCondition.currentText()
        if strVariable == '':
            return
        else:
            strVariable = strVariable.replace('u', '')
            intVariable = (int(strVariable) - 1)
            self.lEditBoundaryFluxSorce.setText(ConditionsPDEMatrix.matrix3D[domainsConditions["domain"]][intVariable][self.cmbBAbsorColumn.currentIndex()])

