from globalVariables import *

import tkinter as tk

class DrawBrain:
    
    def __init__(self, brain):
        self.brain = brain
        self.layers = self.brain.layerCount
        self.create_tkinter_window()
        nodeLocations = self.draw_nodes(self.draw_border_rectangle(1200, 900))
        self.draw_connections(nodeLocations)
        self.print_objects_at_position(self.brain.connList, 1200, 20)
        self.root.mainloop()
        
        
        
    def print_objects_at_position(self, object_list, x, y):
     for obj in object_list:
        # Get the string representation of the object using its __str__ function
        obj_str = obj.__str__()

        # Print the string at the specified x, y position on the canvas
        self.canvas.create_text(x, y, text=obj_str, fill="white")

        # Increment y to move to the next line (adjust as needed)
        y += 20  # You can adjust the value based on your preferred spacing
    
    def create_tkinter_window(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("My Tkinter Window")

        # Add widgets and functionality here if needed
        self.root.geometry("1400x900")
        self.root.configure(bg="black")
        self.canvas = tk.Canvas(self.root, width=1400, height=900, bg="black")
        self.canvas.pack()   
        
    
    

    def draw_connections(self, divided_rectangle_coordinates):
     connection_list = self.brain.connList

     for connection in connection_list:
        inloc = connection.in_node_ID
        outloc = connection.out_Node_ID
        in_coordinate, out_coordinate = None, None

        # Find the coordinates for inloc and outloc
        for node, coordinate in divided_rectangle_coordinates:
            if node.nodeIdentifier == inloc:
                in_coordinate = coordinate
            elif node.nodeIdentifier == outloc:
                out_coordinate = coordinate

        # Draw lines between the centers of inloc and outloc
        if in_coordinate is not None and out_coordinate is not None:
            in_center_x, in_center_y = (in_coordinate[0] + in_coordinate[2]) / 2, (in_coordinate[1] + in_coordinate[3]) / 2
            out_center_x, out_center_y = (out_coordinate[0] + out_coordinate[2]) / 2, (out_coordinate[1] + out_coordinate[3]) / 2
        
        
        if connection.ennabled and connection.is_Recurrent:
         # Draw a line between the centers
         self.canvas.create_line(in_center_x, in_center_y, out_center_x, out_center_y, fill="Blue", width=0.7, dash=(2, 2))
        elif connection.ennabled:
         self.canvas.create_line(in_center_x, in_center_y, out_center_x, out_center_y, fill="Green")
        else:
         self.canvas.create_line(in_center_x, in_center_y, out_center_x, out_center_y, fill="Red")
        
        
        
    
    def draw_nodes(self, divided_rectangle_coordinates):
     node_dict = {}  # Dictionary to store nodes with identifiers as keys

     for node, rect_coords in divided_rectangle_coordinates:
        # Extract rectangle coordinates
        rect_x1, rect_y1, rect_x2, rect_y2 = rect_coords

        # Calculate the center of the rectangle
        center_x = (rect_x1 + rect_x2) / 2
        center_y = (rect_y1 + rect_y2) / 2

        # Draw a small circle representing the node
        radius = 5  # You can adjust the radius as needed
        self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="blue")

        # Print the node's __str__ function below the circle
        text_x = center_x
        text_y = center_y + radius + 5  # Add some space below the circle for the text
        self.canvas.create_text(text_x, text_y, text=node.__str__(), fill="white")
        
        
     return divided_rectangle_coordinates



        
        
    
    
    
    def draw_border_rectangle(self, width, height, border_percentage=0.1):
     rectangleList = list()
     layer = 1
     while layer <= self.layers:
        nodes = self.brain.getNodesAtLayer(layer)
        rectangleList.append(len(nodes))
        layer += 1

     border_x = width * border_percentage
     border_y = height * border_percentage

     x1 = border_x
     y1 = border_y
     x2 = width - border_x
     y2 = height - border_y

     total_rectangles = len(rectangleList)
     rectangle_width = (x2 - x1) / total_rectangles

     rectangle_coordinates = []  # List to store the coordinates of each sub-rectangle

     for i in range(total_rectangles):
        rect_x1 = x1 + i * rectangle_width
        rect_x2 = rect_x1 + rectangle_width
        rect_y1 = y1
        rect_y2 = y2

        self.canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline="black")
        rectangle_coordinates.append((rect_x1, rect_y1, rect_x2, rect_y2))

     # Divide each rectangle into equal horizontal divisions specified by rectangleList
     divided_rectangle_coordinates = []
     for i, (rect_x1, rect_y1, rect_x2, rect_y2) in enumerate(rectangle_coordinates):
        total_divisions = rectangleList[i]

        sub_rectangle_height = (rect_y2 - rect_y1) / total_divisions
        sub_rectangle_width = rect_x2 - rect_x1

        for j in range(total_divisions):
            sub_rect_x1 = rect_x1
            sub_rect_x2 = rect_x2
            sub_rect_y1 = rect_y1 + j * sub_rectangle_height
            sub_rect_y2 = sub_rect_y1 + sub_rectangle_height

            self.canvas.create_rectangle(sub_rect_x1, sub_rect_y1, sub_rect_x2, sub_rect_y2, outline="black")
            divided_rectangle_coordinates.append((sub_rect_x1, sub_rect_y1, sub_rect_x2, sub_rect_y2))
     
     nodeList = self.brain.getNodesInOrder()
     divided_rectangle_coordinates = list(zip(nodeList, divided_rectangle_coordinates))
     return divided_rectangle_coordinates


if __name__ == "__main__":
    inputNodes = 2
    hiddenNodes = 0
    outputNodes = 1
    percConnections = 0
    inputs = (0,1)
    output = 4
    gv = GlobalVariables(inputNodes, outputNodes, hiddenNodes, percConnections)
    brain2 = Brain(gv)
    brain2.loadInputs(inputs)
    brain2.addConnection(False, False,0)
    brain2.addNode()
    brain2.addNode()
    TEST = DrawBrain(brain2)
    brain2.run_network()
    window = DrawBrain(brain2)
