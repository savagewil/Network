import subprocess
processes = []
count = 1
processes.append(subprocess.Popen("tracert 129.21.1." + str(count % 255 + 1), stdin = subprocess.PIPE, stdout = subprocess.PIPE))
while count < 256:
    print processes[0].__dict__