# - Have parameters/No return   
def funcA( x, y) :
    print('AAA')
    z = x + y 
    print(f'{x} + {y} = {z}')
    funcB(10,20,30)

def funcA(x, y ,z):
    print('{:.2f} {:.4f} {:.6f}'.format(x, y ,z)) 

funcA(10 , 20)
funcA(5 , 10)
funcB( 1, 5 ,10)       