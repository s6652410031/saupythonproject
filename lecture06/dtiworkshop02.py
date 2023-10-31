def inputCarDetail():
    carNo = input('Car Registration Number: ')
    carWeight = float(input('Car Weight: '))
    return carNo,carWeight

def checkCarAndShowWeight(carNo,carWeight) :
    if carWeight > 1000:
        print(f'{carNo} NOT PASS')
    else :
        print(f'{carNo} PASS')    


print('+++++++++++++++++++++++++++++++++++++++++')
print(" Truck Checker ")
print('+++++++++++++++++++++++++++++++++++++++++')
carNo,carWeight = inputCarDetail()
print('+++++++++++++++++++++++++++++++++++++++++')
checkCarAndShowWeight(carNo,carWeight)
print('+++++++++++++++++++++++++++++++++++++++++')