def maximumToys(prices, k):
    # Sort the toy prices in ascending order
    prices.sort()

    # Initialize variables
    toys_bought = 0
    total_cost = 0

    # Iterate through the sorted prices
    for price in prices:
        # If Mark can afford the current toy, buy it
        if total_cost + price <= k:
            total_cost += price
            toys_bought += 1
        else:
            break  # Stop if Mark can't afford the next toy

    return toys_bought

# Sample Input
n, k = map(int, input().split())
prices = list(map(int, input().split()))

# Sample Output
result = maximumToys(prices, k)
print(result)
