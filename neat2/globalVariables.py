#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Initialize an empty lookup table
import random
import math
import numpy as np

x_max = 1000
y_max = 1000

# Create 2D arrays for x and y
x_values, y_values = np.meshgrid(np.arange(1, x_max + 1), np.arange(1, y_max + 1), indexing='ij')

# Calculate the unique variable using vectorized operations
lookup_table = (x_values - 1) * y_max + y_values
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
    sumInput = int()
    sumOutput = int()
    
    def __init__(self, nodeID, nodeT, nodeLayer, sum_Input, sum_Output):
        self.nodeIdentifier = nodeID
        self.nodeType = self.nodeTypeList[nodeT]
        self.nodeLayer = nodeLayer
        self.sumInput = sum_Input
        self.sumOutput = sum_Output
        
    def __str__(self):
        return f'ID:{self.sumOutput}                                           '
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
      
    def __str__(self):
        return f'{self.innovation_ID} : {self.conn_Weight}          '   
class Brain():
    
    globalVariableObj = None
    nodeList = []
    connList = []
    layerCount = 0
    layers = None
    nodeLayer = tuple()
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
        
       
        
        def initOutputHiddenConnections():
            threshold = self.globalVariableObj.percentageConnections
            for z in range(self.globalVariableObj.outputNodes):
                outputNode = self.nodeList[self.globalVariableObj.inputNodes+self.globalVariableObj.hiddenNodes+1+z]
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
               hiddenLoc = hiddenNode.nodeIdentifier
               for y in range (self.globalVariableObj.inputNodes+1):
                   inputNode = self.nodeList[y]
                   inputLoc = inputNode.nodeIdentifier
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
        self.nodeLayer = (self.globalVariableObj.inputNodes+1, self.globalVariableObj.hiddenNodes, self.globalVariableObj.outputNodes)
        if self.globalVariableObj.hiddenNodes == 0:
            self.layerCount == 1
            self.layers ==2
        else:
            self.layerCount == 2
            self.layers == 3
        self.initNodes()
        self.initConnections()
        
    def loadInputs(self, inputList = tuple()):
        if len(inputList) != self.globalVariableObj.inputNodes:
            raise Exception('Inputs are not equal to input layer nodes.')
        else:   
         for i in range(self.globalVariableObj.inputNodes+1):
          if self.nodeList[i].nodeType != 'Bias':
            self.nodeList[i].sumInput = inputList[i]
            self.nodeList[i].sumOutput = inputList[i]
         else:
            self.nodeList[i].sumInput = 1
            self.nodeList[i].sumOutput = 1
            
    def run_network(self):
        for i in range(len(self.nodeList)):
            if self.nodeList[i].nodeType in ['Hidden', 'Output']:
                sumOutputs = list()
                nodeID = self.nodeList[i].nodeIdentifier
                for y in range(len(self.connList)):
                    out = self.connList[y].out_Node_ID
                    if out == nodeID and self.connList[y].ennabled:
                        output = self.nodeList[self.connList[y].in_node_ID-1].sumOutput
                        sumOutputs.append(output*self.connList[y].conn_Weight)
                self.nodeList[i].sumInput = sum(sumOutputs)
                finalNodeOutput = 1/(1+ math.exp(-(sum(sumOutputs))))
                self.nodeList[i].sumOutput = finalNodeOutput
                
    def get_output(self):
        outputs = list()
        for i in range(len(self.nodeList)):
            if self.nodeList[i].nodeType in ['Output']:
                outputs.append(self.nodeList[i].sumOutput)
        return outputs
                
                    
    
def main():
 test = GlobalVariables(3,1,0,0) 
 for i in range(50):
  BRAIN = Brain(test)
  BRAIN.loadInputs((0,0,1))
  BRAIN.run_network()
  outputs = BRAIN.get_output()
  x=5
 



if __name__=="__main__": 
    main() 










