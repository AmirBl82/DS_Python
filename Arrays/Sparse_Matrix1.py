import numpy as np

class SparseMatrix:
    def __init__(self, rows, cols, capacity):
        self.rows = rows
        self.cols = cols
        self.capacity = capacity
        # Initialize a 3-column array to store [row, col, value]
        self.elements = np.zeros((capacity, 3), dtype=int)
        self.size = 0  # Tracks the number of non-zero elements

    def add(self, row, col, value):
        if value == 0:
            print("Cannot add zero value to sparse matrix.")
            return
        if row >= self.rows or col >= self.cols or row < 0 or col < 0:
            print("Position out of matrix bounds.")
            return
        if self.size >= self.capacity:
            print("Matrix capacity full. Cannot add more elements.")
            return
        
        # Check if element already exists, update if so
        for i in range(self.size):
            if self.elements[i, 0] == row and self.elements[i, 1] == col:
                self.elements[i, 2] = value
                print(f"Updated element at ({row}, {col}) with value {value}")
                return
        
        # Add new element
        self.elements[self.size] = [row, col, value]
        self.size += 1
        print(f"Added {value} at position ({row}, {col})")

    def delete(self, row, col):
        for i in range(self.size):
            if self.elements[i, 0] == row and self.elements[i, 1] == col:
                # Shift elements up to fill the gap
                self.elements[i:self.size-1] = self.elements[i+1:self.size]
                self.size -= 1
                print(f"Deleted element at position ({row}, {col})")
                return
        print("No element found at this position to delete.")
    
    def get(self, row, col):
        # Retrieve the value at the specified row and column
        for i in range(self.size):
            if self.elements[i, 0] == row and self.elements[i, 1] == col:
                return self.elements[i, 2]
        return 0  # Return 0 if element is not found

    def is_full(self):
        # Check if the matrix has reached its capacity
        return self.size >= self.capacity

    def __str__(self):
        # Optional: visualize the matrix as a dense 2D array
        matrix_repr = np.zeros((self.rows, self.cols), dtype=int)
        for i in range(self.size):
            row, col, value = self.elements[i]
            matrix_repr[row, col] = value
        return "\n".join(" ".join(map(str, row)) for row in matrix_repr)

# Example usage
sparse_matrix = SparseMatrix(3, 3, capacity=2)
sparse_matrix.add(0, 1, 5)
sparse_matrix.add(2, 2, 10)
print("Is matrix full?", sparse_matrix.is_full())  # True if capacity is reached
print(sparse_matrix)
print("Value at (0, 1):", sparse_matrix.get(0, 1))  
print("Value at (1, 1):", sparse_matrix.get(1, 1))  
sparse_matrix.delete(0, 1)
print(sparse_matrix)
