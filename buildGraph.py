import TraceRouteTest #build IPs file and give us access to traceroute method
import numpy

processes = []

def parseTraceRouteText(text):
    if(TraceRouteTest.testOS() == 2):
        lines = text.splitnewlines()
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
    print numberOfProcesses

    while count < TraceRouteTest.getNumberOfIPsInFile():
        for p in range(0, len(processes)):
            if not processes[p][0].poll() == None:
                print processes[p][1]
                text = processes[p][0].stdout.read()
                iplist = parseTraceRouteText(text)
                for n in range(0, len(iplist)-1):
                    firstIpN = TraceRouteTest.getIPPositionFromFile(iplist[n])
                    secondIpN = TraceRouteTest.getIPPositionFromFile(iplist[n + 1])
                    adj_mat[firstIpN][secondIpN] = 1
                    adj_mat[secondIpN][firstIpN] = 1
                processes[p][0].wait()
                processes[p][0] = None
                processes[p] = TraceRouteTest.createTracerouteProcess(count)
                count += 1
    print adj_mat
finally:
    for p in processes:
        p[0].wait()