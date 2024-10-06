graph={'A':set(['B','C']),
       'B': set(['A','D','E']),
       'C': set(['A','F',]),
       'D': set(['B']),
       'E': set(['B','F']),
       'F': set(['C','E'])
       }
def BFS(start):
    queue=[start] 
    levels={}
    levels[start]=0
    visited=set(start) #v=
    while queue:
        node=queue.pop(0)
        ns=graph[node] #ns=neighbours
        for ng in ns:
            if ng not in visited: #ng=neighbor
                queue.append(ng)
                visited.add(ng)
                levels[ng]=levels[node]+1
    print(levels)
    return visited
print(str(BFS('A')))
