class Conditions():
    def currentTypeCondition(comb, tbox, array): 
        
        for i in range(tbox.count()):
            tbox.removeItem(tbox.currentIndex())
         
        if comb.currentIndex() == 1:
            tbox.insertItem(0, array[0], str(comb.currentText()))
        if comb.currentIndex() == 2:
            tbox.insertItem(0, array[1], str(comb.currentText()))

    def reloadEdges(canvas, listWid):
        edges = canvas.getEdges()
        print('here')
        print(edges)
        listOfEdges = []

        if listWid.count() != 0:
            listWid.clear()
        
        for i in range(len(edges)):
            text = "linea " + str(i+1)
            listOfEdges.append([edges[i], text ])
            listWid.addItem(text)
