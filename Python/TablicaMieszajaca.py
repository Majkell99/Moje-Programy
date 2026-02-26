class elementy:
    def __init__(self, klucz, wartosc):
        self.klucz = klucz
        self.wartosc = wartosc
    
    def __str__(self):
        napis = f"{self.klucz}:{self.wartosc}"
        return napis
    
    #

class mieszajaca:
    def __init__(self, rozmiar, c1 = 1, c2 = 0):
        self.rozmiar = rozmiar
        self.tab = [None for i in range(self.rozmiar)]
        self.c1 = c1
        self.c2 = c2

    def mieszanie(self, data):
        if isinstance(data, (int, float)):
            data = int(data)
        elif isinstance(data, str):
            data = sum(ord(litera) for litera in data)
        else:
            return None
        
        return data % self.rozmiar #zrobione
    
    def kolizja(self, klucz, i):
        wynik = (klucz + self.c1 * i + self.c2 * i**2) % self.rozmiar
        return wynik

    def search(self, klucz):
        pomieszany_klucz = self.mieszanie(klucz)
        for i in range(self.rozmiar):
            indeks = self.kolizja(pomieszany_klucz, i)
            if self.tab[indeks] is None:
                return None
            elif self.tab[indeks].klucz == klucz:
                return self.tab[indeks].wartosc # w tablicy pod 0 indeksem jest powiedzmy obiekt klasy elementy zlozony z jakiegos
                #tu trzeba uzyc kolizji         # klucza i wartosci wiec jak chcemy sie dostac do klucza albo do wartosci to robimy
        return None                             # tab[0].klucz albo tab[0].wartosc

    def insert(self, klucz, wartosc):
        pomieszany_klucz = self.mieszanie(klucz)
        for i in range(self.rozmiar):
            indeks = self.kolizja(pomieszany_klucz, i)
            if self.tab[indeks] is None or self.tab[indeks].klucz == klucz: 
                self.tab[indeks] = elementy(klucz, wartosc)
                return
        print('Tablica jest pelna')
    

    def remove(self, klucz):
        pomieszany_klucz = self.mieszanie(klucz)
        for i in range(self.rozmiar):
            indeks = self.kolizja(pomieszany_klucz, i)
            if self.tab[indeks] is None:
                print('Pod tym kluczem nie ma wartosci!')
            elif self.tab[indeks].klucz == klucz:
                self.tab[indeks] = None
                return
            #tu trzeba uzyc kolizji

    def __str__(self):
        napis = "{"
        pomoc = []
        for i in self.tab:
            if i is None:
                pomoc.append(None)
            else:
                pomoc.append(i.__str__())
        napis += ", ".join(map(str, pomoc))
        napis += "}"
        return napis
    #czy nie moge tu uzyc .join po prostu na self.tab?



def test1(rozmiar, c1 = 1, c2 = 0):
    tablica1 = mieszajaca(rozmiar, c1, c2)
    litery = [chr(ord('A') + i) for i in range(0, 15)]
    for i in range(0, 15):
        if i == 6:
            tablica1.insert(18, litery[i])
        elif i == 7:
            tablica1.insert(31, litery[i])
        else:
            tablica1.insert(i+1, litery[i])

    print(tablica1.__str__())
    print(tablica1.search(5))
    print(tablica1.search(14))
    tablica1.insert(5, 'Z')
    print(tablica1.search(5))
    tablica1.remove(5)
    print(tablica1.__str__())
    print(tablica1.search(31))

    tablica1.insert('test', 'W')
    print(tablica1.__str__())


test1(13)
print('\n')

def test2(rozmiar, c1 = 1, c2 = 0):
    tablica2 = mieszajaca(rozmiar, c1, c2)
    litery = [chr(ord('A') + i) for i in range(0, 15)]
    k = 13
    for i in range(0, 15):
        tablica2.insert(k, litery[i])   
        k = k + 13
    print(tablica2.__str__())

test2(13) 
print('\n')
test2(13, 0, 1)
print('\n')
test1(13, 0, 1)




    








        








