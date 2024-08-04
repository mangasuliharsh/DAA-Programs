import time
import matplotlib.pyplot as plt
from random import randint

def heapify(a,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and a[i] < a[l]:
        largest = l
    if r < n and a[largest] < a[r]:
        largest = r
    
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        heapify(a,n,largest)

def heapsort(a):
    n = len(a)
    
    for i in range(n //2-1,-1,-1):
        heapify(a,n,i)
    
    for i in range(n-1,0,-1):
        a[i],a[0] = a[0],a[i]
        heapify(a,i,0)

def main():
    x = []
    y = []
    for n in range(1000, 100000, 1000):
        x.append(n)
        a=[]
        for i in range(n):
            a.append(randint(1,n))
        start = time.time()
        heapsort(a)
        end = time.time()
        total = end - start
        y.append(total)
    plt.plot(x, y)
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Heap Sort')
    plt.grid(True)
    plt.show()

main()
