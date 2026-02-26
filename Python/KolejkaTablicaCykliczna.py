from copy import deepcopy

class kolejka:
    def __init__(self):
        self.rozmiar = 5
        self.tab = [None for i in range(self.rozmiar)]
        self.indexZapisu = 0
        self.indexOdczytu = 0

    def is_empty(self):
        return self.indexZapisu == self.indexOdczytu
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.indexOdczytu] #?
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            if self.indexOdczytu + 1 == self.rozmiar:
                self.indexOdczytu = 0
            else:
                self.indexOdczytu += 1

            return self.tab[self.indexOdczytu - 1] #?
        
    def enqueue(self, data):
        self.tab[self.indexZapisu] = data

        if self.indexZapisu + 1 == self.rozmiar:
            self.indexZapisu = 0
        else:
            self.indexZapisu += 1

        if self.is_empty():
            staryRozmiar = self.rozmiar
            self.rozmiar = self.rozmiar * 2
            tab2 = deepcopy(self.tab)
            self.tab = [None for i in range(self.rozmiar)]

            i = 0
            while i != self.indexZapisu:
                self.tab[i] = tab2[i]
                i += 1
            
            j = 0
            while j != staryRozmiar:
                self.indexOdczytu += 1
                j += 1

            # for j in range(staryRozmiar - 1):
            #     self.indexOdczytu += 1

            pomocIndex = self.indexOdczytu
            while pomocIndex != self.rozmiar:
                self.tab[pomocIndex] = tab2[i]
                i += 1
                pomocIndex += 1

    def __str__(self):
        i = self.indexOdczytu
        pomoc = []
        while i != self.indexZapisu:
            pomoc.append(self.tab[i])
            if i + 1 == self.rozmiar:
                i = 0
            else:
                i += 1
            
        napis = "[" + " ".join(map(str, pomoc)) + "]"
        print(napis)
    
    def wypiszDlaTestu(self):
        print(self.tab)    

            # na poczatku na miejscu 3 byl None i tam tez byl indexZapisu (indexOdczytu na 4), na miejscu tego 
            # indexuZapisu wpisujemy data (trojke) potem zwiekszamy indexZapisu o 1 i wtedy
            # indexy się sobie rownają i po trojce wpisujemy None az do indexuOdczytu (4), a indexZapisu zostaje na pierwszym None
            # [1, 2, 3, 4, 5, 6, 7]
            # [1, 2, 3, None, None, None, None, None, None, 4, 5, 6, 7]

kolejka_ = kolejka()

kolejka_.enqueue(1)
kolejka_.enqueue(2)
kolejka_.enqueue(3)
kolejka_.enqueue(4)

print(kolejka_.dequeue())

print(kolejka_.peek())

kolejka_.__str__() 

kolejka_.enqueue(5)
kolejka_.enqueue(6)
kolejka_.enqueue(7)
kolejka_.enqueue(8)

kolejka_.wypiszDlaTestu()

while not kolejka_.is_empty():
    print(kolejka_.dequeue())

kolejka_.__str__()








        








