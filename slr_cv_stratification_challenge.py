import random
import math

defaultFactor = 2
defaultIntercept = 10
defaultCount = 100

extraIntercept = 100
extraCount = 20

foldsCount = 10
strataCount = 10

evalsCount = 1000

def GenData(count):
    data = []
    for i in range(count):
        data.append([i, defaultFactor * i + defaultIntercept])
    for i in range(count, count + extraCount):
        data.append([i, defaultFactor * i + defaultIntercept + extraIntercept])
    return data

def SLRSolve(data):
    avgTarget = sum(map(lambda x : float(x[1]), data)) / len(data)
    avgVariable = sum(map(lambda x : float(x[0]), data)) / len(data)

    numerator = sum(map(lambda xy : (float(xy[0]) - avgVariable) * (xy[1] - avgTarget), data))
    denominator = sum(map(lambda xy : (float(xy[0]) - avgVariable) * (xy[0] - avgVariable), data))

    factor = float(numerator) / denominator
    intercept = avgTarget - factor * avgVariable

    return factor, intercept

def RMSE(model, data):
    sse = 0.
    for xy in data:
        residual = xy[0] * model[0] + model[1] - xy[1]
        sse += residual * residual
    rmse = math.sqrt(max(0., sse / len(data)))
    return rmse

def CrossValidationSplit(data, foldsCount):
    folds = []
    for foldIdx in range(foldsCount):
        folds.append([[], []])

    random.shuffle(data)
    for i in range(len(data)):
        testFoldIdx = i % foldsCount
        for foldIdx in range(foldsCount):
            if foldIdx == testFoldIdx:
                folds[foldIdx][1].append(data[i])
            else:
                folds[foldIdx][0].append(data[i])
    return folds

def CrossValidationStratifiedSplit(data, foldsCount):
    folds = []
    for foldIdx in range(foldsCount):
        folds.append([[],[]])

    data.sort(key = lambda x : x[0])

    globalIdx = 0
    for strataIdx in range(strataCount):
        startIdx = (strataIdx + 0) * len(data) / strataCount
        endIdx = (strataIdx + 1) * len(data) / strataCount

        dataSubset = data[startIdx : endIdx]
        random.shuffle(dataSubset)

        for instance in dataSubset:
            testFoldIdx = globalIdx % foldsCount
            globalIdx += 1

            for foldIdx in range(foldsCount):
                if foldIdx == testFoldIdx:
                    folds[foldIdx][1].append(instance)
                else:
                    folds[foldIdx][0].append(instance)
    return folds

def EvalFolds(folds):
    est = 0.
    for i in range(len(folds)):
        est += RMSE(SLRSolve(folds[i][0]), folds[i][1])
    return est / len(folds)

def TestCrossValidation(data, epochs, splitGen):
    random.seed(100)
    evals = []
    for epoch in range(epochs):
        folds = splitGen(data, foldsCount)
        evals.append(EvalFolds(folds))
    evals.sort()
    return evals

data = GenData(100)

cvResults = TestCrossValidation(data, evalsCount, CrossValidationSplit)
stratifiedResults = TestCrossValidation(data, evalsCount, CrossValidationStratifiedSplit)

for i in range(evalsCount):
    print cvResults[i], stratifiedResults[i]
