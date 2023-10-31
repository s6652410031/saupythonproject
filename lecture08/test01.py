# List
my_list = (10,20,30,'Hi',True,{20,'Hello'})
print(my_list)
# Tuple
my_Tuple = (10,20,30,'Hi',True,{20,'Hello'})
print(my_Tuple)
print(len,my_Tuple)
#Set
my_set = (10,20,30, 'Hi',True)                        
print(my_set)
print(len,my_set)

for data in my_list :
    print(data, end='/')

print('---------------------------------')

list_fr_set = list(my_set)
print(list_fr_set)
list_fr_set[0] = 'DTI'
my_set = set(list_fr_set)
print(my_set)

my_set.clear()
print(len,(my_set))

my_set1 = (10,20,30,'Hi')
my_set2 = (10,'Hello','Hi',True)

my_set1.add(999)
print(my_set1)
my_set1.remove('Hi')
print(my_set1)

print(my_set.intersection(my_set2))
print(my_set.union(my_set2))