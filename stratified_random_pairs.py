import random

random.seed(100)

cellsCount = 10
cellId = 0

for i in range(500):
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

    print x, y
