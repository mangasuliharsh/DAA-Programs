import time
import matplotlib.pyplot as plt
from random import randint

def arraysum(a):
    sum = 0
    for num in a:
        sum += num
    return sum

def main():
    x = []
    y = []
    for n in range(100,10000,100):
        x.append(n)
        a=[]
        for i in range(n):
            a.append(randint(1,n))
        start = time.time()
        result = arraysum(a)
        print(result)
        end = time.time()
        gap = end - start
        y.append(gap)
    plt.plot(x,y)
    plt.show()

main()
