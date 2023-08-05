import random
from GUI import *

class MainProgamme(object):
    def __init__(self):
        main = Tk()
        main.option_add('*Font', '19')
        main.geometry("400x400")  # Dimensions de la fenetre
        main.title("Arbres binaires de recherche")  # Nom de la fenetre. Reference à un jeu de plateau similaire
        main.resizable(False, False)  # On empeche de redimensionner la fenetre

        root = Arbre(random.randint(0, 99)) #On utilise la fonction randint pour générer un ABR aléatoirement

        for i in range(0, 100):
            root.insert(random.randint(0, 99))

        Menu(main, root)


if __name__ == '__main__':
   MainProgamme()
