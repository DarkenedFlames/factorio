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
    return lowerLimit < number < upperLimit

def listLCD(floats):
    denominators = [Fraction(float(f)).limit_denominator().denominator for f in floats]
    return np.lcm.reduce(denominators)

def machineCount(product, tier):
    r = speed[tier-1]*batch/time
    R_inv = np.linalg.inv(counts)

    o = item.index(product)
    w = r[o]*R_inv[o]/r
    M = (w * listLCD(w)).tolist()

    output = {item[x]: round(M[x], 3) for x in range(len(M)) if not between(M[x], -1, 1)}
    return output

print(machineCount("electronic_circuit",3))
