import numpy as np
import copy

class wezel: #Czy ta klasa jest tu potrzebna?
    def __init__(self, klucz, nazwa = None):
        self.klucz = klucz
        self.nazwa = nazwa
        
    def __eq__(self, other):
        if isinstance(other, wezel):
            return other.klucz == self.klucz
        else:
            return False

    def __hash__(self):
        return hash(self.klucz)

    def __repr__(self):
        return f"{self.klucz}" 
    


class macierzSasiedztwa:
    def __init__(self, parametr_macierzy = 0):
        #self.liczba_wezlow = liczba_wezlow
        self.graf = []
        self.lista_wezlow = []
        self.parametr_macierzy = parametr_macierzy

    def is_empty(self):
        if len(self.graf) == 0:
            return True
        else:
            return False
        
    def insert_vertex(self, wezel):
        if wezel in self.lista_wezlow:
            print("Taki wezel juz istnieje w grafie!")
        else:
            self.lista_wezlow.append(wezel) #self.lista_wezlow[len(self.lista_wezlow)] = wezel #czy to zadziala?
            for wiersz in self.graf:
                wiersz.append(0)
            nowy_wiersz = [self.parametr_macierzy] * (len(self.lista_wezlow))
            self.graf.append(nowy_wiersz)

    def insert_edge(self, wezel1, wezel2, edge = 1):
        index1 = self.get_index(wezel1)
        index2 = self.get_index(wezel2)
        if self.graf[index1][index2] == edge:
            print("Taka krawedz pomiedzy tymi wezlami juz istnieje!")
        else:
            self.graf[index1][index2] = edge
            self.graf[index2][index1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.lista_wezlow:
            indeks_wezla = self.get_index(vertex)
            self.lista_wezlow.pop(indeks_wezla)
            self.graf.pop(indeks_wezla)
            for wiersz in self.graf:
                wiersz.pop(indeks_wezla)
        else:
            print("Takiego wezla nie ma w grafie!")
        
    def delete_edge(self, wezel1, wezel2):
        indeks_wezla1 = self.get_index(wezel1)
        indeks_wezla2 = self.get_index(wezel2)
        if self.graf[indeks_wezla1][indeks_wezla2] == self.parametr_macierzy:
            print("Miedzy tymi wezlami nie ma krawedzi!")
        else:
            self.graf[indeks_wezla1][indeks_wezla2] = self.parametr_macierzy
            self.graf[indeks_wezla2][indeks_wezla1] = self.parametr_macierzy

    def neighbours(self, vertex_id):
        for indeks, wartosc in enumerate(self.graf[vertex_id]):
            if self.graf[vertex_id][indeks] != self.parametr_macierzy:
                yield (indeks, wartosc)

    def vertices(self):
        for i in range(0, len(self.lista_wezlow)):
            yield i

    def get_vertex(self, vertex_id):
        return self.lista_wezlow[vertex_id]
    
    def get_index(self, vertex):
        return self.lista_wezlow.index(vertex)
    
    def __eq__(self, other):
        if not isinstance(other, macierzSasiedztwa):
            return False
        return self.graf == other.graf
    


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")



A = wezel('A')
B = wezel('B')
C  = wezel('C')
D = wezel('D')
E = wezel('E')
F = wezel('F')

graph_G = [(A,B,1), (B,F,1), (B,C,1), (C,D,1), (C,E,1), (D,E,1)]
graph_P = [(A,B,1), (B,C,1), (A,C,1)]

grafG = macierzSasiedztwa()
grafP = macierzSasiedztwa()
for i in graph_G:
    grafG.insert_vertex(i[0])
    grafG.insert_vertex(i[1])
    grafG.insert_edge(i[0], i[1])

for i in graph_P:
    grafP.insert_vertex(i[0])
    grafP.insert_vertex(i[1])
    grafP.insert_edge(i[0], i[1])

# printGraph(grafG)
# printGraph(grafP)

#print(grafG.graf)
liczba_wierszy = 3
liczba_kolumn = 6

M = np.zeros((3, 6), dtype=int)
kolumna = [False for _ in range(0, 6)]
izomorfizmy = []

def ullman(uzywane, aktualny_wiersz, macierz, macierz_sasiedztwa1, macierz_sasiedztwa2, wywolania = 0):
    wywolania += 1

    if aktualny_wiersz == liczba_wierszy:
        if np.array_equal(macierz_sasiedztwa1, macierz @ (np.transpose(macierz @ macierz_sasiedztwa2))):
            izomorfizmy.append(copy.deepcopy(macierz))
        return wywolania
    for i in range(len(uzywane)):
        if uzywane[i] is False:
            uzywane[i] = True
            for j in range(liczba_kolumn):
                if j == i:
                    macierz[aktualny_wiersz][j] = 1
                else:
                    macierz[aktualny_wiersz][j] = 0
            wywolania = ullman(uzywane, aktualny_wiersz + 1, macierz, macierz_sasiedztwa1, macierz_sasiedztwa2, wywolania)
            uzywane[i] = False
    
    return wywolania

print(f"Liczba wywołań to: {ullman(kolumna, 0, M, grafP.graf, grafG.graf)}")
# for i in range(len(izomorfizmy)):
#     print(izomorfizmy[i])
#     print('\n')

# liczba_wierszy = 2
# liczba_kolumn = 3
# testowa = np.zeros((2, 3), dtype=int)
# t_kolumna = [False for _ in range(0, 3)]
# ullman(t_kolumna, 0, testowa)

M0 = np.zeros((3, 6), dtype=int)
stopnieP = np.sum(grafP.graf, axis=1)
stopnieG = np.sum(grafG.graf, axis=1)

for i in range(len(stopnieG)):
    for j in range(len(stopnieP)):
        if stopnieP[j] <= stopnieG[i]:
            M0[j][i] = 1

kolumna = [False for _ in range(0, 6)]
izomorfizmy = []

def ullman2(uzywane, aktualny_wiersz, macierz, macierz_sasiedztwa1, macierz_sasiedztwa2, wywolania = 0):
    wywolania += 1

    if aktualny_wiersz == liczba_wierszy:
        if np.array_equal(macierz_sasiedztwa1, macierz @ (np.transpose(macierz @ macierz_sasiedztwa2))):
            izomorfizmy.append(copy.deepcopy(macierz))
        return wywolania
    macierzKopia = copy.deepcopy(macierz)
    for i in range(len(uzywane)):
        if uzywane[i] is False and macierz[aktualny_wiersz][i] != 0:
            uzywane[i] = True
            for j in range(liczba_kolumn):
                if j == i:
                    macierzKopia[aktualny_wiersz][j] = 1
                else:
                    macierzKopia[aktualny_wiersz][j] = 0
            wywolania = ullman(uzywane, aktualny_wiersz + 1, macierzKopia, macierz_sasiedztwa1, macierz_sasiedztwa2, wywolania)
            uzywane[i] = False
    
    return wywolania

print(f"Liczba wywołań 2.0 to: {ullman2(kolumna, 0, M0, grafP.graf, grafG.graf)}")
# for i in range(len(izomorfizmy)):
#     print(izomorfizmy[i])
#     print('\n')


M0 = np.zeros((3, 6), dtype=int)
stopnieP = np.sum(grafP.graf, axis=1)
stopnieG = np.sum(grafG.graf, axis=1)

for i in range(len(stopnieG)):
    for j in range(len(stopnieP)):
        if stopnieP[j] <= stopnieG[i]:
            M0[j][i] = 1

kolumna = [False for _ in range(0, 6)]
izomorfizmy = []

def ullman3(uzywane, aktualny_wiersz, macierz, macierz_sasiedztwa1, macierz_sasiedztwa2, wywolania = 0):
    wywolania += 1

    if aktualny_wiersz == liczba_wierszy:
        if np.array_equal(macierz_sasiedztwa1, macierz @ (np.transpose(macierz @ macierz_sasiedztwa2))):
            izomorfizmy.append(copy.deepcopy(macierz))
        return wywolania
    
    macierzKopia = copy.deepcopy(macierz)

    while True:
        zmiana = False    
        for i in range(liczba_wierszy):
            for j in range(liczba_kolumn):
                if macierzKopia[i][j] == 1:
                    sasiedziP = []
                    sasiedziG = []

                    for indeks, wartosc in grafP.neighbours(i):
                        sasiedziP.append(indeks)
                    for indeks, wartosc in grafG.neighbours(j):
                        sasiedziG.append(indeks) 

                    for m in sasiedziP:
                        zmienna_pom = False
                        for n in sasiedziG:
                            if macierzKopia[m][n] == 1:
                                zmienna_pom = True
                                break
                        if not zmienna_pom:
                            macierzKopia[i][j] = 0
                            zmiana = True
        if not zmiana:
            break

    for i in range(len(uzywane)):
        if uzywane[i] is False and macierz[aktualny_wiersz][i] != 0:
            uzywane[i] = True
            for j in range(liczba_kolumn):
                if j == i:
                    macierzKopia[aktualny_wiersz][j] = 1
                else:
                    macierzKopia[aktualny_wiersz][j] = 0
            wywolania = ullman(uzywane, aktualny_wiersz + 1, macierzKopia, macierz_sasiedztwa1, macierz_sasiedztwa2, wywolania)
            uzywane[i] = False
    
    return wywolania


print(f"Liczba wywołań 3.0 to: {ullman3(kolumna, 0, M0, grafP.graf, grafG.graf)}")
# for i in range(len(izomorfizmy)):
#     print(izomorfizmy[i])
#     print('\n')
# print(izomorfizmy)