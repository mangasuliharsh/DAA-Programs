def partition(array,low,high):
    i=low-1
    pivot=high
    for j in range(low,high):
        if array[j]<=array[pivot]:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return i+1

def quick(array,low,high):
    if low<high:
        pi = partition(array,low,high)
        quick(array,low,pi-1)
        quick(array,pi+1,high)
    return array

def main():
    x = []
    y = []
    for n in range(1000, 10000, 1000):
        x.append(n)
        a = []
        for i in range(n):
            a.append(randint(1, n))

        start = time.time()
        quick(a, 0, len(a) - 1)
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
