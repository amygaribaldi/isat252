"""
lecture notes for day 3 week 1
"""
my_list = [1,2,3,4,5]
#print(my_list)

my_nested_list = [1,2,3,my_list]
#print(my_nested_list)

#print(my_list[0])
my_list[0]=6
#print(my_list)
#print(my_list[0])
#print(my_list[-1])

#print(my_list[0:2])
#print(my_list[0:3])
   #in [] are the indexes of numbers you want
   #item of last index wont be listed. Right side of : means everything before then
   #index of 4 is 3, index of 1 is 0

#my_letters = ['a','b','c']
#print(my_letters[2])
   #print(my_letters[3]) --> error because not enough variables
#print(my_letters[0:1])
#print(my_letters[:3])
   #gives you everything before index 3
#print(my_list[3:])
#print(my_list[:])

x,y,z = ['a','b','c']
#print(x)
#print(y)
#print(z)
   #x,y = ['a','b','c'] --> error, need equal amount on both sides

#my_list.append(7)
#print(my_list)
#my_list.remove(7)
#print(my_list)

#my_list.sort()
#print(my_list)

#my_list.reverse()
#print(my_list)

#print(my_list)
#print(my_list + [8,9])
   #same as extend function
#my_list.extend([8,9])
#print(my_list)
#my_list.extend(['a','b'])
#print(my_list)

#print(my_list)
#print(6 in my_list)
   #result will be 'True'
#print(0 in my_list)
   #result will be 'False'
#print('6' in my_list)
   #result will be 'False' --> '' make it a string

#print(len(my_list))

#print('hello\tworld')
#print('hello\nworld')
#print(len('helloworld'))
#print('hello world'[0])
   #result is h
   #print('hello world'[11]) --> error bc last index is 10
   
my_letters = ['a','a','b','b','c']
#print(my_letters)
#print(set(my_letters))

#my_unique_letters = set(my_letters)
#print(my_unique_letters)
#print(len(my_unique_letters))
   #result is 3
#print('a' in my_unique_letters)
   #result is 'True'
   #print(my_unique_letters[0]) --> error because set does not support index
#print(list(my_unique_letters)[0])
