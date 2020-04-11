import random

random.seed(100)

radius = 0.4
pi = 3.1415926535

exactSquare = radius * radius * pi / 4

iterations = 100

errors = []

cellsCount = 10
cellId = 0

for epoch in range(100):
    pointsInside = 0
    totalPoints = 0
    for i in range(10000):
        cellVerticalIdx = (cellId / cellsCount) % cellsCount
        cellHorizontalIdx = cellId % cellsCount
        cellId += 1

        left = float(cellVerticalIdx + 0) / cellsCount
        right = float(cellVerticalIdx + 1) / cellsCount

        top = float(cellHorizontalIdx + 1) / cellsCount
        bottom = float(cellHorizontalIdx + 0) / cellsCount

        x, y = random.random(), random.random()
        x = left + x * (right - left)
        y = bottom + y * (top - bottom)

        sqDistanceFromOrigin = x * x + y * y
        if sqDistanceFromOrigin < radius * radius:
            pointsInside += 1
        totalPoints += 1

    errors.append(float(pointsInside) / totalPoints - exactSquare)

errors.sort()

print '\n'.join(map(str, errors))
