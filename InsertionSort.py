import time
from random import randint
import matplotlib.pyplot as plt

def insertion(a,n):
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
        
def main():
    x = []
    y = []
    for n in range(10, 101,10 ):
        x.append(n) 
        a = []
        for i in range(n):
            a.append(randint(1, n))
        start = time.time()
        insertion(a,n)
        end = time.time()
        elapsed = end - start
        y.append(elapsed)
        print("\n-----Sorted list----\n")
        print(a)
    plt.plot(x, y, label='Insertion Sort')
    plt.xlabel("Input Size")
    plt.ylabel("Time(ms)")
    plt.legend(loc='upper right')
    plt.show()
main()
