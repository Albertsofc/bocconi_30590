'''
TOPIC: classes

SUMMARY: classes create objects, which have both properties (variables) and methods (function)
creation of a class is its own function - def __init__

AUTHOR: Olivia Alberts (alber585@umn.edu)
'''

import datetime

class Person:
    
    
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        
    def age(self):
        age = datetime.datetime.today() - self.birthdate
        return (age.days // 365)
        
# use this to test the function
if __name__ == '__main__':
    '''
    TIP: the order of parameters doesn't matter if you use the "first_name = x" 
    strudcture within the function call (like in p1 and p2). if you don't 
    use the variable name in the call (like in p3), the order does matter; 
    it needs to be exactly the same as in the __init__ function.
    '''
    
    p1 = Person(first_name = 'Mickey', last_name = 'Mouse', birthdate = '19300113')
    print("p1 name: " + p1.first_name)
    p2 = Person(last_name = 'Mouse', first_name = 'Mickey2', birthdate = '19300113')
    print("p2 name: " + p2.first_name)
    p3 = Person('Mickey3', 'Mouse', '19300113')
    print("p3 name: " + p3.first_name)
    
    '''
    TIP: type dir(p1) in the IPython console to see all of the different
    properties and methods within the class
    '''
    
    '''
    TIP: use the datetime library (imported on line 6)
    we can call datetime.datetime.strptime(original_string, input_format) to 
    turn our string into a datetime object.
    original string = whatever you input
    input_format = this string explains to the computer how to decode your 
    original_string.
        %Y says four characters will correlate to the year of your datetime object
        %m says 2 characters will correlate to the montho f your datetime object
        %d says 2 characters will correlate to the day of your datetime object
    the way you order them will change how your original_string is read into 
    the datetime object.
    
    '''
    p1_using_datetime = Person(first_name = 'Mickey', 
                               last_name = 'Mouse', 
                               birthdate = datetime.datetime.strptime('19300113','%Y%m%d'))
    print(p1_using_datetime.age())
                                                                 
