#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Initialize an empty lookup table
import random

lookup_table = {}

# Set the maximum values for x and y
x_max = 1000
y_max = 1000

# Populate the lookup table with unique integer variables for each combination of x and y
for x in range(1, x_max + 1):
    for y in range(1, y_max + 1):
        unique_variable = (x - 1) * y_max + y  # Adjust this formula based on your requirements
        lookup_table[(x, y)] = unique_variable




class GlobalVariables:
    
  inputNodes = int()
  outputNodes = int()
  hiddenNodes = int()
  percentageConnections = float()
  
    
  def __init__(self, inputN, outputN, hiddenN, percConnection):
    self.inputNodes = inputN
    self.outputNodes = outputN
    self.hiddenNodes = hiddenN
    self.percentageConnections = percConnection 
    

class Node:
    
    nodeIdentifier = int()
    nodeTypeList = ('I/P', 'Bias', 'Hidden', 'Output')
    '''
    store selection of nodeType
    '''
    nodeType = str()
    nodeLayer = int()
    sum_Input = int()
    sum_Output = int()
    
    def __init__(self, nodeID, nodeT, nodeLayer, sum_Input, sum_Output):
        self.nodeIdentifier = nodeID
        self.nodeType = self.nodeTypeList[nodeT]
        self.nodeLayer = nodeLayer
        self.sum_Input = sum_Input
        self.sum_Output = sum_Output
        

class Connections:
    
    innovation_ID = int()
    in_node_ID = int()
    out_Node_ID = int()
    conn_Weight = float()
    ennabled = bool()
    is_Recurrent = bool()
    
    def __init__(self, in_Nodes, out_Nodes,conn_Weight, ennabled, is_Recurrent):
      self.in_node_ID = in_Nodes
      self.out_Node_ID = out_Nodes
      self.conn_Weight = conn_Weight
      self.ennabled = ennabled
      self.is_Recurrent = is_Recurrent
      self.innovation_ID = lookup_table[self.in_node_ID,self.out_Node_ID]
      
     
        
class Brain():
    
    globalVariableObj = None
    nodeList = []
    connList = []
    layerCount = 0
    
    
    
    def initNodes(self):
        '''
        Generate input Nodes,

        Returns
        -------
        None.

        '''
        '''
        input & bias node initiation
        '''
        for i in range(self.globalVariableObj.inputNodes):
            node = Node(i+1, 0,0,0,0)
            self.nodeList.append(node)
            
        nodeBias = Node(self.globalVariableObj.inputNodes+1, 1,0,0,0)
        '''
        hidden node initiation.
        '''
        self.nodeList.append(nodeBias)
        self.layerCount+=1
        for i in range(self.globalVariableObj.hiddenNodes):
            node = Node(len(self.nodeList)+1, 2, self.layerCount,0,0)
            self.nodeList.append(node)
        self.layerCount+=1
        '''
        output node initiation
        '''
        for i in range(self.globalVariableObj.outputNodes):
            node = Node(len(self.nodeList)+1, 3, self.layerCount, 0,0)
            self.nodeList.append(node)
    
    
    def initConnections(self):
        
        '''
        validate tomorrrow.
        '''
        
        def initOutputHiddenConnections():
            threshold = self.globalVariableObj.percentageConnections
            for x in range(self.globalVariableObj.outputNodes):
                outputNode = self.connList[self.globalVariableObj.inputNodes+self.globalVariableObj.hiddenNodes+1+x]
                for y in range(self.globalVariableObj.hiddenNodes):
                   hiddenNode = self.nodeList[y+self.globalVariableObj.inputNodes+1]
                   randomNumber = random.random()
                   if randomNumber >= threshold:
                       setEnnabled = True
                   else:
                       setEnnabled = False
                   connection = Connections(hiddenNode.nodeIdentifier, outputNode.nodeIdentifier, 
                                            random.randint(-10, 10), setEnnabled, False)
                   self.connList.append(connection)
        
        def initHiddenInputConnections():
            for x in range(self.globalVariableObj.hiddenNodes):
               hiddenNode = self.nodeList[x+self.globalVariableObj.inputNodes+1]
               for y in range (self.globalVariableObj.inputNodes):
                   inputNode = self.nodeList[y]
                   randomNumber = random.random()
                   if randomNumber >= self.globalVariableObj.percentageConnections:
                       setEnnabled = True
                   else:
                       setEnnabled = False
                   connection = Connections(inputNode.nodeIdentifier, hiddenNode.nodeIdentifier,
                                            random.randint(-10,10), setEnnabled, False)
                   self.connList.append(connection)
        
        initHiddenInputConnections()
        initOutputHiddenConnections()
         
         
    
    
    
    def __init__(self, globalVariableObj = GlobalVariables):
        self.globalVariableObj = globalVariableObj
        if self.globalVariableObj.hiddenNodes == 0:
            self.layerCount = 1
        else:
            self.layerCount == 2
        self.initNodes()

            
      
def main():
 test = GlobalVariables(3,3,1,0.45) 
   
 BRAIN = Brain(test)



if __name__=="__main__": 
    main() 










