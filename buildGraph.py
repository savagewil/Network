import TraceRouteTest #build IPs file and give us access to traceroute method
import numpy
import re

processes = []
TestProcesses = False
ip_regex = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
myIPAddr = TraceRouteTest.findMyIP()



#This function is broken af.  TODO fix
def parseTraceRouteText(text):
    allIPs = ip_regex.findall(text)
    if(TraceRouteTest.testOS() == 2):
        myIPAddrList = [myIPAddr]
        IPs = allIPs[2:]
        myIPAddrList.extend(IPs)
        IPs = myIPAddrList
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
    #print TraceRouteTest.numberOfProcesses
    print "Scanning Network Connections..."
    while count < TraceRouteTest.getNumberOfIPsInFile():
        for p in range(0, len(processes)):
            if (not processes[p][0].poll() == None) and (count < TraceRouteTest.getNumberOfIPsInFile()):
                #print processes[p][1]
                text = processes[p][0].stdout.read()
                iplist = parseTraceRouteText(text)
                #print iplist
                for n in range(0, len(iplist)-1):
                    firstIpN = TraceRouteTest.getIPPositionFromFile(iplist[n])
                    secondIpN = TraceRouteTest.getIPPositionFromFile(iplist[n + 1])
                    adj_mat[firstIpN][secondIpN] = 1
                    adj_mat[secondIpN][firstIpN] = 1
                processes[p][0].wait()
                processes[p][0] = None
                #print count
                #print TraceRouteTest.getNumberOfIPsInFile()
                processes[p] = TraceRouteTest.createTracerouteProcess(count)
                count += 1
                TraceRouteTest.printStatusBar(TraceRouteTest.getNumberOfIPsInFile(), count, 40)
    adj_mat_file = open("adj-mat.csv", "w")
    adj_mat_file.write("IP addrs")
    with open("IPs.txt") as f:
        for row in f:
            adj_mat_file.write(',' + row.strip('\n'))
        adj_mat_file.write('\n')
    upIPAddrs = open('IPs.txt').readlines()
    for j in range(0, len(adj_mat)):
        adj_mat_file.write(upIPAddrs[j].strip('\n') + ',')
        for i in range(0, len(adj_mat[j])):
            adj_mat_file.write(str(adj_mat[j][i]))
            if i != len(row) - 1:
                adj_mat_file.write(", ")
            adj_mat_file.flush()
        adj_mat_file.write("\n")
finally:
    for p in processes:
        if(p[0] != None):
            p[0].wait()