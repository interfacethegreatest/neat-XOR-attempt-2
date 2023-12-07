#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:03:14 2023

@author: new
"""
# Initialize an empty lookup table
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
    nodeList = list()
    layerCount = 0
    
    
    
    def initInputNodes(self):
        '''
        Generate input Nodes,

        Returns
        -------
        None.

        '''
        for i in range(self.globalVariableObj.inputNodes):
            node = Node(self.nodeList.i, 0,0,0,0)
            self.nodeList.append(node)
            
        nodeBias = Node(self.globalVariableObj.inputNodes, 1,0,0,0)
        self.nodeList.append(nodeBias)
    
    def initHiddenNodes(self):
        '''
        test this and above function.

        Returns
        -------
        None.

        '''
        for i in range(self.globalVariableObj.hiddenNodes):
            node = Node(self.nodeList.len()-1, 2, self.layerCount,0,0)
            self.nodeList.append(node)
            
    
    
    
    
    
    def __init__(self, globalVariableObj = GlobalVariables):
        self.globalVariableObj = globalVariableObj
        if self.globalVariableObj.hiddenNodes == 0:
            layerCount = 1
        else:
            layerCount == 2
            
      

















