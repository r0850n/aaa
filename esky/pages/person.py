'''
Created on 18 wrz 2015

@author: Penny
'''

class Person(object):
    '''
    
    '''
    
    

    def __init__(self, name, age ):
        self.name = name
        self.age = age
        
    def setName(self,name):
        self.name = name
        
    def __str__(self):
        return str(self.name) +" "+ str(self.age)