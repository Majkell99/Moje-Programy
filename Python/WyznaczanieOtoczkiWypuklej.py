def Jarvis(punkty : list):
    skrajny_lewo = punkty[0]
    for i in punkty:
        if skrajny_lewo[0] > i[0]:
            skrajny_lewo = i
        elif skrajny_lewo[0] == i[0]:
            if skrajny_lewo[1] > i[1]:
                skrajny_lewo = i
    
    indeks_skrajny_lewo = punkty.index(skrajny_lewo)
    if len(punkty) - 1 == indeks_skrajny_lewo:
        q = punkty[0] #albo punkty[indeks_skrajny_lewo - 1]
    else:
        q = punkty[indeks_skrajny_lewo + 1]

    p = skrajny_lewo

    punkty_wielokatu = []
    punkty_wielokatu.append(p)
    while True: #q != skrajny_lewo:
        for i in punkty:
            if i != p and i != q:
                r = i
                x1 = p[0]
                y1 = p[1]
                x2 = q[0]
                y2 = q[1]
                x3 = r[0]
                y3 = r[1]

                if (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1) > 0: #prawoskretny
                    q = r

        if q == skrajny_lewo:
            break  

        punkty_wielokatu.append(q)
        p = q

        indeks_p = punkty.index(p)
        if len(punkty) - 1 == indeks_p:
            q = punkty[0] #albo punkty[indeks_skrajny_lewo - 1]
        else:
            q = punkty[indeks_p + 1]

    return punkty_wielokatu


lista1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
lista2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]

print(Jarvis(lista1))
#print('\n')
print(Jarvis(lista2))
print('\n')

def Jarvis2(punkty : list):
    skrajny_lewo = punkty[0]
    for i in punkty:
        if skrajny_lewo[0] > i[0]:
            skrajny_lewo = i
        elif skrajny_lewo[0] == i[0]:
            if skrajny_lewo[1] > i[1]:
                skrajny_lewo = i
    
    indeks_skrajny_lewo = punkty.index(skrajny_lewo)
    if len(punkty) - 1 == indeks_skrajny_lewo:
        q = punkty[0] #albo punkty[indeks_skrajny_lewo - 1]
    else:
        q = punkty[indeks_skrajny_lewo + 1]

    p = skrajny_lewo

    punkty_wielokatu = []
    punkty_wielokatu.append(p)
    while True: #q != skrajny_lewo
        for i in punkty:
            if i != p and i != q:
                r = i
                x1 = p[0]
                y1 = p[1]
                x2 = q[0]
                y2 = q[1]
                x3 = r[0]
                y3 = r[1]

                if (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1) > 0: #prawoskretny
                    q = r
                if (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1) == 0: #współliniowe
                    if (min(p[0], r[0]) < q[0] < max(p[0], r[0]) or min(p[1], r[1]) < q[1] < max(p[1], r[1])):
                        q = r

        if q == skrajny_lewo:
            break

        punkty_wielokatu.append(q)
        p = q

        indeks_p = punkty.index(p)
        if len(punkty) - 1 == indeks_p:
            q = punkty[0] #albo punkty[indeks_skrajny_lewo - 1]
        else:
            q = punkty[indeks_p + 1]

    return punkty_wielokatu

lista3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

print(Jarvis2(lista1))
print(Jarvis2(lista2))
print('\n')

print("Pierwsza wersja algorytmu")
print(Jarvis(lista3))
print('\n')

print("Druga wersja algorytmu")
print(Jarvis2(lista3))