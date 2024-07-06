def divide(array, low, high):
    if low < high:
        mid = (low + high) // 2
        divide(array, low, mid)
        divide(array, mid + 1, high)
        merge(array, low, mid, high)
    return array

def merge(array, low, mid, high):
    i = low
    j = mid + 1
    k = low
    temp = [0] * len(array)  # Create a temporary array for merging

    while i <= mid and j <= high:
        if array[i] <= array[j]:
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = array[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = array[j]
        j += 1
        k += 1

    for idx in range(low, high + 1):
        array[idx] = temp[idx]

def main():
    x = []
    y = []
    for n in range(1000, 10000, 1000):
        x.append(n)
        a = []
        for i in range(n):
            a.append(randint(1, n))

        start = time.time()
        divide(a, 0, len(a) - 1)
        end = time.time()
        elapsed = end - start
        y.append(elapsed)
        print("\n-----Sorted list----\n")
        print(a)
    plt.plot(x,y,c='red')
    plt.xlabel("N-size")
    plt.ylabel("Time(ms)")
    plt.show()
main()
