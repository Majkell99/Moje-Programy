import math

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
    def __init__(self):
        self.kolejka = [] #tablica
        self.rozmiarKopca = 0
        #self.tablica = [] 

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
                lewe = self.kolejka[self.lewo(i)] #self.kolejka[2*i+1]
            else:
                #print("Wyjscie poza zakres")
                lewe = None
            
            if self.prawo(i) < self.rozmiarKopca:
                prawe = self.kolejka[self.prawo(i)] #self.kolejka[2*i+2]
            else:
                #print("Wyjscie poza zakres")
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
                    return #doNaprawy jest na swoim miejscu
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
                    return
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


k = kolejka()

lista = [7, 5, 1, 2, 5, 3, 4, 8, 9]
wyraz = 'GRYMOTYLA'
for i, litera in enumerate(wyraz):
    elem = elemKolejki(litera, lista[i])
    k.enqueue(elem)

k.print_tree()
print('\n')
k.print_tab()
print('\n')
zapamietaj = k.dequeue()
print('\n')
print(k.peek())
print('\n')
k.print_tab()
print('\n')
print(zapamietaj)
print('\n')

while not k.is_empty():
    print(k.dequeue())

print('\n')
k.print_tab()

    

