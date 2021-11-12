import random
numList = []
random.seed(150)
for i in range(0,25):
    numList.append(round(100*random.random(),1))
    
import statistics

def problem4_2(l):
    print(statistics.mean(l))
    print(statistics.stdev(l))

