import time 
from random import randint
import matplotlib.pyplot as plt

def selection(a,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if a[j] < a[min_index]:
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]

def main():
    x=[]
    y=[]
    for n in range(1000,10000,1000):
        a = []
        x.append(n)
        for i in range(n):
            a.append(randint(1,n))
        print('------------------------------\n')
        print (a)
        start=time.time()
        selection(a,n)
        end=time.time()
        print('------------------------------\n')
        print(a)
        gaptime=end-start
        y.append(gaptime)
    plt.plot(x,y,c='red')
    plt.xlabel("N-size")
    plt.ylabel("Time(ms)")
    plt.show()
main()
