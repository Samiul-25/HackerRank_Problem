def birthdayCakeCandles(candles):
    # Find the maximum height of the candles
    max_height = max(candles)
    
    # Count the number of candles with the maximum height
    count_tallest_candles = candles.count(max_height)
    
    return count_tallest_candles

# Read input
n = int(input())
candles = list(map(int, input().split()))

# Call the birthdayCakeCandles function to get the result
result = birthdayCakeCandles(candles)

# Print the result
print(result)
