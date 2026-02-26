import math
import random
import time

class elemKolejki:
    def __init__(self, __dane, __priorytet):
        self.__dane = __dane
        self.__priorytet = __priorytet

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet
    
    def __gt__(self, other):
        return self.__priorytet > other.__priorytet
    
    def __repr__(self):
        reprezentacja = f"{self.__priorytet} : {self.__dane}"
        return reprezentacja #gotowe
    
class kolejka:
    def __init__(self, tablica = None):
        if tablica is None:
            self.kolejka = [] #tablica
            self.rozmiarKopca = 0
        else:
            self.kolejka = tablica
            self.rozmiarKopca = len(self.kolejka)

            i = self.rozmiarKopca - 1
            while i > 0:
                self.naprawaPoUsunieciu(self.rodzic(i))
                i -= 1

    def is_empty(self):
        if self.rozmiarKopca == 0:
            return True
        else:
            return False #gotowe
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.kolejka[0] #gotowe
        
    def lewo(self, indeks):
        return 2*indeks + 1
    
    def prawo(self, indeks):
        return 2*indeks + 2
    
    def rodzic(self, indeks):
        return math.ceil(indeks/2 - 1)
    
    def naprawaPoUsunieciu(self, index = 0): #indeks dodany ze wzgl. na to ze przyda sie to w innym kodzie
        i = index
        doNaprawy = self.kolejka[index]
        while i < self.rozmiarKopca:
            if self.lewo(i) < self.rozmiarKopca:
                lewe = self.kolejka[self.lewo(i)] 
            else:
                lewe = None
            
            if self.prawo(i) < self.rozmiarKopca:
                prawe = self.kolejka[self.prawo(i)] 
            else:
                prawe = None

            if lewe is not None and prawe is not None:
                if doNaprawy < prawe and not(lewe > prawe):
                    self.kolejka[i] = prawe
                    self.kolejka[self.prawo(i)] = doNaprawy
                    i = self.prawo(i)
                elif doNaprawy < lewe and lewe > prawe:
                    self.kolejka[i] = lewe
                    self.kolejka[self.lewo(i)] = doNaprawy
                    i = self.lewo(i)
                else:
                    return 
            elif lewe is not None and prawe is None:
                if doNaprawy < lewe:
                    self.kolejka[i] = lewe
                    self.kolejka[self.lewo(i)] = doNaprawy
                    i = self.lewo(i)
                else:
                    return
            elif lewe is None and prawe is not None:
                if doNaprawy < prawe:
                    self.kolejka[i] = prawe
                    self.kolejka[self.prawo(i)] = doNaprawy
                    i = self.prawo(i)
                else:
                    return #
            else:
                return #nie ma prawego ani lewego

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            zwracanie = self.kolejka[0]
            self.kolejka[0] = self.kolejka[self.rozmiarKopca - 1]
            self.kolejka[self.rozmiarKopca - 1] = zwracanie
            self.rozmiarKopca -= 1
            self.naprawaPoUsunieciu()
            return zwracanie
        
    def naprawaPoDodaniu(self, indeks):
        i = indeks
        doNaprawy = self.kolejka[i]
        while i > 0:
            if self.kolejka[self.rodzic(i)] < doNaprawy:
                pomoc = self.kolejka[self.rodzic(i)]
                self.kolejka[self.rodzic(i)] = doNaprawy
                self.kolejka[i] = pomoc
                i = self.rodzic(i)
            else:
                return
            
    def enqueue(self, dane):
        if self.rozmiarKopca == len(self.kolejka):
            self.rozmiarKopca += 1
            self.kolejka.append(dane)
            self.naprawaPoDodaniu(self.rozmiarKopca - 1)
        else:
            self.rozmiarKopca += 1
            self.kolejka[self.rozmiarKopca - 1] = dane
            self.naprawaPoDodaniu(self.rozmiarKopca - 1)

    def print_tab(self):
        print ('{', end=' ')
        print(*self.kolejka[:self.rozmiarKopca], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx = 0, lvl = 0):
        if idx<self.rozmiarKopca:           
            self.print_tree(self.prawo(idx), lvl+1)
            print(2*lvl*'  ', self.kolejka[idx] if self.kolejka[idx] else None)           
            self.print_tree(self.lewo(idx), lvl+1)

def test1():
    lista =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    listaElem = []
    for priorytet, dane in lista:
        listaElem.append(elemKolejki(dane, priorytet))
    
    k = kolejka(listaElem)
    k.print_tab()
    print('\n')
    k.print_tree()

    i = len(listaElem) - 1
    while i >= 0:
        k.dequeue()
        i -= 1

    print(k.kolejka)
    print("NIESTABILNE")

##
def wybieranie1(lista):
    for j in range(len(lista)):
        minimum = lista[j]
        i = j
        indeks_min = j
        while i < len(lista):
            if lista[i] < minimum:
                minimum = lista[i]
                indeks_min = i
            i += 1
        lista[j], lista[indeks_min] = lista[indeks_min], lista[j]

def wybieranie2(lista):
    for j in range(len(lista)):
        minimum = lista[j]
        i = j
        indeks_min = j
        while i < len(lista):
            if lista[i] < minimum:
                minimum = lista[i]
                indeks_min = i
            i += 1
        minimum = lista.pop(indeks_min)
        lista.insert(j, minimum)

lista1 = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
lista1_ = []
for i in lista1:
    lista1_.append(elemKolejki(i[1], i[0]))

wybieranie1(lista1_)
print(lista1_)
print("NIESTABILNY")

print("\n")
lista2 = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
lista2_ = []
for i in lista2:
    lista2_.append(elemKolejki(i[1], i[0]))

wybieranie2(lista2_)
print(lista2_)
print("STABILNY")

def test2():
    lista1 = []
    for i in range(0, 10000):
        losowaLiczba = int(random.random() * 100)
        lista1.append(losowaLiczba)
    
    lista2 = lista1.copy()
    lista3 = lista1.copy()

    t_start = time.perf_counter()
    # listaElem = []
    # for i in lista1:
    #     listaElem.append(elemKolejki(i, i))
    
    k = kolejka(lista1)

    i = len(lista1) - 1
    while i >= 0:
        k.dequeue()
        i -= 1

    # print(k.kolejka)
    t_stop = time.perf_counter()
    print("Czas obliczeń kopiec:", "{:.7f}".format(t_stop - t_start))


    t_start = time.perf_counter()
    wybieranie1(lista2)
    t_stop = time.perf_counter()
    print("Czas obliczeń wybieranie1:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    wybieranie2(lista3)
    t_stop = time.perf_counter()
    print("Czas obliczeń wybieranie2:", "{:.7f}".format(t_stop - t_start))

def main():
    print("Wybierz opcję: ")
    wybor = input()

    if wybor == "1":
        test1()
    elif wybor == "2":
        test2()
    else:
        print("Wybrałeś złą opcję")

main()

    
