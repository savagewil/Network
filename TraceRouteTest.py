import subprocess, sys

processes = []
count = 0
numberOfProcesses = 255
TestProcesses = False
numberOfPings = 1
pingTimeout = 1
IPs = {}
Start_Octaves = [129, 21, 1, 1]
End_Octaves = [129, 21, 255, 255]

def generateIP(count):
    """
    Generates and IP using Modulus
    :param count: The current count
    :return: an IP
    """
    STRING = ""
    for i in range(3, -1, -1):
        STRING = "." + str(count % (End_Octaves[i] - Start_Octaves[i] + 1) + Start_Octaves[i]) + STRING
        count = count // (End_Octaves[i] - Start_Octaves[i] + 1)
    return STRING[1:]


def testOS():
    if sys.platform == "win32":
        return 1
    elif sys.platform == "linux2":
        return 2
    else:
        raise OSError(1, "Operating System sucks")


def findMyIP():
    """
    :return: The IP of the current system
    """
    if testOS() == 1:
        p = subprocess.Popen("ipconfig", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        text = p.stdout.read()
        lines = text.split("\n")
        lines = filter(lambda line:"IPv4 Address" in line, lines)
        if len(lines) >= 1:
            line = lines[0]
        else:
            raise EnvironmentError(1, "Not On Wifi")


        return [subprocess.Popen("ping -n " + str(numberOfPings) + " " + generateIP(count),
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE), generateIP(count)]
    elif testOS() == 2:
        args = ["ip", "-4", "route","get", "8.8.8.8", "|", "awk","{'print $7'}", "|" , "tr", "-d", "'\n'"]
        return subprocess.check_output(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)


def createProcess(count):
    if testOS() == 1:
        return [subprocess.Popen("ping -n " + str(numberOfPings) + " " + generateIP(count),
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE), generateIP(count)]
    elif testOS() == 2:
        args = ["ping", "-c", str(numberOfPings),"-W", str(pingTimeout), generateIP(count)]
        return [subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE), generateIP(count)]

def getCountOfPosibleIPs():
    return (End_Octaves[0] - Start_Octaves[0] + 1) * (End_Octaves[1] - Start_Octaves[1] + 1) * (
        End_Octaves[2] - Start_Octaves[2] + 1) * (End_Octaves[3] - Start_Octaves[3] + 1)

try:
    count = 0

    while count < numberOfProcesses:
        try:
            processes.append(createProcess(count))
            if TestProcesses:
                numberOfProcesses += 1
            count += 1
        except Exception as e:
            print e
            TestProcesses = False
            numberOfProcesses = count
    print numberOfProcesses

    print "Possible IPs:", getCountOfPosibleIPs()
    while count < getCountOfPosibleIPs():
        for p in range(0, len(processes)):
            if not processes[p][0].poll() == None:
                print processes[p][1]
                text = processes[p][0].stdout.read()
                if(testOS() == 1):
                    IPs[processes[p][1]] = (text.count("Request timed out.") != numberOfPings)
                elif(testOS() == 2):
                    IPs[processes[p][1]] = (text.count("64 bytes from") >= 1)
                processes[p][0].wait()
                processes[p][0] = None
                processes[p] = createProcess(count)
                count += 1


    for process in processes:
        text = process[0].stdout.read()
        IPs[process[1]] = (text.count("Request timed out.") != numberOfPings)
    print "======================"
    FILE = open("IPs.txt", "w")
    for IP in IPs:
        if IPs[IP]:
            print IP
            FILE.write(IP + "\n")

finally:
    for p in processes:
        p[0].wait()
