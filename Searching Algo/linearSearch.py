def linear(arr,target):
    for index,element in enumerate(arr):
        if element == target:
            return index
    return -1

a = [1,3,2,4,5,6,78,10]
target = int(input("Enter the Number"))
result = linear(a,target)
print(f"{target} found at {result}")
