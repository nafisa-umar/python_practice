class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rows = self.matrix_string.split("\n")
        rows = [row.split() for row in rows]
        rows = [[int(item) for item in row] for row in rows]
        return rows[index - 1]
        
        
        
        

    def column(self, index):
        rows = self.matrix_string.split("\n")
        rows = [row.split() for row in rows]
        rows = [[int(item) for item in row] for row in rows]
        columns = []
        for i in range(len(rows[0])):
            columns.append([int(row[i]) for row in rows])

        return columns[index - 1]

            

        
