import mapa

class wezel:
    def __init__(self, klucz, nazwa = None):
        self.klucz = klucz
        self.nazwa = nazwa
        
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

    def insert_edge(self, wezel1, wezel2, edge = None):
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
        if self.graf[wezel1][wezel2] == self.parametr_macierzy:
            print("Miedzy tymi wezlami nie ma krawedzi!")
        else:
            self.graf[wezel1][wezel2] = self.parametr_macierzy
            self.graf[wezel2][wezel1] = self.parametr_macierzy

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
    

mapa.draw_map(mapa.graf)