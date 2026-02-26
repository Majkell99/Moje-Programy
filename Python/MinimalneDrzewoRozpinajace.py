import numpy as np

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
                    self.graf[wezel1][wezel2] = edge
                    self.graf[wezel2][wezel1] = edge
            else:
                self.graf[wezel1][wezel2] = edge
                self.graf[wezel2][wezel1] = edge
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


class drzewoRozpinajace:
    def __init__(self, graf: listaSasiedztwa):
        #self.graf = graf
        self.intree = {klucz: False for klucz in graf.vertices()} # dict.fromkeys(graf, False)
        self.distance = {klucz: float('inf') for klucz in graf.vertices()} #dict.fromkeys(graf, float('inf'))
        self.parent = {klucz: None for klucz in graf.vertices()} #dict.fromkeys(graf, None)
        self.drzewo = listaSasiedztwa()

        w = list(graf.graf.keys())[0]
        suma_krawedzi = 0
        #self.distance[w] = 0 - Po co to?
        while True:
            self.intree[w] = True
            self.drzewo.insert_vertex(w)
            
            for i in graf.graf[w]:
                if self.intree[i] == False and graf.graf[w][i] < self.distance[i]:
                    self.distance[i] = graf.graf[w][i]   
                    self.parent[i] = w

            #Teraz dalej trzeba znalezc kolejny wierzcholek
            minimum = float('inf')
            nastepny_w = None
            for i in graf.graf:
                if self.intree[i] == False and self.distance[i] < minimum:
                    minimum = self.distance[i]
                    nastepny_w = i
            
            if nastepny_w == None:
                break
            
            suma_krawedzi += minimum
            self.drzewo.insert_vertex(nastepny_w)

            rodzic = self.parent[nastepny_w] #Po co tu brac rodzica?
            self.drzewo.insert_edge(rodzic, nastepny_w, minimum)
            # self.drzewo.insert_edge(nastepny_w, rodzic, minimum)

            w = nastepny_w



graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]

listaWezlow = []
for i in graf:
    wezel1 = wezel(i[0])
    wezel2 = wezel(i[1])
    listaWezlow.append((wezel1, wezel2, i[2]))

grafLista = listaSasiedztwa()

for i in listaWezlow:
    grafLista.insert_vertex(i[0])
    grafLista.insert_vertex(i[1])
    
    grafLista.insert_edge(i[0], i[1], i[2])

drzewoMST = drzewoRozpinajace(grafLista)

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

printGraph(drzewoMST.drzewo)


