import random
import copy

def secretSanta(nameList):
    """
	args: a list of strings. each string a name in the secret santa pool
    return: a list of tuples of strings. each tupel (x,y),
        being a 'x gets y' relationship
    This function creates a random secret santa list from the nameList
    """
    #register = []
    drawingList = copy.deepcopy(nameList)
    done = False
    register = []
    index = 0
    while(not done):
        #person drawing
        name = nameList[index]
        
        #draw a name
        drawnName = drawingList[random.randint(0,len(drawingList)-1)]

        #make sure last person to draw doesn't draw themselves
        if (len(drawingList) == 2) and (nameList[-1] in drawingList):
            drawnName = nameList[-1]
        
        if (drawnName != name):
            register.append((name,drawnName))
            drawingList.remove(drawnName)
            index+=1

        if (len(drawingList) == 0):
            done = True

    return register



names = ["Sara", "Sheena", "Amrit", "Hannah", "Chloe", "Claire", "Seqouyah"]

secretList = secretSanta(names)

for drawing in secretList:
    drawer, drawie = drawing
    print("{} drew: \t{}".format(drawer, drawie))

