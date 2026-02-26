import time

def obliczanie_kosztu_zmiany(wzorzec, i, tekst, j):
    if i == 0:
        return j
    if j == 0:
        return i
    
    koszt_wstawienia = 1 + obliczanie_kosztu_zmiany(wzorzec, i, tekst, j-1)
    koszt_usuniecia = 1 + obliczanie_kosztu_zmiany(wzorzec, i - 1, tekst, j)
    koszt_wymiany = obliczanie_kosztu_zmiany(wzorzec, i - 1, tekst, j - 1) + (1 if wzorzec[i-1] != tekst[j-1] else 0)

    return min(koszt_wstawienia, koszt_usuniecia, koszt_wymiany)

P = ' kot'
T = ' pies'

# t_start = time.perf_counter()
koszt = obliczanie_kosztu_zmiany(P, len(P), T, len(T))
# t_stop = time.perf_counter()
# print(f"Czas obliczeń: {t_stop - t_start:.7f}")
print(koszt)
print('\n')


def PD(wzorzec, i, tekst, j):
    D = [[0 for _ in range(j)] for _ in range(i)]
    r = [['X' for _ in range(j)] for _ in range(i)]
    for n in range(i):
        for m in range(j):
            if n == 0 and m != 0:
                r[n][m] = 'I'
            
            if n != 0 and m == 0:
                r[n][m] = 'D'

    for n in range(j):
        D[0][n] = n
    for n in range(i):
        D[n][0] = n

    for n in range(1, i):
        for m in range(1, j):   
            koszt_wstawienia = 1 + D[n][m-1]
            koszt_usuniecia = 1 + D[n-1][m]
            koszt_wymiany = D[n-1][m-1] + (wzorzec[n] != tekst[m])

            min_koszt = min(koszt_wstawienia, koszt_usuniecia, koszt_wymiany)
            D[n][m] = min_koszt
            if min_koszt == koszt_wstawienia:
                r[n][m] = 'I'
            elif min_koszt == koszt_usuniecia:
                r[n][m] = 'D'
            else:
                if min_koszt == D[n-1][m-1]:
                    r[n][m] = 'M'
                else:
                    r[n][m] = 'S'

    koszt = D[i-1][j-1]
    tab_przeksztalcen = []

    i -= 1
    j -= 1
    while r[i][j] != 'X':

        if r[i][j] == 'M' or r[i][j] == 'S':
            tab_przeksztalcen.append(r[i][j])
            i -= 1  
            j -= 1
        elif r[i][j] == 'D':
            tab_przeksztalcen.append(r[i][j])
            i -= 1
        else:
            tab_przeksztalcen.append(r[i][j])
            j -= 1
            
    return koszt, ''.join(tab_przeksztalcen[::-1])

P = ' thou shalt not'
T = ' you should not'
wynikPD = PD(P, len(P), T, len(T))
kosztPD = wynikPD[0]
napisPD = wynikPD[1]
print(kosztPD)
print(napisPD)
#print(PD(P, len(P), T, len(T)))
print('\n')


def PD_podciagi(wzorzec, i, tekst, j):
    D = [[0 for _ in range(j)] for _ in range(i)]
    r = [['X' for _ in range(j)] for _ in range(i)]
    for n in range(i):
        for m in range(j): 
            if n != 0 and m == 0:
                r[n][m] = 'D'

    for n in range(i):
        D[n][0] = n

    for n in range(1, i):
        for m in range(1, j):   
            koszt_wstawienia = 1 + D[n][m-1]
            koszt_usuniecia = 1 + D[n-1][m]
            koszt_wymiany = D[n-1][m-1] + (wzorzec[n] != tekst[m])

            min_koszt = min(koszt_wstawienia, koszt_usuniecia, koszt_wymiany)
            D[n][m] = min_koszt
            if min_koszt == koszt_wstawienia:
                r[n][m] = 'I'
            elif min_koszt == koszt_usuniecia:
                r[n][m] = 'D'
            else:
                if min_koszt == D[n-1][m-1]:
                    r[n][m] = 'M'
                else:
                    r[n][m] = 'S'

    minimum_last_wiersz = min(D[i-1][:])
    indeks_last = D[i-1].index(minimum_last_wiersz)
    koszt = D[i-1][indeks_last]
            
    return koszt, indeks_last

P = ' ban'
T = ' mokeyssbanana'

wynikPD = PD_podciagi(P, len(P), T, len(T))
print(wynikPD[0])
print(wynikPD[1])
print(f"Indeks pod ktorym zaczyna sie szukany podciag to {wynikPD[1] - len(P) + 2}")
print('\n')


def PD_sekwencja(wzorzec, i, tekst, j):
    D = [[0 for _ in range(j)] for _ in range(i)]
    r = [['X' for _ in range(j)] for _ in range(i)]
    for n in range(i):
        for m in range(j):
            if n == 0 and m != 0:
                r[n][m] = 'I'
            
            if n != 0 and m == 0:
                r[n][m] = 'D'

    for n in range(j):
        D[0][n] = n
    for n in range(i):
        D[n][0] = n

    for n in range(1, i):
        for m in range(1, j):   
            koszt_wstawienia = 1 + D[n][m-1]
            koszt_usuniecia = 1 + D[n-1][m]
            koszt_wymiany = D[n-1][m-1] + (999999 if wzorzec[n] != tekst[m] else 0)  

            min_koszt = min(koszt_wstawienia, koszt_usuniecia, koszt_wymiany)
            D[n][m] = min_koszt
            if min_koszt == koszt_wstawienia:
                r[n][m] = 'I'
            elif min_koszt == koszt_usuniecia:
                r[n][m] = 'D'
            else:
                if min_koszt == D[n-1][m-1]:
                    r[n][m] = 'M'
                else:
                    r[n][m] = 'S'

    koszt = D[i-1][j-1]
    tab_przeksztalcen = []

    indeksy = []
    i -= 1
    j -= 1
    while r[i][j] != 'X':

        if r[i][j] == 'M' or r[i][j] == 'S':
            tab_przeksztalcen.append(r[i][j])
            indeksy.append(i)
            i -= 1  
            j -= 1
        elif r[i][j] == 'D':
            tab_przeksztalcen.append(r[i][j])
            i -= 1
        else:
            tab_przeksztalcen.append(r[i][j])
            j -= 1

    odtworzona_sciezka = ''.join(tab_przeksztalcen[::-1])
    
    wynik = ''
    for n in indeksy:
        wynik += wzorzec[n]

    return odtworzona_sciezka, wynik[::-1] #Dokoncz

P = ' democrat'
T = ' republican'

wynik = PD_sekwencja(P, len(P), T, len(T))
print(wynik[0])
print(wynik[1])
print('\n') 


T = ' 243517698'
P = ''.join(sorted(T))
#print(P)

wynik = PD_sekwencja(P, len(P), T, len(T))
print(wynik[0])
print(wynik[1])