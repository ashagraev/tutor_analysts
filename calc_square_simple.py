import random

random.seed(100)

radius = 0.4
pi = 3.1415926535

exactSquare = radius * radius * pi / 4

pointsInside = 0
totalPoints = 0

iterations = 100

errors = []

for epoch in range(100):
    for i in range(100):
        x, y = random.random(), random.random()

        sqDistanceFromOrigin = x * x + y * y
        if sqDistanceFromOrigin < radius * radius:
            pointsInside += 1
        totalPoints += 1

    errors.append(float(pointsInside) / totalPoints - exactSquare)

errors.sort()

print '\n'.join(map(str, errors))
