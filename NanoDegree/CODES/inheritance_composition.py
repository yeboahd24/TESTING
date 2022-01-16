from abc import ABC, abstractmethod

# Interface
class Bird(ABC):
    
    @abstractmethod
    def hasBeak(self):
        pass
    
    @abstractmethod
    def canFly(self):
        pass
    
    
# Inheritance
class CommonBird(Bird):
    
    def hasBeak(self):
        return True
    
    def canFly(self):
        return True
    

        
    
# Composition
class CommonBird2(Bird):
                
    def hasBeak(self):
        return True
    
    def canFly(self):
        return True
        

class Penguin:
    
    def __init__(self):
        self.bird = CommonBird2()
        
    def canFly(self):
        return False if self.bird.canFly() else True
    
    def hasBeak(self):
        return self.bird.hasBeak()
    
    
print(Penguin().hasBeak())
print(Penguin().canFly())
    


        
