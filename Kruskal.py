p=[]
def parent(x):
    while x != p[x]:
        x = p[x]
    return x

def kruskal(graph,n):
    for i in range(n):
        p.append(i)

    sum=0
    ecount=0
    while ecount < n-1:
        min = 999
        for i in range(n):
            for j in range(n):
                if i != j and graph[i][j]<min:
                    min = graph[i][j]
                    u=i
                    v=j
        if parent(u) != parent(v):
            print("connect",u,"------>",v,"=",graph[u][v])
            sum+=graph[u][v]
            ecount+=1
            p[v]=u
        graph[u][v] = graph[v][u] = 999
    print("MST Cost = ",sum)
def main():
    graph=[ [0,30,40,999,999,999],
        [30,0,50,10,999,999],
        [40,50,0,999,20,999],
        [999,10,999,0,60,80],
        [999,999,20,60,0,70],
        [999,999,999,80,70,0]]
    n=len(graph[0])
    print(".....weight matrix........")
    for row in graph:
        print(row)
    print("..........MST Edge.........")
    kruskal(graph,n)
main() 
