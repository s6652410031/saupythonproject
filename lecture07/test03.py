# list method
var1 = [10 , 20 , 'Hello' , True , [111, 'wow'],'ก้อง']
# append
var1.append(555)
var1.append({'Hi','Hey',999})
print(var1)
# extend
var1.extend([10,20,30])
print(var1)
# remove
var1.remove('Hello')
var1.remove(10)
print(var1)
# ------------------
var2 = [10,20,'Hello']
# insert
var2.insert(2,'Hi')
print(var2)
# pop
var2.pop()
print(var2) # [10,20,'Hi]
var2.pop(1)
print(var2)
# index
print(var2.index('Hi'))
# count
print(var1.count(10))
var3 = [10,20,30,'Hi',10,'Hi']
print(f' ใน var3 มี 10 ทั้งหมด{var3.count(10)}ตัว')
print(f' ใน var3 มี Hi ทั้งหมด{var3.count("Hi")}ตัว')
print('Hi\'SAU\'')
print('Hi \'SAU\'')
print('Hi\'SAU\'')
print('Hi\'SAU\'')
print('Hi\'SAU\'')

# sort
var4 = [10,20,30,'Hi',10,'Hi']
var4.sort()
var5=[99,34,635,3423,99]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse)
print(var5)