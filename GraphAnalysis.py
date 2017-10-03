import networkx, numpy
def clean(FILE,NEWFILE, count):
    print count
    NEWFILE.write(FILE.readline().replace("0.00.0", "0.0"))
def test(x):
    try:
        return float(x)
    except Exception:
        print x

# int("CRASH")
PATH = "C:\Users\William\Google Drive\school\College\Intro to Place and Space\NetworkMapper\\adj-mat.csv"
PATHNEW = "C:\Users\William\Google Drive\school\College\Intro to Place and Space\NetworkMapper\\adj-matCleaned.csv"

PATHNEW2 = "C:\Users\William\Google Drive\school\College\Intro to Place and Space\NetworkMapper\\adj-matCleaned2.csv"
# FILE = open(PATH, "r")
# FILENEW = open(PATHNEW,"w")
# FILE = open(PATH,"r")

FILENEW = open(PATHNEW,"r")
# FILENEW2 = open(PATHNEW2,"w")
count = 0
matrixArray = []
IPsArray = []
print count
for line in FILENEW:
    # line = FILENEW.readline()
    print count
    count += 1
    if 1 <= count <= 12391:
        matrixArray.append(line.split(",")[1:])
        # FILENEW.write(line.replace("0.00.0", "0.0, 0.0")[:-3] + "\n")
        # FILENEW2.write(line.replace("0.00.0", "0.0, 0.0")[:-3] + "\n")
    else:
        IPsArray = matrixArray.append(line.split(",")[1:])
        print IPsArray

for row in matrixArray:
    for num in row:
        print num,
    print
