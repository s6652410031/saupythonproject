# - Have parameters/Have returns
def dti1( a , b , c):
    print(f'{a} ยกกำลัง {b} =')
    return a ** b 

def dti2( a , b , x , y ) :
    return a + b + x + y + dti1( 2 , 3) , "wow wow owo"

x, y = dti2( 2 , 4 , 6 ,8 )

print(f'{x} UwU {y}')
    