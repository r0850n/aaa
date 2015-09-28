'''
Created on 18 wrz 2015

@author: Penny
'''
import unittest
from pages.person import Person


class Test(unittest.TestCase):


    def testName(self):
        listaPersonow =[]
        
        person1= Person("aaa",12)
        person2 = Person('bbb',13)
        
        listaPersonow.append(person1)
        listaPersonow.append(person2)
        listaPersonow.append()
        print str(person1)
        print str(listaPersonow[0])
        
        person1.setName("nowe")
                
        print person1
        print person2
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()