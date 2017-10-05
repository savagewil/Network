import networkx
import matplotlib.pyplot as pylt
def clean(FILE,NEWFILE, count):
    print count
    NEWFILE.write(FILE.readline().replace("0.00.0", "0.0"))
def test(x):
    try:
        return float(x)
    except Exception:
        print x

# int("CRASH")
PATHNEW = "C:\Users\Savage\Google Drive\school\College\Exploration of Place and space CSV\\adj-matCleaned.csv"


FILENEW = open(PATHNEW,"r")

count = 0
matrixArray = []
graph = networkx.graph.Graph()
IPsArray = FILENEW.readline().split(",")[1:]
for IP in IPsArray:
    graph.add_node(IP)
for line in FILENEW:
    print count
    temp_array = [int(float(i)) for i in line.split(",")[1:]]
    for ii in range(0, len(temp_array)):
        if temp_array[ii] >= 1:
            graph.add_edge(IPsArray[count], IPsArray[ii])
    count += 1


pylt.plot()
networkx.draw(graph)
