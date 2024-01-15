def countSwaps(a):
    n = len(a)
    swaps = 0

    for i in range(n):
        for j in range(n - 1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

# Input from STDIN
n = int(input())
arr = list(map(int, input().split()))

# Call the function with the input array
countSwaps(arr)
