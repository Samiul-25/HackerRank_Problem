def staircase(n):
    for i in range(1, n+1):
        # Print spaces
        spaces = " " * (n - i)
        # Print '#' symbols
        hashes = "#" * i
        # Print the staircase row
        print(spaces + hashes)

# Read input
n = int(input())

# Call the staircase function to print the staircase
staircase(n)
