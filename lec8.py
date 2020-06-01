"""
lec 8
"""
#functions

#def my_function(a,b=0):
#    result = a + b
#    print('a is ',a)
#    print('b is ',b)
#    return result
#print(my_function(1,2))

#ex1
#def calculate_abs(a):
#    if type(a) is str:
#        return('wrong data type')
#    elif a>0:
#        return a
#    else:
#        return -a
#print(calculate_abs('a'))
#print(calculate_abs(0)) --> result will be None

#ex2

#result = 0
#for i in range(3,6):
#    result = result + i
#print(result)

result = 0
for i in range(2,9):
    result = result +i
#print(result)

def cal_sigma(m,n):
    result=0
    for i in range(n,m+1):
        result = result +i
    return result
#print(cal_sigma(5,3))

'''
calculate pi (n,m)
'''
def cal_pi(m,n):
    result = 1
    for i in range(n,m+1):
        result = result*i
    return result
#print(cal_pi(5,3))

#ex3
def cal_f(m):
    if m ==0:
        return 1
    else:
        return m * cal_f(m-1)
#print(cal_f(3))

def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
print(cal_p(5,3))