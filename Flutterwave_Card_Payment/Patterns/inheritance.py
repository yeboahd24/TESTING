#usr/bin/python

# Inheritance
class Duck:
    pass

    def fly(self):
        pass
    
    def swim(self):
        pass
    
    def quack(self):
        pass
    
class ReadHeadDuck(Duck):
    
    def display(self): # override display method
        pass
    
class RubberDuck(Duck):
    '''NB: this is not pythonic since Rubber Duck do not quack,
        You rather over burden the class.
        You may try to tweak/override but that is the right way
        I think using  interface can  solve this issue
    '''
    pass


    
    
    
    