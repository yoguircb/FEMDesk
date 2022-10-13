from Modules.Dictionary.DMatrix import *
class Materials():
     def currentHeatConduction(comb, ar):
        for i, item in enumerate(ar):
            ar[i].clear()
            ar[i].setEnabled(False)

        if comb.currentIndex() == 0:
            diffusionMatrix["inputMode"] = 0
            ar[0].setEnabled(True)
        if comb.currentIndex() == 1:
            diffusionMatrix["inputMode"] = 1
            ar[1].setEnabled(True)
            ar[4].setEnabled(True)
            ar[2].insert("0")
            ar[3].insert("0")
        if comb.currentIndex() == 2:
            diffusionMatrix["inputMode"] = 2
            ar[1].setEnabled(True)
            ar[2].setEnabled(True)
            ar[4].setEnabled(True)
        if comb.currentIndex() == 3:
            diffusionMatrix["inputMode"] = 3
            ar[1].setEnabled(True)
            ar[2].setEnabled(True)
            ar[3].setEnabled(True)
            ar[4].setEnabled(True)

     def currentTextSimmetry(comb, ar):
        if comb.currentIndex() == 2:
            ar[3].clear()
            ar[3].insert(ar[2].text())