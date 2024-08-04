def binary(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

a = [1,3,2,4,5,6,78,10]
a.sort()
target = int(input("Enter the Number"))
result = binary(a,target)
print(f"{target} found at {result}")
