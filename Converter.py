import networkx, numpy, matplotlib
def clean(FILE,NEWFILE, count):
    print count
    NEWFILE.write(FILE.readline().replace("0.00.0", "0.0"))
def test(x):
    try:
        return float(x)
    except Exception:
        print x

# int("CRASH")
PATH = "C:\Users\Savage\Google Drive\school\College\Exploration of Place and space CSV\\adj-mat.csv"

PATHNEW= "C:\Users\Savage\Google Drive\school\College\Exploration of Place and space CSV\\adj-matCleaned.csv"


FILE= open(PATH,"r")
FILENEW= open(PATHNEW,"w")
count = 0
matrixArray = []
for line in FILE:
    print count
    count += 1
    if count > 1:
        array = line.split(",")
        line_new = [array.pop(0)]

        while len(array) > 0:
            word = array.pop(0)
            word = word.replace(".00.", ".0,0.").replace(".01.", ".0,1.")
            # print word
            try:
                word = [str(float(i)) for i in word.split(",")]
                line_new.extend(word)
            except Exception as e:
                pass
                # print "'"+word+"'"
                # raise e


        FILENEW.write(", ".join(line_new)+"\n")
    else:
        FILENEW.write(line)

FILENEW.close()