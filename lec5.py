"""
lec 5
"""

#import this

#print(1 + 2)     --> white space is ignored inside () and []
#m = 1+\
#      2          --> can also avoid error with \ to move to next line without () or []
#print(m)

#a = 123
#print(id(123))
#print(id(a))      --> have the same id

#a = [1,2,3]
#b = [1,2,3]
#print(a==b)       --> result is True because they have the same values
#print(a is b)     --> result is False because they have different ids

#x = None
#print(x is None)  --> True, have same id
#print(x==None)    --> True, have same value

#y = []
#print(type(y))    --> y is an empty list
#print(y==None)    --> False because an empty list is not None

#print(True and False) --> x is true so we will return y (False)
#print(True or False)
#print(not False)      --> True
#print(not True)       --> False
       # x or y : if x is False, then y, else x
       # x and y : if x is False, then x, else y
       # not x : if x is False, then True, else False
       # Empty data containers, empty strings, int 0 and float 0.0, None are all considered False

#print(not None)    --> None data type is considered False, so result is True
#print(not '0')     --> 'O' is a string. Empty string '' and 0 are False, but '0' is True, so result is False
#print(() and [])   --> result is () because x is False so return x

#if 2<=1 :
    #print('2<=1')
    
#if 2>1 :
    #if 1.5<1:
        #print('1.5<1')
    #print('2>1')
        # conditional test 2>1 is True so it is printed
        # conditional test 2<=1 is False so it is not printed
        # indent is automatic part of code, make sure to keep it!
        # dont forget : !!
#if 2<=1 :
    #print('2<=1')
#elif 2<=2:
    #print('2<=2')
#else:
    #print('2>1')

if None:
    print(1)
elif {}:
    print(2)
elif '0':
    print(3)
else:
    print(4)
        # result is 3 because first two conditions are False