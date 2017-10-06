import networkx, random
import matplotlib.pyplot as pylt
graph = networkx.graph.Graph()
numberNodes = 10 #int(raw_input("Number of nodes:"))
numberEdges = 20 #int(raw_input("Number of edges:"))

ArrayNodes = []
ArrayConnections = {}

for number in range(0, numberNodes):
    graph.add_node(str(number))
    ArrayNodes.append(str(number))
    ArrayConnections[str(number)] = [str(number)]
    

for edge in range(0,numberEdges):
    
    if len(ArrayConnections[ArrayNodes[0]]) == len(ArrayNodes):
        n1 = random.randint(0,len(ArrayNodes) - 1)
        ArrayNodes2 = ArrayNodes[:n1] + ArrayNodes[n1 + 1:]
        n2 = random.randint(0,len(ArrayNodes2) - 1)
        graph.add_edge(ArrayNodes2[n2], ArrayNodes[n1])
        
    else:
        n1 = random.randint(0,len(ArrayNodes) - 1)
        print ArrayConnections[ArrayNodes[n1]]
        ArrayNodes2 = filter(lambda num:not num in ArrayConnections[ArrayNodes[n1]], ArrayNodes)
        print ArrayNodes2
        n2 = random.randint(0,len(ArrayNodes2) - 1)
        temp = ArrayConnections[ArrayNodes[n1]][:]
        temp2 = ArrayConnections[ArrayNodes2[n2]][:]
        for let in temp:
            ArrayConnections[let].extend(temp2)
        for let in temp2:
            ArrayConnections[let].extend(temp)
        graph.add_edge(ArrayNodes2[n2], ArrayNodes[n1])
        print ArrayConnections
##        raw_input()
    
pylt.plot()
networkx.draw(graph)
pylt.show()
