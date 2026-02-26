class secondClass:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class oneWayList:
    def __init__(self):
        self.head = None
        lista = []
        self.lista = lista

    def create(self):
        pass #zrobione

    def destroy(self):
        self.head = None #zrobione

    def add(self, data):
        new_elem = secondClass(data)
        new_elem.next = self.head
        self.head = new_elem #zrobione

    def append(self, data):
        new_elem = secondClass(data)
        if(self.head is None):
            self.head = new_elem
            new_elem.next = None
        else:
            new_elem.next = None
            current_elem = self.head
            while (current_elem.next is not None):
                current_elem = current_elem.next
            current_elem.next = new_elem #zrobione

    def remove(self):
        if self.head is None:
            print("Lista jest pusta, wiec nie ma jak usunac pierwszego elementu")
        else:
            elem = self.head
            self.head = elem.next #zrobione

    def remove_end(self):
        if self.head is None:
            print("Lista jest pusta, wiec nie ma jak usunac ostatniego elementu")
        elif self.head.next is None:
            self.head = None
        else:
            current_elem = self.head
            while (current_elem.next.next is not None):
                current_elem = current_elem.next
            current_elem.next = None

    def is_empty(self) -> bool:
        return self.head is None #zrobione
    
    def length(self):
        size = 0
        elem = self.head
        while (elem  != None):
            size += 1
            elem = elem.next

        return size #zrobione

    def get(self):
        if self.head is None:
            return None
        else:
            elem = self.head
            return elem #zrobione
        
    def write(self):
        elem = self.head
        pomoc = []
        while elem is not None:
            pomoc.append(elem)
            elem = elem.next 
        wypisanie = "-> " + "\n-> ".join(map(str, pomoc)) #zrobione
        print(wypisanie)


lista = [('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]

elem1 = secondClass(lista[0])
elem2 = secondClass(lista[1])
elem3 = secondClass(lista[2])
elem4 = secondClass(lista[3])
elem5 = secondClass(lista[4])
elem6 = secondClass(lista[5])

uczelnie = oneWayList()

uczelnie.append(elem1)
uczelnie.append(elem2)
uczelnie.append(elem3)

uczelnie.add(elem4)
uczelnie.add(elem5)
uczelnie.add(elem6)

uczelnie.write()

print(uczelnie.length())

uczelnie.remove()

print(uczelnie.get())

uczelnie.remove_end()

uczelnie.write() #

uczelnie.destroy()
print(uczelnie.is_empty())

uczelnie.remove()

uczelnie.remove_end()

uczelnie.append(elem1)

uczelnie.remove_end()

print(uczelnie.is_empty())









