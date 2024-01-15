def diagonalDifference(arr):
    n = len(arr)
    
    # Initialize variables to store the sum of each diagonal
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    # Calculate the sum of the primary diagonal
    for i in range(n):
        primary_diagonal_sum += arr[i][i]
    
    # Calculate the sum of the secondary diagonal
    for i in range(n):
        secondary_diagonal_sum += arr[i][n - 1 - i]
    
    # Calculate the absolute difference between the two diagonals
    absolute_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
    
    return absolute_difference

# Example usage:
matrix_size = int(input())  # Assuming you read the matrix size from input
matrix = []

# Reading the matrix from input
for _ in range(matrix_size):
    row = list(map(int, input().split()))
    matrix.append(row)

result = diagonalDifference(matrix)
print(result)
