import sys
nodes = []
with open('adj-mat.csv') as f:
    nodes = open("nodes.csv", 'w')
    nodes.write("ID, Label\n")
    lines = f.readlines()
    line1 = lines[0]
    line1Tokens = line1.split(',')
    for i in range(1,len(line1Tokens)):
        nodes.write(str(i)+ ", " + line1Tokens[i] + '\n')
    nodes.close()
    edges = open("edges.csv", 'w')
    edges.write("ID,Source,Target,Type\n")
    counter = 1
    for i in range(1,len(lines)):
        lineTokens = lines[i].split(',')
        for j in range(1, len(lineTokens)):
            #print lineTokens[j]
            if lineTokens[j].strip(' ') == '1.0':
                edges.write(str(counter) + ", " + str(i) + ', ' + str(j) + ',undirected\n')
                counter += 1
                edges.flush()
    edges.close()