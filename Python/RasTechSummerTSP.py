import random
import matplotlib.pyplot as plt

import RasTechSummerZad as zad

def TSP(graph : zad.listaSasiedztwa, start : zad.wezel):
    unvisited = set(graph.vertices)
    unvisited.remove(start)
    tour = [start]
    current_vertex = start
    min_cost = 9999
    actual_cost = 0


    while unvisited:
        current_neighbours = list(graph.neighbours(current_vertex))
        for i in range(len(current_neighbours)):
            next_vertex = current_neighbours[i][0]
            acutal_cost += current_neighbours[i][1]

            if acutal_cost > min_cost:
                continue
            else:
                min_cost = actual_cost #te dwa chyba bedzie trzeba jakos resetowac potem

            tour.append(next_vertex)

    kolejnosc = []
    visited = set()

    if start not in visited:
        visited.add(start)
        kolejnosc.append(start)
        
    for wezly in graph.graf[start]: #iteruje po samych kluczach
        
        kolejnosc.extend(dfs(graph, wezly, visited))

    return kolejnosc


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
