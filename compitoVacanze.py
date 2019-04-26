import math


diz={  0:[1,2],
        1:[3,0],
        2:[0],
        3:[1],
        4:[2,6,0],
        5:[2,3],
        6:[6,7],
        7:[7,2]
}  

#dijkstra nella funzione

def dijkstra(graph,initial,finish,dim):
    labelList = [math.inf] * len(graph) #inizializzazione delle label (moltiplico per il numero di nodi per le righe)
    labelList[initial] = 0  #distanza dal nodo sorgente è 0
    unexploredNode = []   

    for cont in range(dim):
        unexploredNode.append(cont)

    cntPasso=0

    while len(unexploredNode)>0:
       
        infiniteList = [math.inf] * len(graph)
        
        for i in unexploredNode:
            infiniteList[i]=labelList[i]    #valore della labelList[i] 
        
        minimun = min(infiniteList)   #trovo il minimo

        if(minimun==math.inf):  #controllo per uscire dal ciclo
            break
        
        currentNode = infiniteList.index(minimun)  #prendo l'indice del valore minimo
        for node, weight in enumerate(graph[currentNode]):       #ciclo for con ricerca dei nodi collegati a k per indici non ancora esplorati
            if(weight!=0):   #verifico che sia collegato e che non sia se stesso
                newLabel = labelList[currentNode] + weight
                if(newLabel<labelList[node]):
                    labelList[node] = newLabel     #per ogni nuovo nodo sommo (valore label(k)+peso arco di quel nodo) il valore della sua label e controllo se sono minori così sostituisco sennò niente
        
        cntPasso=cntPasso+1
        unexploredNode.remove(currentNode) #rimuovo l'indice visitato

    print("la distanza dal nodo %s di partenza ed il nodo %s di arrivo e' --> %s" % (initial,finish,labelList[finish]))
    
    return labelList

def generateGraph(diz):
    graph=[]
    nodi=0

    for key,value in diz.items():      #visualizzo dizionario
        print("%s --> %s" %(key,value))
        nodi+=1
    
    graph = [[False for r in range(nodi)] for c in range(nodi)] #inizializzo la matrice a false
    
    for key,value in diz.items():
        for k in value:
            graph[key][k] = True        #viene assegnato true alle celle dei nodi collegati fra loro 

    return graph,nodi


start = int(input("inserire il nodo di partenza: "))

finish = int(input("inserire il nodo di arrivo: "))

graph,dim = generateGraph(diz)

dijkstra(graph,start,finish,dim)