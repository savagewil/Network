import networkx
import matplotlib.pyplot as pylt

array = "Make A Sentence".split("")
graph = networkx.Graph(data=array)
pylt.subplot(121)
networkx.draw(graph)
