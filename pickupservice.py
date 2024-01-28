
def PickUp(N, start, connections): 
    graph = defaultdict(list) 
    taxes = defaultdict(int) 

    for i in range(N - 1): 
        city1, city2, goods, tax = connections[i] 
        graph[city1].append((-1 * goods, tax, city2)) 
        taxes[city2] = tax 

    route = [] 



    def dfs(city): 
        route.append(city) 
        for n in sorted(graph[city]): 
            dfs(n[2]) 
            route.append(city) 
    dfs(start) 



    total_tax = 0 
    for c in route[1:]: 
        total_tax += taxes[c] 

    return route, total_tax 



N = int(input()) 
cons = [] 


for _ in range(N-1): 
    l = input() 
    ls = l.split() 
    cons.append((ls[0], ls[1], int(ls[2]), int(ls[3]))) 


ans, t = PickUp(N, cons[0][0], cons) 

print("-".join(ans)) 
print(t, end="")

