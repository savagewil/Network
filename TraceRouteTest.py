import subprocess
processes = []
count = 1
numberOfProcesses = 4
for p in range(0, numberOfProcesses):
    processes.append(subprocess.Popen("tracert 129.21.1." + str(count % 255 + 1), stdin = subprocess.PIPE, stdout = subprocess.PIPE))
    count += 1
while count < 256:
    for p in range(0, len(processes)):
        if not processes[p].poll() == None:
            print processes[p].stdout.read()
            processes[p] = processes.append(subprocess.Popen("tracert 129.21.1." + str(count % 255 + 1), stdin = subprocess.PIPE, stdout = subprocess.PIPE))
            count += 1
for process in processes:
    print process.stdout.read()
