import networkx, numpy
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
IPsArray = []
print count
for line in FILENEW:
    if count == 0:
        IPsArray = line.split(",")[1:]
    # line = FILENEW.readline()
    print count
    if 1 < count <= 12391:
        matrixArray.append([int(float(i)) for i in line.split(",")[1:]])


# for row in matrixArray:
#     for num in row:
#         print num,
#     print
graph = networkx.graph.Graph()
print "IPS", len(IPsArray)
for IP in IPsArray:
    graph.add_node(IP)
for i in range(0, len(matrixArray)):
    # print"LENGTH", len(matrixArray[i])
    for ii in range(0, len(matrixArray[i])):
        # print i,ii
        if matrixArray[i][ii] == 1:
            graph.add_edge(IPsArray[i], IPsArray[ii])

pylt.plot()
networkx.draw(graph)
