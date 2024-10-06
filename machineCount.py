import numpy as np
import math
from recipeInfo import time, counts, batch, item, speed
from fractions import Fraction
from collections import defaultdict

time = np.array(time)
counts = np.array(counts)
batch = np.array(batch)
speed = np.array(speed)



def between(number, lowerLimit, upperLimit):
    if number > lowerLimit and number < upperLimit:
        return True
    return False

def listLCD(floats):
    floats_list = [float(f) for f in np.array(floats).flatten()]
    denominators = [Fraction(f).limit_denominator().denominator for f in floats_list]
    return np.lcm.reduce(denominators)

def machineCount(product, tier):
    r = speed[tier-1]*batch/time
    R_inv = np.linalg.inv(np.array(counts))

    o = item.index(product)
    w = r[o]*R_inv[o]/r
    M = (w * listLCD(w)).tolist()
    output = defaultdict(list)
    for x in range(0,len(M)):
        if not between(M[x],-1,1):
            output[item[x]] = round(M[x],3)
    return output

print(machineCount("electronic_circuit",3))

