###Projet arbre binaire de recherche (fenêtre n°1)

#Création d'une classe Arbre contenant les fonctions associées
class Arbre:
    def __init__(self, data,index = 1,line = 0):
        self.left = None
        self.right = None
        self.data = (data,index,line)

#Méthodes servant à créer les noeuds
    def insert(self, data,line = 0):
        if line == 3:
            return False
        if self.data:
            if data < self.data[0]:
                if self.left is None:
                    if self.data[0] == 1:
                        self.left = Arbre(data, 1,line+1)
                    else:
                        self.left = Arbre(data,(self.data[1]*2)-1,line+1)
                else:
                    return self.left.insert(data,line +1)
            elif data > self.data[0]:
                if self.right is None:
                    self.right = Arbre(data,self.data[1]*2,line+1)
                else:
                    return self.right.insert(data,line +1)
        else:
            self.data = (data)

        return True

#Utilisation de la méthode findval (find value) pour rechercher une valeur au sein de l'arbre
    def rechercher(self, lkpval):

        def findval(self,lkpval):
            if lkpval < self.data[0]:
                if self.left is None:
                    return False
                return self.left.rechercher(lkpval)
            elif lkpval > self.data[0]:
                if self.right is None:
                    return False
                return self.right.rechercher(lkpval)
            else:
                return self.data

        return findval(self,lkpval)

    def deleteNode(self,val):
        def minValueNode(node):
            current = node

            #Boucle while permettant de trouver la feuille la plus à gauche
            while (current.left is not None):
                current = current.left

            return current

        def deleteNode(root, key):
            if root is None:
                return root

            if key < root.data[0]:
                root.left = deleteNode(root.left, key)

            elif (key > root.data[0]):
                root.right = deleteNode(root.right, key)

            else:

                #Nœud avec un seul ou 0 fils
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp

                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp

                temp = minValueNode(root.right)

                root.data = temp.data
                root.right = deleteNode(root.right, temp.data[0])

            return root

        self = deleteNode(self,val)

    def infixe(self):
        list_returned = []
        def GND(Noeud):
            if Noeud == None:
                return

            GND(Noeud.left)
            list_returned.append(Noeud.data)
            GND(Noeud.right)

        GND(self)
        return list_returned

    def prefixe(self):
        list_returned = []
        def NGD(Noeud):
            if Noeud == None:
                return

            list_returned.append(Noeud.data)
            NGD(Noeud.left)
            NGD(Noeud.right)

        NGD(self)
        return list_returned

    def sufixe(self):
        list_returned = []
        def GDN(Noeud):
            if Noeud == None:
                return

            GDN(Noeud.left)
            GDN(Noeud.right)
            list_returned.append(Noeud.data)

        GDN(self)
        return list_returned

    def largeur(self):
        def BFS(Noeud):
            if Noeud is None:
                return

            file = []
            file.append(Noeud)

            while (len(file) > 0):
                #Affichage et retrait du premier élément
                print(file[0].data)
                node = file.pop(0)

                #Ajout du SAG de l'élément retiré
                if node.left is not None:
                    file.append(node.left)

                #Ajout du SAD de l'élément retiré
                if node.right is not None:
                    file.append(node.right)
        BFS(self)

    def getLargeur(self):
        def BFS(Noeud):
            if Noeud is None:
                return

            list_returned = []
            file = []
            file.append(Noeud)

            while (len(file) > 0):
                #Affichage et suppresion du premier élément
                list_returned.append(file[0].data)
                node = file.pop(0)

                #Ajout du SAG de l'élément retiré
                if node.left is not None:
                    file.append(node.left)

                #Ajout du SAD de l'élément retiré
                if node.right is not None:
                    file.append(node.right)
            return list_returned

        return BFS(self)


"""
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
                       \
                        88

root = Arbre(50)
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)
root.insert(88)

root.deleteNode(70)

root.largeur()

"""