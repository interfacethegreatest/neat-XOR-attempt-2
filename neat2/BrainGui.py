from globalVariables import *

import tkinter as tk

class DrawBrain:
    
    def __init__(self):
        num_layers = 3
        num_nodes = (1,3,2)
        self.create_tkinter_window()
        canvas, rectangle_indexes = self.create_outlined_rectangle(1400, 900, num_layers)
        self.draw_nodes(canvas, rectangle_indexes, num_nodes)
        self.root.mainloop()
    
 
    def draw_nodes(self, canvas, rectangle_indexes, num_nodes_list):
     for rect_index, num_nodes in zip(rectangle_indexes, num_nodes_list):
        # Get the coordinates of the rectangle
        x0, y0, x1, y1 = canvas.coords(rect_index)

        # Calculate the height of each node
        node_height = (y1 - y0) / num_nodes

        # Draw nodes vertically within each rectangle
        for i in range(num_nodes):
            node_x0 = x0
            node_y0 = y0 + i * node_height
            node_x1 = x1
            node_y1 = node_y0 + node_height
            canvas.create_rectangle(node_x0, node_y0, node_x1, node_y1, fill="black") 

            # Calculate the center of the node
            center_x = (node_x0 + node_x1) / 2
            center_y = (node_y0 + node_y1) / 2

            # Draw a white circle at the center
            radius = min((node_x1 - node_x0) / 14, (node_y1 - node_y0) / 14)
            canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="red")
            
        canvas.pack()





    def create_tkinter_window(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("My Tkinter Window")

        # Add widgets and functionality here if needed
        self.root.geometry("1400x900")
        self.root.configure(bg="black")

    def create_outlined_rectangle(self, width, height, num_subrectangles):
        # Set the default border percentage
        border_percentage = 10

        # Calculate the dimensions of the inner rectangle
        inner_width = width * (1 - border_percentage / 100)
        inner_height = height * (1 - border_percentage / 100)

        # Calculate the border size
        border_width = (width - inner_width) / 2
        border_height = (height - inner_height) / 2

        # Calculate the dimensions of each smaller rectangle
        subrect_width = inner_width / num_subrectangles
        subrect_height = inner_height

        # Create a Canvas widget
        canvas = tk.Canvas(self.root, width=width, height=height, bg="black")
        canvas.pack()

        # Draw the outer rectangle (border)
        canvas.create_rectangle(0, 0, width, height, outline="black", width=border_width, fill="")

        # Draw the inner rectangle
        canvas.create_rectangle(border_width, border_height, width - border_width, height - border_height, fill="black")

        # Draw the smaller rectangles and store their indexes
        rectangle_indexes = []
        for i in range(num_subrectangles):
            x0 = border_width + i * subrect_width
            y0 = border_height
            x1 = x0 + subrect_width
            y1 = height - border_height
            rect_index = canvas.create_rectangle(x0, y0, x1, y1, fill="black")
            rectangle_indexes.append(rect_index)

        # Return the canvas and the list of rectangle indexes
        return canvas, rectangle_indexes

if __name__ == "__main__":
    window = DrawBrain()



    

