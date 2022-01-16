"""Module for describing one cell of the field"""

class Cell:

    def __init__(self, y_in_field = 0, x_in_field = 0, cell_status = 0, cell_color = (0, 255, 127), thickness = 12):
        self.y_in_field = y_in_field
        self.x_in_field = x_in_field
        self.cell_status = cell_status
        self.cell_color = cell_color
        self.thickness = thickness

    def __str__(self):
        return  f"""
        Cell color: {self.cell_color}
        Cell thickness: {self.thickness}
        """

    def get_info_about_cell(self):
        """Print the information about the cell"""
        print(str(self))

    def in_field(self, height = None, width = None):
        if(height is None) or (width is None):
            print("Wrong attributes")
            return None
        if(self.y_in_field <= height) and (self.x_in_field <= width):
            return True
        return False
    
    def status_in_next_generation(self, number_of_neighbours = 0):
        """The method will return 1 if the cell is alive, otherwise 0"""
        if(self.cell_status):
            if(number_of_neighbours >= 2) and (number_of_neighbours <= 3):
                return 1
        else:
            if number_of_neighbours == 3:
                return 1
        return 0
        
        
