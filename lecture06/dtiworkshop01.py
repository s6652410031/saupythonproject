def inputBaseHigh():
    base = float(input('Base :'))
    high = float(input('High :'))
    return base , high

def calAndShowTriangleArea(base , high):
    area = base * high / 2
    print(f'Triangle base {base:.2f} High {high:.2f} Total Area {area:.2f}')



print('+++++++++++++++++++++++++++++++')
print('Calculate Triangle Area')
print('+++++++++++++++++++++++++++++++')
base,high = inputBaseHigh()
print('+++++++++++++++++++++++++++++++')
calAndShowTriangleArea(base,high)
print('+++++++++++++++++++++++++++++++')