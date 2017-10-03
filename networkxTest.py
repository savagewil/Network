print "4"
import networkx.classes.graph as g
import networkx.drawing as d
print "3"
import matplotlib.pyplot as pylt
print "2"
# array = .split()
print "1"
graph = g.Graph()
path = "Book.txt"
for line in open(path):
    line = line[:-1]
    for l in line:
        if not l in graph:
            graph.add_node(l)
    for i in range(0, len(line)):
        if i > 0:
            graph.add_edge(line[i], line[i - 1])
pylt.plot()
print "test"
d.draw(graph)
pylt.show()