from Modules.Tabs import *
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt
import Modules.Matrix
#from dialogMatrix import Matrix

class ModelWizard:
    def hideInitialTabs(tabs, tabMenu):
        Tabs.hideElementsTab(tabs, tabMenu)

    flagHeatTransferSolids = False
    flagHeatTransferFluids = False
    flagCoefficientPDE = False
    flagModelWizardActivated = False

    def currentTreeItem(self, item, indexTree):
        if item.text(indexTree) == "Heat Transfer in Solids":
            item.setForeground(0, QBrush(Qt.blue))
            anotheritem = self.treeModelWizard.itemBelow(item)
            anotheritem.setForeground(0, QBrush(Qt.black))
            ModelWizard.flagSolid = True
            ModelWizard.flagFluid = False
            ModelWizard.flagCoefficientPDE = False

        if item.text(indexTree) == "Heat Transfer in Fluids":
            item.setForeground(0, QBrush(Qt.blue))
            anotheritem = self.treeModelWizard.itemAbove(item)
            anotheritem.setForeground(0, QBrush(Qt.black))
            ModelWizard.flagSolid = False
            ModelWizard.flagFluid = True
            ModelWizard.flagCoefficientPDE = False
            
        if item.text(indexTree) == "Coefficient form PDE":
            item.setForeground(0, QBrush(Qt.blue))
            ModelWizard.flagCoefficientPDE = True

        


    def currentTreeWidgetConfiguration(self, tabs, tabMenu):
        if ModelWizard.flagModelWizardActivated == True:
            Modules.Matrix.Matrix.newMatrix(self)
        else:
         if ModelWizard.flagSolid == True:
            Tabs.hideElementsTab(tabs, tabMenu)
            Tabs.addTabElement(tabs, tabMenu)
            Tabs.hideElementTab(5, tabMenu)
            Tabs.hideElementTab(6, tabMenu)
            ModelWizard.flagModelWizardActivated = True

         if ModelWizard.flagFluid == True:
            Tabs.hideElementsTab(tabs, tabMenu)
            Tabs.addTabElement(tabs, tabMenu)
            Tabs.hideElementTab(5, tabMenu)
            Tabs.hideElementTab(6, tabMenu)

         if ModelWizard.flagCoefficientPDE == True:
            Tabs.hideElementsTab(tabs, tabMenu)
            Tabs.addTabElement(tabs, tabMenu)
            Tabs.hideElementTab(1, tabMenu)
            Tabs.hideElementTab(3, tabMenu)
            Tabs.hideElementTab(7, tabMenu)
            self.inputDepedentVarial.setEnabled(True)
            self.btnModelWizardReset.setEnabled(True)
            ModelWizard.flagModelWizardActivated == True


    

    

