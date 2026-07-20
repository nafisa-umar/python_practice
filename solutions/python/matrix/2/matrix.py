class Matrix:
    def __init__(self, matrix_string): # first split matrix string into new lines, then split by spaces
        self.matrix_string =  [[int(i) for i in row.split()] 
                               for row in matrix_string.split("\n")]                  

    def row(self, index):
        return self.matrix_string[index-1]

    def column(self, index):    # single out rows, then take index-1 for each row
        return [row[index - 1] for row in self.matrix_string]
