class wezelDrzewa:
    def __init__(self, klucz, wartosc):
        self.klucz = klucz
        self.wartosc = wartosc
        self.lewo = None
        self.prawo = None
        

class korzen:
    def __init__(self):
        self.root = None

    # def search(self, klucz):
    #     return self.search2(self.root, klucz)

    def search(self, wezel, klucz):
        if wezel is None:
            return None 
        
        if klucz < wezel.klucz:
            wezel = wezel.lewo
            return self.search(wezel, klucz)
        elif klucz > wezel.klucz:
            wezel = wezel.prawo
            return self.search(wezel, klucz)
        else:
            return wezel.wartosc
    
        
    def insert(self, node, key, data):    
        if node == None: 
            node = wezelDrzewa(key, data)
            return node  
        if key < node.klucz:                    
            node.lewo = self.insert(node.lewo, key, data)          
            return node     
        elif key > node.klucz:      
            node.prawo = self.insert(node.prawo, key, data)                  
            return node    
        else:
            node.wartosc = data 
            return node
    
    def delete(self, wezel, klucz):
        if wezel is None:
            print("Ten wezel jest pusty!")
        if wezel.klucz == klucz:
            if wezel.prawo is None and wezel.lewo is None:
                return None
            elif wezel.prawo is None and wezel.lewo is not None:
                return wezel.lewo
            elif wezel.prawo is not None and wezel.lewo is None:
                return wezel.prawo
            else:
                pomoc = wezel.prawo
                while pomoc.lewo is not None:
                    pomoc = pomoc.lewo
                wezel.wartosc = pomoc.wartosc
                wezel.klucz = pomoc.klucz
                wezel.prawo = self.delete(wezel.prawo, pomoc.klucz)
        elif wezel.klucz > klucz:
            wezel.lewo = self.delete(wezel.lewo, klucz)
        else:
            wezel.prawo = self.delete(wezel.prawo, klucz)

        return wezel

    def height(self, wezel):        
        if wezel is None:
            return 0
        
        lewy = self.height(wezel.lewo)
        prawy = self.height(wezel.prawo)

        return 1 + max(lewy, prawy)
        
        
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.prawo, lvl+5)

            print()
            print(lvl*" ", node.klucz, node.wartosc)
     
            self.__print_tree(node.lewo, lvl+5)


drzewo = korzen()

drzewo.root = drzewo.insert(drzewo.root, 50, 'A')
drzewo.root = drzewo.insert(drzewo.root, 15, 'B')
drzewo.root = drzewo.insert(drzewo.root, 62, 'C')
drzewo.root = drzewo.insert(drzewo.root, 5, 'D')
drzewo.root = drzewo.insert(drzewo.root, 20, 'E')
drzewo.root = drzewo.insert(drzewo.root, 58, 'F')
drzewo.root = drzewo.insert(drzewo.root, 91, 'G')
drzewo.root = drzewo.insert(drzewo.root, 3, 'H')
drzewo.root = drzewo.insert(drzewo.root, 8, 'I')
drzewo.root = drzewo.insert(drzewo.root, 37, 'J')
drzewo.root = drzewo.insert(drzewo.root, 60, 'K')
drzewo.root = drzewo.insert(drzewo.root, 24, 'L')

drzewo.print_tree()
#drzewo.print(drzewo.root)

print(drzewo.search(drzewo.root, 24))

drzewo.root = drzewo.insert(drzewo.root, 20, 'AA')
drzewo.root = drzewo.insert(drzewo.root, 6, 'M')
drzewo.root = drzewo.delete(drzewo.root, 62)
drzewo.root = drzewo.insert(drzewo.root, 59, 'N')
drzewo.root = drzewo.insert(drzewo.root, 100, 'P')
drzewo.root = drzewo.delete(drzewo.root, 8)
drzewo.root = drzewo.delete(drzewo.root, 15)
drzewo.root = drzewo.insert(drzewo.root, 55, 'R')
drzewo.root = drzewo.delete(drzewo.root, 50)
drzewo.root = drzewo.delete(drzewo.root, 5)
drzewo.root = drzewo.delete(drzewo.root, 24)

print(drzewo.height(drzewo.root))
#drzewo.print()
drzewo.print_tree()

#Nie zrobiłem funkcji print



            


        


    








        








