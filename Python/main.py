from webbrowser import Error


class Macierz:
    def __init__(self, macierz, wartosc = 0):
        self.__matrix = []
        if isinstance(macierz, tuple):
            for i in range(macierz[0]):
                kolumna = []
                for j in range(macierz[1]):
                    kolumna.append(wartosc)
                self.__matrix.append(kolumna)
        else:
            self.__matrix = macierz

    def __str__(self):
        wynik = ""
        for i in range(len(self.__matrix)):
            pomoc = []
            for j in range(len(self.__matrix[0])):
                pomoc.append(str(self.__matrix[i][j]))
            wynik = wynik + "|" + " ".join(pomoc) + "|\n"
        return wynik.strip()

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise ValueError
        else:
            matrix = Macierz((self.size()))
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[0])):
                    matrix.__matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]

        return matrix

    def __mul__(self, other):
        if self.size()[1] != other.size()[0]:
            raise ValueError
        else:
            matrix = Macierz((self.size()[0], other.size()[1]))
            for i in range(len(self.__matrix)): 
                for j in range(len(other.__matrix[0])):
                    for k in range(len(other.__matrix)):
                        matrix.__matrix[i][j] += self.__matrix[i][k] * other.__matrix[k][j]

        return matrix

    def __getitem__(self, index):
        wiersze, kolumny = index
        return self.__matrix[wiersze][kolumny]

    
def transpose(macierz: Macierz) -> Macierz:
    nowa_macierz = []
    for i in range(macierz.size()[1]):
        pomoc = []
        for j in range(macierz.size()[0]):
            pomoc.append(0)
        nowa_macierz.append(pomoc)

    for i in range(macierz.size()[0]):
        for j in range(macierz.size()[1]):
            nowa_macierz[j][i] += macierz[(i,j)]
    return Macierz(nowa_macierz)


m1 = Macierz(
[ [1, 0, 2],
  [-1, 3, 1] ]
)

m2 = Macierz(
[ [3, 1],
  [2, 1],
  [1, 0]]
)

print(transpose(m1))
print('\n')

m3 = Macierz((2, 3), 1)

print(m1+m3)
print("\n")
print(m1*m2)








