def plusMinus(arr):
    n = len(arr)
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)

    # Calculate and print the proportions
    print("{:.6f}".format(positive_count / n))
    print("{:.6f}".format(negative_count / n))
    print("{:.6f}".format(zero_count / n))

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the plusMinus function to calculate and print proportions
plusMinus(arr)
