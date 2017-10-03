import networkx, numpy, matplotlib
def clean(FILE,NEWFILE, count):
    print count
    NEWFILE.write(FILE.readline().replace("0.00.0", "0.0"))
def test(x):
    try:
        return float(x)
    except Exception:
        print x

# int("CRASH")
PATH = "C:\Users\William\Google Drive\school\College\Intro to Place and Space\NetworkMapper\\adj-mat.csv"

# FILE = open(PATH, "r")
# FILENEW = open(PATHNEW,"w")
# FILE = open(PATH,"r")

FILENEW = open(PATHNEW,"r")
# FILENEW2 = open(PATHNEW2,"w")
count = 0
matrixArray = []
IPsArray = []
print count
for line in FILENEW:
    if line == 0:
        IPsArray = matrixArray.append(line.split(",")[1:])
    # line = FILENEW.readline()
    print count
    count += 1
    if 1 < count <= 12391:
        matrixArray.append(line.split(",")[1:])


# for row in matrixArray:
#     for num in row:
#         print num,
#     print
graph = networkx.graph.Graph()
for IP in IPsArray:
    graph.add_node(IP)
for i in range(0, len(matrixArray)):
    for ii in range(0, len(matrixArray[i])):
        if matrixArray[i][ii] == 1:
            graph.add_edge(IPsArray[i], IPsArray[ii])

matplotlib.subplot(121)
networkx.draw(graph)
