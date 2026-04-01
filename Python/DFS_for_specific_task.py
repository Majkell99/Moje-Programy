wyniki = {}
cost = 0
def dfs(graph: zad.listaSasiedztwa, start : zad.wezel, visited : set = None, kolejnosc = None): #nie uzywaj pustej listy jako argumentu funkcji w py
    global cost
    if visited is None:                                                                   
        visited = set()

    if kolejnosc is None:
        kolejnosc = []

    if start not in visited:
        visited.add(start)
        kolejnosc.append(start)
        
        for wezly in graph.graf[start]: #iteruje po samych kluczach
            if wezly not in visited:
                actual_cost = graph.graf[start][wezly]
                cost += actual_cost
                dfs(graph, wezly, visited, kolejnosc) #kolejnosc.extend(dfs(graph, wezly, visited, kolejnosc))
                cost -= actual_cost #czemu tutaj musze odejmowac cost a nie poza petla? 

    if len(visited) == 11:
        wyniki[tuple(kolejnosc)] = cost #nie moge użyć listy w slowniku bo lista jest mutowalna 
    kolejnosc.pop()         
    visited.remove(start) #usuwamy dany wezel jesli wszyscy sasiedzi byli odwiedzeni - trasa sie skonczyla

    return

dfs(zad.graf, zad.wezel(0))

print(wyniki)
