import TraceRouteTest #build IPs file and give us access to traceroute method
import numpy

processes = []
TestProcesses = False


def parseTraceRouteText(text):
    if(TraceRouteTest.testOS() == 2):
        lines = text.splitlines()
        IPs = []
        for i in range (1, len(lines)):
            tokens = lines[i].split(' ')
            IPs.append(tokens[3])
    elif(TraceRouteTest.testOS() ==1):
        pass
    return IPs

adj_mat = numpy.zeros((TraceRouteTest.getNumberOfIPsInFile(),TraceRouteTest.getNumberOfIPsInFile()))

try:
    count = 0
    while count < TraceRouteTest.numberOfProcesses and count < TraceRouteTest.getNumberOfIPsInFile():
        try:
            processes.append(TraceRouteTest.createTracerouteProcess(count))
            if TestProcesses:
                numberOfProcesses += 1
            count += 1
        except Exception as e:
            print e
            TestProcesses = False
            numberOfProcesses = count
    print TraceRouteTest.numberOfProcesses

    while count < TraceRouteTest.getNumberOfIPsInFile():
        for p in range(0, len(processes)):
            if (not processes[p][0].poll() == None) and (count < TraceRouteTest.getNumberOfIPsInFile()):
                #print processes[p][1]
                text = processes[p][0].stdout.read()
                iplist = parseTraceRouteText(text)
                for n in range(0, len(iplist)-1):
                    firstIpN = TraceRouteTest.getIPPositionFromFile(iplist[n])
                    secondIpN = TraceRouteTest.getIPPositionFromFile(iplist[n + 1])
                    adj_mat[firstIpN][secondIpN] = 1
                    adj_mat[secondIpN][firstIpN] = 1
                processes[p][0].wait()
                processes[p][0] = None
                print count
                print TraceRouteTest.getNumberOfIPsInFile()
                processes[p] = TraceRouteTest.createTracerouteProcess(count)
                count += 1
    adj_mat_file = open("adj-mat.csv", "w")
    for row in adj_mat:
        for i in range(0, len(row)):
            adj_mat_file.write(str(row[i]))
            if i != len(row) - 1:
                adj_mat_file.write(", ")
        adj_mat_file.write("\n")
finally:
    for p in processes:
        if(p[0] != None):
            p[0].wait()