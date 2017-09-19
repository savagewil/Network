import subprocess, sys
processes = []
count = 0
numberOfProcesses = 10
TestProcesses = True
numberOfPings = 1
IPs = {}
Start_Octaves = [129, 21, 1, 1]
End_Octaves = [129, 21, 2, 255]

def generate_IP(count):
    STRING = ""
    for i in range(3,-1, -1):
        STRING = "." + str(count % (End_Octaves[i] - Start_Octaves[i] + 1) + Start_Octaves[i]) + STRING
        count = count // (End_Octaves[i] - Start_Octaves[i] + 1)
    return STRING[1:]
def testOS():
    if not sys.platform == "win32":
        return 1
    else:
        raise OSError(1, "Operating System is not yet supported")
def findMyIP():
    if testOS() == 1:
        return [subprocess.Popen("ping -n " + str(numberOfPings) + " " + generate_IP(count),
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE), generate_IP(count)]

    processes.append([subprocess.Popen("ping -n " + str(numberOfPings) + " " + generate_IP(count),
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE), generate_IP(count)])

def createProcess(count):
    if testOS() == 1:
        return [subprocess.Popen("ping -n " + str(numberOfPings) + " " + generate_IP(count),
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE), generate_IP(count)]
count = 0


while count < numberOfProcesses:
    try:
        processes.append(createProcess(count))
        if TestProcesses:
            numberOfProcesses += 1
            count += 1
    except Exception:
        TestProcesses = False
        numberOfProcesses = count
print numberOfProcesses

print (End_Octaves[0] - Start_Octaves[0] + 1) * (End_Octaves[1] - Start_Octaves[1] + 1) * (End_Octaves[2] - Start_Octaves[2] + 1) *(End_Octaves[3] - Start_Octaves[3] + 1)
while count < (End_Octaves[0] - Start_Octaves[0] + 1) * (End_Octaves[1] - Start_Octaves[1] + 1) * \
        (End_Octaves[2] - Start_Octaves[2] + 1) *(End_Octaves[3] - Start_Octaves[3] + 1):
    for p in range(0, len(processes)):
        if not processes[p][0].poll() == None:
            print processes[p][1]
            text = processes[p][0].stdout.read()
            IPs[processes[p][1]] = (text.count("Request timed out.") != numberOfPings)
            processes[p][0] = None
            processes[p] = createProcess(count)
            count += 1

print "======================"
for process in processes:
    text = process[0].stdout.read()
    IPs[process[1]] = (text.count("Request timed out.") != numberOfPings)

for IP in IPs:
    if IPs[IP]:
        print IP

"""129.21.1.155
129.21.1.165
129.21.1.23
129.21.1.21
129.21.1.20
129.21.1.26
129.21.1.25
129.21.1.24
129.21.1.29
129.21.1.28
129.21.1.164
129.21.1.143
129.21.1.30
129.21.1.32
129.21.1.35
129.21.1.174
129.21.1.175
129.21.1.170
129.21.1.169
129.21.1.18
129.21.1.19
129.21.1.16
129.21.1.17
129.21.1.200
129.21.1.90
129.21.1.91
129.21.1.98
129.21.1.99
129.21.1.114
129.21.1.111
129.21.1.183
129.21.1.182
129.21.1.104
129.21.1.103
129.21.1.101
129.21.1.100
129.21.1.166"""