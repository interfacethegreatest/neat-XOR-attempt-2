# -*- coding: utf-8 -*-

import random
from globalVariables import *
from BrainGui import *

class Speciate:
    '''
    ''' 
    def getCompareDifferenceCD(self, brainA, brainB):
        c1 = 1.0
        c2 = 1.0
        c3 = 0.4
        e = self.getExcessGenesE(brainA, brainB)
        d = self.getDisjointGenesD(brainA, brainB)
        w = self.getWeightAverageW(brainA, brainB)
        n = self.getLargestNetworkN(brainA, brainB)
        return ((e*c1)/n) + ((d*c2)/n) + (w*c3)
    
    
    
    def getLargestNetworkN(self, brainA, brainB):
     conLengthA = sum(1 for connection in brainA.connList if connection.ennabled)
     conLengthB = sum(1 for connection in brainB.connList if connection.ennabled)

     return max(conLengthA, conLengthB)

    
    def getWeightAverageW(self, brainA, brainB):
     innovation_weightsA = {connection.innovation_ID: connection.conn_Weight for connection in brainA.connList if connection.ennabled}
     innovation_weightsB = {connection.innovation_ID: connection.conn_Weight for connection in brainB.connList if connection.ennabled}

     total_weight = 0.0
     matching_count = 0

     for innovation_ID in innovation_weightsA:
        if innovation_ID in innovation_weightsB:
            total_weight += abs(innovation_weightsA[innovation_ID] - innovation_weightsB[innovation_ID])
            matching_count += 1

    # Avoid division by zero
     return total_weight / matching_count if matching_count > 0 else 0.0
      
        
    def getExcessGenesE(self, brainA, brainB):
        '''
        NEEDS TO BE TESTED ON LARGER NETWORKS
        Parameters
        ----------
        bNetA : Brain
            An object of type Brain stores in globalVariables.py.
        bNetB : TYPE
            DESCRIPTION.

        Returns
        -------
        The number of excess genes in bNetB that do not exist in bNetA.

        '''
        """Get the excess genes (Innovation IDs) in genome2 that do not exist in genome1."""
        """Excess genes are those outside the range of netA , """
        """first find the range of net A,"""
        """initialise obj holders"""
        lowerRangeID = None
        upperRangeID = None
        e = 0
        """ return list[obj0] and list[len(list)-1], i.e. upper and lower ranges"""
        lowerRangeID = brainA.connList[0]
        upperRangeID = brainA.connList[len(brainA.connList)-1]
        """ loop through brainB, if any list[i].innovation_ID is less than lowerRangeID or,
        greater than upperRangeID, increment e number by 1,"""
        for i in range(len(brainB.connList)):
            store = brainB.connList[i]
            if (brainB.connList[i].innovation_ID < lowerRangeID.innovation_ID or brainB.connList[i].innovation_ID > upperRangeID.innovation_ID) and (brainB.connList[i].ennabled):
              e+=1  
        return e
        
    def getDisjointGenesD(self, brainA, brainB):
        '''
        NEEDS TO BE TESTED ON LARGER NETWORKS
        '''
        
        def extract_innovation_ids(connections_list):
         '''
         Parameters
         ----------
         connections_list : List
             Lists all connections contained within the brain NN object.

         Returns
         -------
         innovation_ids : TYPE
             allows for checking of disjoint genes in list_a/b.

         '''
         innovation_ids = {conn.innovation_ID for conn in connections_list if conn.ennabled}
         return innovation_ids

        list_a = extract_innovation_ids(brainA.connList)
        list_b = extract_innovation_ids(brainB.connList)

        d = 0  # Counter for disjoint genes

         # Check for disjoint genes in list_a
        for gene_id in list_a:
          if gene_id not in list_b:
            d += 1

         # Check for disjoint genes in list_b
        for gene_id in list_b:
          if gene_id not in list_a:
            d += 1

        return d
 
 
    def speciateGen0(self, population):
        
    
        
                
                
        species.update({randomChoice:group})
        # compare to level 0, if less than threshold, pop and update,
        for 
        
        '''
        def recursiveSpeciate(group, dictionaryGrouping, brainOutThreshold, population) :
            groupN = group + 1
            for i in range(len(population)):
                if brainOutThreshold is not population[i] and self.getCompareDifferenceCD(brainOutThreshold, population[i]) >=4.0:
                    recursiveSpeciate(groupN, dictionaryGrouping,population[i], population)
                elif:
                    dictionaryGrouping.update({population[i] : group})
        group = 1
        group1obj = random.choice(population)
        dictionaryGrouping = dict()
        dictionaryGrouping.update({group1obj:group})
        for i in range(len(population)):
            if group1obj is not population[i] and self.getCompareDifferenceCD(group1obj, population[i]) >=4.0:
                recursiveSpeciate(group, dictionaryGrouping, population[i], population)
            elif group1obj is not population[i]:
                dictionaryGrouping.update({population[i] : group})
            else:
                pass
        '''
        
                    
                
                
        
       
 
    
     
         
         
     
     
     
    def __init__(self):
     parameters = GlobalVariables(2, 1, 0, 0)
     test = Run_Test(parameters)
     obj1 = test.outputs[1]
     obj2 = test.outputs[0]
     e = self.getExcessGenesE(obj1, obj2)
     d = self.getDisjointGenesD(obj1, obj2)
     w = self.getWeightAverageW(obj1, obj2)
     CD = self.getCompareDifferenceCD(obj1, obj2)
     self.speciateGen0(test.outputs)

     

def main():
    speciate = Speciate()

if __name__=="__main__": 
 outputs = main() 