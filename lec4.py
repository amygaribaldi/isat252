"""
lec 4, tuple and dictionary
"""
my_tuple = 'a','b','c','d','e'
#print(my_tuple)

my_2nd_tuple = ('a','b','c','d','e')
#print(my_2nd_tuple)
   #('a') is not a tuple, it is a str. Tuple needs commas --> ('a',).
   
#print(my_tuple[0])
#print(my_tuple[1:3])
#print(my_tuple[:])
   # [1:3] value on left is inclusive (from that point on). Value on right is exclusive(will give everything before then)

my_car = {
         'color':'red',
         'maker':'toyota',
         'year': 2015
         }
#print(my_car)
#print(my_car['color'])
#print(my_car.items())
#print(my_car.keys())
#print(my_car.values())
#print(my_car.get('year'))

#my_car['model'] = 'corolla'
#my_car['year'] = 2020
#print(my_car)
#print(len(my_car))
#print('mile' in my_car) --> result is False