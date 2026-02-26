import time

with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()

def szukanieWzorca(tekst, wzorzec):
    licznik = 0
    t_start = time.perf_counter()

    dlugosc_w = len(wzorzec)
    dlugosc_t = len(tekst)

    if dlugosc_w > dlugosc_t:
        print("Wzorzec jest dluzszy niz tekst!")
        return 

    m = 0
    ilosc_wzorcow = 0
    numery_znakow = []

    while dlugosc_t > m:
        i = 0
        while dlugosc_w > i:
            licznik += 1
            if dlugosc_t <= m:
                 break
            if tekst[m] == wzorzec[i]:
                pierwszy_raz = True
                i += 1
                m += 1
                if i == dlugosc_w:
                     ilosc_wzorcow += 1
                     numery_znakow.append(m - dlugosc_w)
                     break
            else:
                if 'pierwszy_raz' not in locals():  
                    m += 1
                    break

                if pierwszy_raz:
                    pierwszy_raz = False
                    break
                else:
                    m += 1
                    break

    t_stop = time.perf_counter()
    #print(f"Czas obliczeń: {t_stop - t_start:.7f}")
    return ilosc_wzorcow, licznik, t_stop - t_start


# with open("test_wyszukiwania.txt", encoding='utf-8') as f1:
#         text1 = f1.readlines()

# test = ' '.join(text1).lower()

# wynik = szukanieWzorca(test, "abc")
# print(f"{wynik[0]};{wynik[1]};{wynik[2]}")

wynik2 = szukanieWzorca(S, "time.")
print(f"{wynik2[0]};{wynik2[1]};{wynik2[2]}")


def RabinKarp(tekst, wzorzec):
    t_start = time.perf_counter()

    N = len(wzorzec) 
    M = len(tekst)

    d = 256 
    q = 101  # liczba pierwsza

    def hash(word):
        hw = 0
        for i in range(N):  # N - to długość wzorca
            hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
        return hw
    
    hWzorzec = hash(wzorzec)

    licznik = 0
    ilosc_wzorcow = 0
    liczba_kolizji = 0
    numery_znakow = []
    for m in range(M-N+1):
        licznik += 1
        hTekst = hash(tekst[m : m+N])
        
        if hTekst == hWzorzec:
            if tekst[m : m+N] == wzorzec:
                numery_znakow.append(m)
                ilosc_wzorcow += 1
            else:
                liczba_kolizji += 1

    t_stop = time.perf_counter()
    return ilosc_wzorcow, licznik, liczba_kolizji, t_stop - t_start

wynikRabin = RabinKarp(S, 'time.')
print(f"{wynikRabin[0]};{wynikRabin[1]};{wynikRabin[2]};{wynikRabin[3]}")


def RabinKarp_RollingHasz(tekst, wzorzec):
    t_start = time.perf_counter()

    N = len(wzorzec) 
    M = len(tekst)

    d = 256 
    q = 101  # liczba pierwsza

    h = 1
    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q

    def hash(word):
        hw = 0
        for i in range(N):  # N - to długość wzorca
            hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
        return hw
    
    hWzorzec = hash(wzorzec)

    licznik = 0
    ilosc_wzorcow = 0
    liczba_kolizji = 0
    numery_znakow = []
    pierwszy_hash = hash(tekst[0:N])
    for m in range(M-N+1):
        licznik += 1

        # hTekst = (d * (hash(S[m:m+N-1]) - ord(S[m]) * h) + ord(S[m + N])) % q
        # if hTekst < 0:
        #     hTekst += q
        
        if pierwszy_hash == hWzorzec:
            if tekst[m : m+N] == wzorzec:
                numery_znakow.append(m)
                ilosc_wzorcow += 1
            else:
                liczba_kolizji += 1

        if m < M - N:
            pierwszy_hash = (d * (pierwszy_hash - ord(tekst[m]) * h) + ord(tekst[m + N])) % q
            if pierwszy_hash < 0:
                pierwszy_hash += q

    t_stop = time.perf_counter()
    return ilosc_wzorcow, licznik, liczba_kolizji, t_stop - t_start

wynikRabin_Rolling = RabinKarp_RollingHasz(S, 'time.')
print(f"{wynikRabin_Rolling[0]};{wynikRabin_Rolling[1]};{wynikRabin_Rolling[2]};{wynikRabin_Rolling[3]}")


def KMP_Table(wzorzec):
    N = len(wzorzec)
    #T = []
    T = [0] * (N + 1)
    pos = 1
    cnd = 0
    
    T[0] = -1

    while pos < N:
        if wzorzec[pos] == wzorzec[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and wzorzec[pos] != wzorzec[cnd]:
                cnd = T[cnd]

        pos += 1
        cnd += 1
    T[pos] = cnd
    return T

def KnuthMorrisPratt(tekst, wzorzec):
    t_start = time.perf_counter()
    T = KMP_Table(wzorzec)
    liczba_wzorcow = 0
    numery_znakow = []
    N = len(wzorzec)
    M = len(tekst)
    liczba_porownan = 0

    m = 0
    i = 0
    while m < M:
        liczba_porownan += 1
        if wzorzec[i] == tekst[m]:
            m += 1
            i += 1

            if i == N:
                numery_znakow.append(m - i)
                liczba_wzorcow += 1
                i = T[i]

        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    t_stop = time.perf_counter()
    return liczba_wzorcow, liczba_porownan, T


wynikKMP = KnuthMorrisPratt(S, 'time.')
print(f"{wynikKMP[0]};{wynikKMP[1]};{wynikKMP[2]}")