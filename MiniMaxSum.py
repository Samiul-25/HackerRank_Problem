def miniMaxSum(arr):
    # Sort the array
    arr.sort()
    
    # Calculate the minimum sum excluding the largest element
    min_sum = sum(arr[:-1])
    
    # Calculate the maximum sum excluding the smallest element
    max_sum = sum(arr[1:])
    
    # Print the results
    print(min_sum, max_sum)

# Read input
arr = list(map(int, input().split()))

# Call the miniMaxSum function to calculate and print the results
miniMaxSum(arr)
