import time 
from random import randint
import matplotlib.pyplot as plt

def bubble(a,n):
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

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
        bubble(a,n)
        end=time.time()
        print(a)
        gaptime=end-start
        y.append(gaptime)
    plt.plot(x,y,c='red')
    plt.xlabel("N-size")
    plt.ylabel("Time(ms)")
    plt.show()
main()
