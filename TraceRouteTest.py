import subprocess
from subprocess import check_output
import sys
processes = []
count = 1
numberOfProcesses = 4
for p in range(0, numberOfProcesses):
    if sys.platform == 'linux2':
        args = ["/usr/sbin/traceroute"]
        args.append("129.21.1."+ str(count % 255 + 1))
        processes.append(check_output(args, stdin = subprocess.PIPE, shell=True))
    elif sys.platform == 'win32':
        processes.append(
            subprocess.Popen("tracert 129.21.1." + str(count % 255 + 1), stdin=subprocess.PIPE, stdout=subprocess.PIPE))
    count += 1

while count < 256:
    for p in range(0, len(processes)):
        if not processes[p].poll() == None:
            print processes[p].stdout.read()
            if sys.platform == 'linux2':
                processes.append(check_output("/usr/sbin/traceroute 129.21.1." + str(count % 255 + 1), stdin=subprocess.PIPE))
            else:
                processes.append(
                    subprocess.Popen("tracert 129.21.1." + str(count % 255 + 1), stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE))
            count += 1
for process in processes:
    print process.stdout.read()
