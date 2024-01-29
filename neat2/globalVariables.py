#annotate add connection and add node, 02/01/2024 -

# Initialize an empty lookup table
import random
import math
import numpy as np
from BrainGui import *

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
        return f'ID {self.nodeIdentifier} : Output {self.sumOutput} : Layer : {self.nodeLayer}                                          '
class Connections:
    
    innovation_ID = int()
    in_node_ID = int()
    out_Node_ID = int()
    conn_Weight = float()
    ennabled = bool()
    is_Recurrent = bool()
    connectionLayer = int()
    
    def __init__(self, in_Nodes, out_Nodes,conn_Weight, ennabled, is_Recurrent):
      self.in_node_ID = in_Nodes
      self.out_Node_ID = out_Nodes
      self.conn_Weight = conn_Weight
      self.ennabled = ennabled
      self.is_Recurrent = is_Recurrent
      self.innovation_ID = lookup_table[self.in_node_ID,self.out_Node_ID]
      
    def __str__(self):
        return f'{self.in_node_ID}-->{self.out_Node_ID} W({self.conn_Weight})         '
    
class Brain():
    
    
    def getNodesAtLayer(self, layer = int):
        
        '''
        returns list of nodes at a certain layer
        '''
        return [node for node in self.nodeList if node.nodeLayer == layer]

            
    def getNodesInOrder(self):
        orderedNodeList = list()
        counter= 1
        while counter <= self.layerCount:
            orderedNodeList += self.getNodesAtLayer(counter)
            counter+=1
        return orderedNodeList
        
        
        
    def addNode(self,):
        
      def getNodeLayer(self, layerCount, node = Node): 
          
          
          
        while node.nodeType not in ('Output'):
         #return the list of connection objects which connect to node.
         connections = [connection for connection in self.connList if connection.in_node_ID == node.nodeIdentifier and connection.ennabled == True and connection.is_Recurrent == False]
        
         #return the list of nodes which end at the given connection in the connections list,
         node_Connections = [node for connection in connections for node in self.nodeList if node.nodeIdentifier == connection.out_Node_ID]
        
         layerCount+=1
         for node in node_Connections:
            if layerCount > node.nodeLayer:
                if layerCount > self.layerCount:
                    self.layerCount = layerCount
                node.nodeLayer = layerCount
            getNodeLayer(self,layerCount, node)
            
        
    
        #select a random ENNABLED connection as the place for the node.
      randomConnection = None
      while randomConnection is None or randomConnection.ennabled == False or randomConnection.is_Recurrent == True:
       randomConnection = random.choice(self.connList)
       inID = randomConnection.in_node_ID
       outID = randomConnection.out_Node_ID
      newNode = Node(len(self.nodeList)+1, 2, 0, 0, 0)
      self.nodeList.append(newNode)
      randomConnection.ennabled == False
      index = self.connList.index(randomConnection)
      self.connList.pop(index)
      # generate two new connections
      firstConnection = Connections(self.nodeList[inID-1].nodeIdentifier, newNode.nodeIdentifier,
                                    randomConnection.conn_Weight, True, False)
      secondConnection = Connections(newNode.nodeIdentifier, self.nodeList[outID-1].nodeIdentifier,
                                    random.randint(-10, 10), True, False)
      self.connList.append(firstConnection)
      self.connList.append(secondConnection)
      #loop through node list,
      for node in self.nodeList:
              getNodeLayer(self, 1, node)
          
    
    
    
    def addConnection(self, isValid = bool, isRecurrent = bool, count = int):
        '''
        Could use further testing
        Recursive function used to validate nodes and generate a new connection.
        Conditions are:
            nodes cannot be same in and out node
            nodes connot be in same layer
            cannot be already existing connection

        Parameters
        ----------
        isValid : TYPE, bool
            Used to confirm the connection is valid and break the recursive function. The default is False to ennable recursion.
        isRecurrent : TYPE, bool
            Set by the user to determine whether recursive functions are turned off for the connection. The default is bool.
        Returns
        -------
        A new connection in self.connList.

        '''
        if count > 20:
            isValid = True
        while isValid == False:
         count+=1
         #generate two different loops whether if recurrent or not,
         if isRecurrent:
             #select two nodes at random,
              inNode = random.choice(self.nodeList)
              outNode = random.choice(self.nodeList)
              # generate an ID which , if connected they would create,
              potentialID = lookup_table[inNode.nodeIdentifier, outNode.nodeIdentifier]
              #the next three if conditions, look for conditions mentioned above in the greentext,
              # these are incorrect conditions
              #if the connection already exists,
              if any(connection.innovation_ID == potentialID for connection in self.connList):
                  #recall the recursive function
                  self.addConnection(isValid, isRecurrent, count)
                  #for the already existing connection, there is a 25 % chance to re-ennable the connection.
                  matching_connection = next((connection for connection in self.connList if connection.innovation_ID == potentialID), None) 
                  if matching_connection.ennabled == False:
                      if random.random() >= 0.75:
                          matching_connection.ennabled == True
                  #break out of the recursion once an incorrect selection is found.
                  break
            # if the randomly selected nodes are the same,
              if inNode == outNode:
                  # recursively call the function,
                  self.addConnection(isValid, isRecurrent, count)
                  break
              # if the randomly selected nodes are in the same layer, recursively call the function
              if inNode.nodeLayer == outNode.nodeLayer:
                  self.addConnection(isValid, isRecurrent, count)
                  break
              isValid = True
              check = random.random()
              #if the random nodes do not occupy the incorrect conditions, there is a 95% chance to ,
              #generate a connection between the randomly selected nodes,
              if check >=0.95:
               newConnection = Connections(inNode.nodeIdentifier, outNode.nodeIdentifier, random.randint(-10, 10), True, isRecurrent)
               # if the connection goes backwards, set recurrent to true
               if inNode.nodeLayer > outNode.nodeLayer:
                   newConnection.is_Recurrent = True
               else:
                   newConnection.is_Recurrent = False
               self.connList.append(newConnection)
         else:
             #else if the add a connection sets, recurrent to false, add this fact to the list of conditions to recursively,
             #call the function again,
                inNode = random.choice(self.nodeList)
                outNode = random.choice(self.nodeList)
                potentialID = lookup_table[inNode.nodeIdentifier, outNode.nodeIdentifier]
                if any(connection.innovation_ID == potentialID for connection in self.connList):
                    self.addConnection(isValid, isRecurrent, count)
                    break
                if inNode == outNode:
                    self.addConnection(isValid, isRecurrent, count)
                    break
                if inNode.nodeLayer == outNode.nodeLayer:
                    self.addConnection(isValid, isRecurrent, count)
                    break
                if inNode.nodeLayer > outNode.nodeLayer:
                    self.addConnection(isValid, isRecurrent, count)
                    break
                isValid = True 
                check = random.random()
                if check >=0.95:
                 newConnection = Connections(inNode, outNode, random.randint(-10, 10), self.globalVariableObj.percentageConnections > random.random(), isRecurrent)
                 self.connList.append(newConnection)
             
            
            
             
        
        
    def mutate(self):
        if random.random() >= 0.8:
         for connection in self.connList:
             if random.random() <=0.1:
                 connection.conn_Weight = random.randint(-10, 10)
             else:
                 coinflip = random.randint(1, 2)
                 weightAdjustment = connection.conn_Weight *0.2
                 if coinflip == 1 :
                     connection.conn_Weight + weightAdjustment
                 else:
                     connection.conn_Weight - weightAdjustment
                     
                
    
    
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
            node = Node(i+1, 0,1,0,0)
            self.nodeList.append(node)
            
        nodeBias = Node(self.globalVariableObj.inputNodes+1, 1,1,0,0)
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
            if self.globalVariableObj.hiddenNodes == 0:
                layers = 2
            else:
                layers = 3
            node = Node(len(self.nodeList)+1, 3, layers, 0,0)
            self.nodeList.append(node)
            
    def initConnections(self):
        
       
        def initInputOutputConnections():
         threshold = self.globalVariableObj.percentageConnections
         for z in range(self.globalVariableObj.outputNodes):
            outputNode = self.nodeList[self.globalVariableObj.inputNodes + self.globalVariableObj.hiddenNodes + 1 + z]
            for y in range (self.globalVariableObj.inputNodes+1):
                inputNode = self.nodeList[y]
                randomNumber = random.random()
                if randomNumber >= threshold:
                    setEnnabled = True
                else:
                    setEnnabled = False
                connection = Connections(inputNode.nodeIdentifier, outputNode.nodeIdentifier,
                                         random.randint(-10, 10), setEnnabled, False)
                self.connList.append(connection)
                
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
        if self.globalVariableObj.hiddenNodes !=0:     
         initHiddenInputConnections()
         initOutputHiddenConnections()
        else:
            initInputOutputConnections()
    
    def __init__(self, globalVariableObj = GlobalVariables):
        self.globalVariableObj = globalVariableObj
        self.nodeList = []
        self.connList = []
        self.layerCount=0
        self.layers = None
        if self.globalVariableObj.hiddenNodes == 0:
            self.layerCount == 1
            self.layers ==2
            self.initNodes()
            self.initConnections()
        else:
            self.layerCount == 2
            self.layers == 3
            self.initNodes()
            self.initConnections()
        
    def loadInputs(self, inputList = tuple()):
        '''
        Load's input values into array'

        Parameters
        ----------
        inputList : TYPE, tuple
            DESCRIPTION. Load's input values into array, ignoring the bias node.'

        Raises
        ------
        Exception
            DESCRIPTION.

        Returns
        -------
        None.

        '''    
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
    
            
    def run_network_node(self, node = Node):
        for i in range(len(self.connList)):
            if self.connList[i].out_Node_ID == node.nodeIdentifier and self.connList[i].ennabled:
                connection_weight = self.connList
                
    
    def run_network(self):
        '''
        test

        Returns
        -------
        None.

        '''
        counter = 2
        while counter <= self.layerCount:
            nodesAtLayer = self.getNodesAtLayer(counter)
            counter+=1
            for node in nodesAtLayer:
                sumInput = 0
                node.sumInput = 0
                input_connections = [connection for connection in self.connList if node.nodeIdentifier == connection.out_Node_ID]
                for connection in input_connections:
                    for nodes in self.nodeList:
                        if connection.in_node_ID == nodes.nodeIdentifier:
                            sumInput+=(nodes.sumOutput*connection.conn_Weight)
                node.sumInput = sumInput
                finalNodeOutput = 1/(1+ math.exp(-(sumInput)))
                node.sumOutput = finalNodeOutput
                        
        
        
        '''
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
         '''       
    def get_output(self, node_number):
        outputs = list()
        for i in range(len(self.nodeList)):
         if (self.nodeList[i].nodeType in ['Output']) and (self.nodeList[i].nodeIdentifier == node_number):
          return self.nodeList[i].sumOutput
                
    
                    
    def calculate_fitness(self, predicted_value, desired_value, previous_fitness_scores=None):
     """
    Calculate fitness based on squared difference between predicted and desired values.

    Parameters:
    - predicted_value (float): The predicted value from the sigmoid activation function (between 0 and 1).
    - desired_value (int): The desired value (either 0 or 1).
    - previous_fitness_scores (list, optional): List of previous fitness scores.

    Returns:
    - float: Fitness score between 0 and 1.
    """
    # Ensure the predicted value is within the valid range (0 to 1)
     predicted_value = max(0.0, min(1.0, float(predicted_value)))

    # Calculate squared difference between predicted and desired values
     squared_difference = (predicted_value - float(desired_value)) ** 2

    # Normalize the fitness score to be between 0 and 1
     fitness_score = 1 - squared_difference

    # Accumulate previous fitness scores
     if previous_fitness_scores is not None:
        fitness_score += previous_fitness_scores

     return fitness_score

    
class Run_Test():
    
    def __init__(self, globalVariableObj=GlobalVariables(2, 1, 0, 0), population_size = int):
        self.variables = globalVariableObj
        self.outputs = list()
        self.fitness = list()
        for i in range(population_size):
            arr_population = Brain(self.variables)  # Create a new instance of Brain in each iteration
            self.outputs.append(arr_population)
        for i in range(len(self.outputs)):
             self.outputs[i].loadInputs((0, 1))
             self.outputs[i].run_network()
             out = self.outputs[i].get_output(4)
             fitness_score = self.outputs[i].calculate_fitness(out, 1)
             self.fitness.append(fitness_score)
        for i in range(len(self.outputs)):
             self.outputs[i].loadInputs((0, 0))
             self.outputs[i].run_network()
             out = self.outputs[i].get_output(4)
             fitness_score = self.outputs[i].calculate_fitness(out, 0, self.fitness[i])
             self.fitness[i] = fitness_score
        for i in range(len(self.outputs)):
             self.outputs[i].loadInputs((1, 1))
             self.outputs[i].run_network()
             out = self.outputs[i].get_output(4)
             fitness_score = self.outputs[i].calculate_fitness(out, 0, self.fitness[i])
             self.fitness[i] = fitness_score
        for i in range(len(self.outputs)):
             self.outputs[i].loadInputs((1, 1))
             self.outputs[i].run_network()
             out = self.outputs[i].get_output(4)
             fitness_score = self.outputs[i].calculate_fitness(out, 1, self.fitness[i])
             self.fitness[i] = fitness_score

    def getFitness(self):
        return self.fitness

def main():
    parameters = GlobalVariables(2, 1, 0, 0)
    brain = Brain(parameters)
    draw = DrawBrain(brain)
    brain.addConnection(False, False, 0)
    brain.addNode()
    draw = DrawBrain(brain)
    brain.addNode()
    draw = DrawBrain(brain)
    x=1
    '''
    test = Run_Test(parameters)
    fitness = test.getFitness()
    '''
    
    
    '''
    test = GlobalVariables(2, 1, 0, 0)
    outputs = list()
    fitness = list()
    for i in range(50):
        arr_population = Brain(test)  # Create a new instance of Brain in each iteration
        outputs.append(arr_population)
    for i in range(len(outputs)):
         outputs[i].loadInputs((0,1))
         outputs[i].run_network()
         out = outputs[i].get_output(4)
         fitness_score = outputs[i].calculate_fitness(out, 1)
         fitness.append(fitness_score)
    for i in range(len(outputs)):
         outputs[i].loadInputs((0,0))
         outputs[i].run_network()
         out = outputs[i].get_output(4)
         fitness_score = outputs[i].calculate_fitness(out, 0, fitness[i])
         fitness[i] = fitness_score
    for i in range(len(outputs)):
         outputs[i].loadInputs((1,1))
         outputs[i].run_network()
         out = outputs[i].get_output(4)
         fitness_score = outputs[i].calculate_fitness(out, 0, fitness[i])
         fitness[i] = fitness_score
    for i in range(len(outputs)):
         outputs[i].loadInputs((1,1))
         outputs[i].run_network()
         out = outputs[i].get_output(4)
         fitness_score = outputs[i].calculate_fitness(out, 1, fitness[i])
         fitness[i] = fitness_score
    return fitness
'''

if __name__=="__main__": 
 outputs = main() 