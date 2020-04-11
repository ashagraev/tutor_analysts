import random
import math

import numpy as np

freqs = []
for i in range(1000):
    freq = 1. / math.pow(i + 1, 1.5)
    freqs.append(freq)

sf = sum(freqs)
for i in range(len(freqs)):
    freqs[i] /= sf

def isGood(i):
    return freqs[i] > 0.01

tries = 10000

def goodFractionOne():
    goodCount = 0
    totalCount = 0

    random.seed(100)
    for i in range(tries):
        q = random.randint(0, len(freqs) - 1)
        if isGood(q):
            goodCount += 1
        totalCount += 1

    return float(goodCount) / totalCount

def goodFractionTwo():
    goodCount = 0.
    totalCount = 0.

    random.seed(100)
    for i in range(tries):
        q = random.randint(0, len(freqs) - 1)
        if isGood(q):
            goodCount += freqs[q]
        totalCount += freqs[q]

    return goodCount / totalCount

def goodFractionThree():
    goodCount = 0.
    totalCount = 0.

    numbers = []
    for i in range(len(freqs)):
        numbers.append(i)

    taken = np.random.choice(numbers, tries, p=freqs)
    for t in taken:
        if isGood(t):
            goodCount += 1
        totalCount += 1

    return goodCount / totalCount

print goodFractionOne(), goodFractionTwo(), goodFractionThree()
