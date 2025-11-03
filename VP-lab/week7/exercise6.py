def pascal(num_rows):
    triangle = []

    for row_num in range(num_rows):
        row = [1] * (row_num + 1)
        # Each element (except the first and last in the row) is the sum of the two elements above it
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        
        # Append the completed row to the triangle
        triangle.append(row)
    
    return triangle

# Function to print the triangle nicely
def print_triangle(triangle):
    for row in triangle:
        print(" " * (len(triangle) - len(row)), " ".join(map(str, row)))

# Example usage:
row = int(input())
triangle = pascal(row)
print_triangle(triangle)

