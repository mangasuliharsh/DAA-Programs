visited=[]
def dfs(graph,n,u):
    visited[u]=1
    for v in range(n):
        if visited[v]==0 and graph[u][v]==1:
            dfs(graph,n,v)
    print(u)
   
    
def main():  
    graph=[ [0,1,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0]]
    n=len(graph[0])
    source=0
    for i in range(n):
        visited.append(0)
    print(".....adjacency matrix........")
    for row in graph:
        print(row)
    print(".........DFS Order............")
    dfs(graph,n,source)
main()
