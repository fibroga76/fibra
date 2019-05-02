import math

graph = [[0,3,0,4],
         [3,0,1,5],
         [0,1,0,2],
         [4,5,2,0]]
         

source = 0
nodeNumber = len(graph)

labelList = [math.inf for i in range (nodeNumber)]
labelList[source] = 0


unexploredNode = [i for i in range(nodeNumber)]

while len(unexploredNode)>0:       #scegliere il nodo con label minore

    minLabel = min([labelList[node] for node in unexploredNode])

    for i in unexploredNode:
        if labelList[i]==minLabel:
            currentNode = i
        else:
            break


    unexploredNode.remove(currentNode)

    for neighbourNode,weight in enumerate(graph[currentNode]):   #si cicla sui vicini del sorgente (di zero), per ottenere indice e valore si aggiunge enumerate
        if weight>0:
            distance = labelList[currentNode]+weight
            if(distance<labelList[neighbourNode]):
                labelList[neighbourNode]=distance
    

print(labelList)

    


