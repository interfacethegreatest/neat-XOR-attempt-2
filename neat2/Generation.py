from globalVariables import *
from Speciation import *
from Crossover import *
from BrainGui import *
from Speciation import *

class Generation:
    
    
    def __init__(self):
        self.generation = 0
        self.speciesTargetSize = 50
        self.compatibilityThreshold = 99
        self.variables = GlobalVariables(2, 1, 0, 0)
        self.test = Run_Test(self.variables, self.speciesTargetSize)
        self.speciate = Speciate(self.test, self.speciesTargetSize, self.compatibilityThreshold)
        self.crossOver = CrossOver(self.compatibilityThreshold, self.speciate)
        
    #def generation():
        #Run_Test()
        
        
    #def run(numberofgens, )




def main():
 test = Generation()
    
if __name__ == "__main__":
 main()