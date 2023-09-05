import math
# inputRadius

def inputRadius():
    r = float(input('Radius: '))
    return r

# calAreaCircle
def calAreaCircle(r):
    area = math.pi * r ** 2
    return math.pi * r ** 2

# calRoundCircle
def calRoundCircle(r):
    rd = 2 * math.pi * r
    return rd

# calCubeCircle
def calCubeCircle(r):
    c = (4/3) * math.pi * r ** 3
    return c

#showResult
radius = inputRadius()
print(f'Area of Circle: {area:.2f}')
print(f'Round of Circle: {rd:.2f}')
print(f'Volume of Circle: {c:.2f}')
