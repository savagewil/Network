import networkx
import Dictionaryfunctions
import matplotlib.pyplot as pylt


def clean(FILE,NEWFILE, count):
    print count
    NEWFILE.write(FILE.readline().replace("0.00.0", "0.0"))


def test(x):
    try:
        return float(x)
    except Exception:
        print x


def getShortestPathData(graph):
    shortestPathsData = graph.shortest_path_length()
    MaxPath, AveragePath = Dictionaryfunctions.Get_Max_And_Average(shortestPathsData)

getMaxAndSumAndCount
# int("CRASH")
PATHNEW = "C:\Users\Savage\Google Drive\school\College\Exploration of Place and space CSV\\adj-matCleaned.csv"


FILENEW = open(PATHNEW,"r")

count = 0
matrixArray = []
graph = networkx.graph.Graph()
graph.number_of_nodes()
IPsArray = FILENEW.readline().split(",")[1:]
# for IP in IPsArray:
for line in FILENEW:
    # print count
    temp_array = [int(float(i)) for i in line.split(",")[1:]]
    for ii in range(0, len(temp_array)):
        if temp_array[ii] >= 1:
            if not graph.has_node(IPsArray[count]):
                graph.add_node(IPsArray[count])
            if not graph.has_node(IPsArray[ii]):
                graph.add_node(IPsArray[ii])
            graph.add_edge(IPsArray[count], IPsArray[ii])
    count += 1
print "Read CSV"

pylt.plot()
for IP in IPsArray:
    if graph.has_node(IP):
        graph2 = graph.copy()
        graph2.remove_node(IP)

print networkx.average_shortest_path_length(graph)
