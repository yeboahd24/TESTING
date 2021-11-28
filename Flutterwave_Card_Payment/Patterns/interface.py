#!usr/bin/python

class Duck:
    pass

    def swim(self):
      pass

# interfaces

# NB: interface of inheriting we create a separate interface or class
# This makes your code clean beacuse you do not over burden the class
class Fly:
    pass

    def fly(self):
        pass
    
class Quack:
    pass

    def quack(self):
        pass
    
class RubberDuck(Duck):
    pass

class ReadHeadDuck(Duck, Fly, Quack):
    '''You can now override the methods'''
    pass