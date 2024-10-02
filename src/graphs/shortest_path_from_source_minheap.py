import heapq
print("hello")

input = [['C', 'A', 2],
         ['C', 'D', 5],
         ['C', 'B', 9],
         ['A', 'F', 4],
         ['F', 'E', 6],
         ['A', 'B', 5],
         ['B', 'E', 3],
         ['D', 'B', 8],
        ]

def findShortestpathFromSource(input, source):
    # create_adj_list = lambda input : {u : [[v,w] for x, v, w in input if x == u ] for u, _, _ in input}
    # adj_list = create_adj_list(input)
    adj_list = { c: [] for c, _, _ in input}
    print(adj_list)
    for x, y, w in input:
        if (x not in adj_list):
            adj_list[x] = []
        adj_list[x].append((y, w))
        if (y not in adj_list):
            adj_list[y] = []
        adj_list[y].append((x, w))
    print(adj_list)
    
    arr = [(0, source)]
    heapq.heapify(arr)
    
    visited = set()
    ans = { }
    
    while len(arr) > 0:
        w, v = heapq.heappop(arr) # weight, value
        visited.add(v)
        
        if (v not in ans):
            ans[v] = float("infinity")
            
        if (ans[v] > w):
            ans[v] = w   
        
        for n, w in adj_list[v]:
            if n not in visited:
                weight = w 
                if (v in ans):
                    weight = w + ans[v]
                heapq.heappush(arr, (weight, n))
    return ans

print("ans", findShortestpathFromSource(input, 'C'))
