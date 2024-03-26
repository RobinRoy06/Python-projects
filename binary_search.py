def binary_search(arr, target, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

arr = [1, 2, 3, 4, 5]
target = 1
high = len(arr) - 1
low = 0

result = binary_search(arr, target, low, high)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the array.")
