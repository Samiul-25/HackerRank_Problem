def simpleArraySum(n, ar):
    # Sum the elements of the array using the built-in sum() function
    return sum(ar)

# Read input values
n = int(input())
ar = list(map(int, input().split()))

# Call the function and print the result
result = simpleArraySum(n, ar)
print(result)
