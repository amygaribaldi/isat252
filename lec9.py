"""
lec 9
"""

#class car:                            #define a class
#    maker= 'toyota'                   #dont HAVE to define an attribute
#    def report_maker(self):           #method
#        return(self.maker)
#my_car = car()                        #create an instance/ object
#print(my_car.report_maker())


#class car:
#    maker = 'toyota'
#    def __init__(self,input_model):
#        self.model = input_model

#my_corolla = car('corolla')
#print(my_corolla.maker)
#print(my_corolla.model)

#my_highlander = car('highlander')
#print(my_highlander.maker)
#print(my_highlander.model)


class car:                             #car is the class name
    maker = 'toyota'                   #attribute
    def __init__(self,input_model):
        self.model = input_model       #unique attribute
    def report(self):
        #return the attribute of the instance
        return self.maker,self.model
my_car = car('corolla')
print(my_car.report())

my_car.maker = 'ford'
#print(my_car.report())


