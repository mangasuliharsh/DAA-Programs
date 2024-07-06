import numpy as np

def show(w,p,n,m,v):
    print("Dynamic Programming Table")
    print(v)
    profit = v[n][m]
    print("Items included in Optimal Solution")
    i=n
    j=m
    while i>0 and profit>0:
        if v[i][j] != v[i-1][j]:
            print("Item Weight=",w[i],"Item value=",p[i])
            profit -= p[i]
            j -= w[i]
        i-=1

def knapsack(w,p,n,m):
    v = np.zeros((n+1,m+1),dtype=int)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if w[i] > j:
                v[i][j] = v[i-1][j]
            else:
                v[i][j] = max(v[i-1][j],p[i]+v[i-1][j-w[i]])
    show(w,p,n,m,v)
    return v[n][m]

w = [0, 2, 1, 3, 2]
p = [0, 12, 10, 20, 15]
n = 4
m = 5

res = knapsack(w, p, n, m)
print("Optimal solution =", res)
