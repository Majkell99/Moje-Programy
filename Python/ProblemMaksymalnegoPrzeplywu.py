class wezel:
    def __init__(self, klucz, kolor = None):
        self.klucz = klucz
        self.kolor = kolor
        
    def zwroc_kolor(self):
        return self.kolor
    
    # def nowy_kolor(self, nowy_kolor):
    #     self.kolor = nowy_kolor          #Czy to ma byc?

    def __eq__(self, other):
        if isinstance(other, wezel):
            return other.klucz == self.klucz
        else:
            return False

    def __hash__(self):
        return hash(self.klucz) #używanie węzła (klucza) jako indeks słownika 

    def __repr__(self):
        return f"{self.klucz}"



class krawedz:
    def __init__(self, przepustowosc: int, info: bool):
        if info:
            self.info = info
            self.przepustowosc = przepustowosc #chyba to jest pojemnosc
            self.pojemnosc_resztowa = przepustowosc
            self.przeplyw = 0
        else:
            self.info = info
            self.pojemnosc_resztowa = 0
            self.przeplyw = 0
            self.przepustowosc = przepustowosc

    def __repr__(self):
        return f'{self.przepustowosc} {self.przeplyw} {self.pojemnosc_resztowa} {self.info}'



class listaSasiedztwa:
    def __init__(self):
        self.graf = {}

    def is_empty(self):
        if len(self.graf) == 0:
            return True
        else:
            return False
        
    def insert_vertex(self, wezel):
        if wezel in self.graf:
            print("Ten wezel jest juz w grafie")
        else:
            self.graf[wezel] = {}

    def insert_edge(self, wezel1, wezel2, edge):
        if wezel1 in self.graf:
            if wezel2 in self.graf[wezel1]:
                if self.graf[wezel1][wezel2] == edge:
                    print("Taka krawedź, pomiędzy takimi węzłami już istnieje")
                else:
                    self.graf[wezel1][wezel2] = krawedz(edge, True)
                    self.graf[wezel2][wezel1] = krawedz(edge, False)
            else:
                self.graf[wezel1][wezel2] = krawedz(edge, True)
                self.graf[wezel2][wezel1] = krawedz(edge, False)
        else:
            print("Wezla 1 nie ma w grafie")

    def delete_vertex(self, wezel):
        if wezel not in self.graf:
            print("Takiego węzła nie ma w grafie")
        else:
            del self.graf[wezel]
            for i in self.graf:
                if wezel in self.graf[i]:
                    del self.graf[i][wezel] 

    def delete_edge(self, wezel1, wezel2):
        if wezel2 not in self.graf[wezel1]:
            print("Miedzy tymi węzłami nie ma krawędzi")
        else:
            del self.graf[wezel1][wezel2]
            del self.graf[wezel2][wezel1] #chyba bedzie to trzeba zmienic przy grafie skierowanym

    def neighbours(self, vertex_id):
        if vertex_id in self.graf:
            podslownik = self.graf[vertex_id]
            for klucz, wartosc in podslownik.items():
                yield (klucz, wartosc)
        else:
            print("Takiego węzła nie ma w grafie!")

    def vertices(self):
        if self.is_empty():
            print("Graf jest pusty")
        else:
            lista_wezlow = []
            for klucz, wartosc in self.graf.items():
                lista_wezlow.append(klucz)
            return lista_wezlow
        
    def get_vertex(self, vertex_id):
        return vertex_id

    def get_edge(self, wezel1, wezel2):
        return self.graf[wezel1][wezel2]



def BFS(graf : listaSasiedztwa, start : wezel, stop : wezel) -> dict:
    odwiedzone = set()
    kolejka = []
    parent = {}

    kolejka.append(start)
    odwiedzone.add(start)

    while kolejka and stop not in odwiedzone:
        i = kolejka.pop(0) #i = kolejka[-1]
        for klucz, wartosc in graf.neighbours(i):
            if klucz not in odwiedzone and wartosc.pojemnosc_resztowa > 0:
                kolejka.append(klucz)
                odwiedzone.add(klucz)
                parent[klucz] = i

    return parent #chyba jest git



def analiza_sciezki(graf : listaSasiedztwa, start : wezel, stop : wezel, parent : dict):
    if stop in parent:
        i = stop
        najmniejsza_poj_reszt = None
        while i != start:
            kraw = graf.get_edge(parent[i], i)
            # if kraw == None:
            #     print("Pomiedzy danym wierzcholkiem a jego rodzicem nie ma krawedzi - błąd grafu!")
            #     return 0  
            if najmniejsza_poj_reszt == None or najmniejsza_poj_reszt > kraw.pojemnosc_resztowa:
                najmniejsza_poj_reszt = kraw.pojemnosc_resztowa
            i = parent[i]
    else:
        najmniejsza_poj_reszt = 0

    return najmniejsza_poj_reszt



def sciezka(graf : listaSasiedztwa, start : wezel, stop : wezel, parent : dict, najm_poj : int):
    i = stop
    while i != start:
        kraw1 = graf.get_edge(parent[i], i) 
        kraw2 = graf.get_edge(i, parent[i])
        kraw1.pojemnosc_resztowa -= najm_poj
        # kraw1.przeplyw += najm_poj
        
        # kraw2.przeplyw -+ najm_poj
        kraw2.pojemnosc_resztowa += najm_poj #nie rozumiem do konca tej funkcji w kontekście tego algorytmu i 
                                             #tego algorytmu troche tez nie rozumiem
        if kraw1.info:
            kraw1.przeplyw += najm_poj 
        else:
            kraw2.przeplyw -= najm_poj # tego nie rozumiem
        
        i = parent[i] 



def AlgorytmFordaFulkersona(graf : listaSasiedztwa, start : wezel, stop : wezel):
    maksymalny_przeplyw = 0

    while True:
        parent = BFS(graf, start, stop) 
        if stop in parent:
            najmniejsza_poj_reszt = analiza_sciezki(graf, start, stop, parent)
            sciezka(graf, start, stop, parent, najmniejsza_poj_reszt)
            maksymalny_przeplyw += najmniejsza_poj_reszt
        else:
            break

    return maksymalny_przeplyw



def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")



def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf0 = listaSasiedztwa()
    wezly_krawedzie = []
    s = wezel('s')
    u = wezel('u')
    t = wezel('t')
    v = wezel('v')

    wezly_krawedzie = [(s,u,2), (u,t,1), (u,v,3), (s,v,1), (v,t,2)]

    for i in wezly_krawedzie:
        graf0.insert_vertex(i[0])
        graf0.insert_vertex(i[1])
        graf0.insert_edge(i[0], i[1], i[2])

    maksprzeplyw0 = AlgorytmFordaFulkersona(graf0, s, t)
    przeplyw_wyplywajacy0 = 0
    for i in wezly_krawedzie:
        if i[0] == u:
            przeplyw_wyplywajacy0 += graf0.get_edge(i[0], i[1]).przeplyw
    


    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf1 = listaSasiedztwa()
    wezly_krawedzie1 = []
    s = wezel('s')
    a = wezel('a')
    c = wezel('c')
    b = wezel('b')
    d = wezel('d')
    t = wezel('t')

    wezly_krawedzie1 = [(s, a, 16), (s, c, 13), (a, c, 10), (a, b, 12), (b, c, 9), (b, t, 20), (c, d, 14), (d, b, 7), (d, t, 4) ]

    for i in wezly_krawedzie1:
        graf1.insert_vertex(i[0])
        graf1.insert_vertex(i[1])
        graf1.insert_edge(i[0], i[1], i[2])
    
    maksprzeplyw1 = AlgorytmFordaFulkersona(graf1, s, t)
    przeplyw_wyplywajacy1 = 0
    for i in wezly_krawedzie1:
        if i[0] == a:
            przeplyw_wyplywajacy1 += graf1.get_edge(i[0], i[1]).przeplyw

    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf2 = listaSasiedztwa()
    wezly_krawedzie2 = []
    s = wezel('s')
    a = wezel('a')
    c = wezel('c')
    b = wezel('b')
    d = wezel('d')
    t = wezel('t')
    e = wezel('e')

    wezly_krawedzie2 = [ (s, a, 3), (s, c, 3), (a, b, 4), (b, s, 3), (b, c, 1), (b, d, 2), (c, e, 6), (c, d, 2), (d, t, 1), (e, t, 9)]

    for i in wezly_krawedzie2:
        graf2.insert_vertex(i[0])
        graf2.insert_vertex(i[1])
        graf2.insert_edge(i[0], i[1], i[2])
    
    maksprzeplyw2 = AlgorytmFordaFulkersona(graf2, s, t)
    przeplyw_wyplywajacy2 = 0
    for i in wezly_krawedzie2:
        if i[0] == a:
            przeplyw_wyplywajacy2 += graf2.get_edge(i[0], i[1]).przeplyw


    graf_3 = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3),  ('f', 't', 3), ('d', 'e', 2), ('e','f',2)]
    graf3 = listaSasiedztwa()
    wezly_krawedzie3 = []
    s = wezel('s')
    a = wezel('a')
    c = wezel('c')
    b = wezel('b')
    d = wezel('d')
    t = wezel('t')
    e = wezel('e')
    f = wezel('f')

    wezly_krawedzie3 = [(s,a, 3), (s, d, 2), (a, b, 4), (b, c, 5), (c, t, 6), (a, f, 3),  (f, t, 3), (d, e, 2), (e,f,2)]

    for i in wezly_krawedzie3:
        graf3.insert_vertex(i[0])
        graf3.insert_vertex(i[1])
        graf3.insert_edge(i[0], i[1], i[2])
    
    maksprzeplyw3 = AlgorytmFordaFulkersona(graf3, s, t)
    przeplyw_wyplywajacy3 = 0
    for i in wezly_krawedzie3:
        if i[0] == a:
            przeplyw_wyplywajacy3 += graf3.get_edge(i[0], i[1]).przeplyw

    print('\n')
    print(f"Maksymalny przeplyw 0: {maksprzeplyw0}")
    printGraph(graf0)
    print(f"Rzeczywisty przepływ wypływający z węzła u: {przeplyw_wyplywajacy0}")

    print('\n')
    print(f"Maksymalny przeplyw 1: {maksprzeplyw1}")
    printGraph(graf1)
    print(f"Rzeczywisty przepływ wypływający z węzła a: {przeplyw_wyplywajacy1}")

    print('\n')
    print(f"Maksymalny przeplyw 2: {maksprzeplyw2}")
    printGraph(graf2)
    print(f"Rzeczywisty przepływ wypływający z węzła a: {przeplyw_wyplywajacy2}")

    print('\n')
    print(f"Maksymalny przeplyw 3: {maksprzeplyw3}")
    printGraph(graf3)
    print(f"Rzeczywisty przepływ wypływający z węzła a: {przeplyw_wyplywajacy3}")


main()
    




