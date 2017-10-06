def getMaxAndSumAndCount(DICT):
    return reduce(lambda base,current:[max(base[0], current), base[1] + current], DICT.values(),[0,0]) + [len(DICT.values())]


def getMaxAndSumAndCountSuper(DICT):
    return reduce(getMaxAndSumAndCountSuperHelper, DICT.values(), [0,0,0])
    
    
def getMaxAndSumAndCountSuperHelper(base, DICT):
    out = getMaxAndSumAndCount(DICT)
    print out
    return [max(base[0], out[0]), out[1] + base[1], out[2] + base[2]]

##import random

##DICT = {}
##word = "wertyuioplkjhgfdsazxcvbnm"
##for let in word:
##    d2 = {}
##    for let_ in word:
##        d2[let_] = random.randint(0, 50)
##    DICT[let] = d2
def Get_Max_And_Average(DICT):
    out = getMaxAndSumAndCountSuper(DICT)
    return out[0], float(out[1])/float(out[2])
