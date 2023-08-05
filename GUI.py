### GUI Interface graphique principale
#Importation des modules
import threading
import time
from tkinter import *
import tkinter.messagebox
from Tree import *
from PIL import Image,ImageTk

class Menu:
    def __init__(self, root,tree = None):
        self.tree = Tree_GUI(tree)
        self.root = root
        self.frame = Frame(root, background="#B0E0E6")
        f_Calibri = ('Calibri',11,'bold')

        #Section principale
        self.canva_tree = Canvas(self.frame, width=400, height=300, background="#B0E0E6")
        self.tree.draw_tree(self.canva_tree)

        self.canva_tree.pack(expand=True, fill="both")

        #Boutons
        frame_btns = Frame(self.frame,background="#B0E0E6")

        self.b_settings = Button(frame_btns,font = f_Calibri, text= "Affichage et parcours",command = self.parcours)
        self.b_parcours = Button(frame_btns,font = f_Calibri, text= "Paramètres de l'arbre",command = self.parametre)

        self.b_settings.pack(pady = 10)
        self.b_parcours.pack()

        frame_btns.pack(expand = True,fill = "both")

        self.frame.pack(expand = True,fill = "both")
        self.root.mainloop()

    def parcours(self):
        self.frame.destroy()
        Parcours(self.root,self.tree.tree)

    def parametre(self):
        self.frame.destroy()
        Parametre(self.root,self.tree.tree)


class Parametre:
    def __init__(self, root, tree = None):
        self.tree = Tree_GUI(tree)
        self.root = root
        self.frame = Frame(root, background="#B0E0E6")
        f_Calibri = ('Calibri',11,'bold')

        #Section principale de l'arbre
        btn_img2 = Image.open("sortie.jpg")
        btn_img2 = btn_img2.resize((30, 30), Image.ANTIALIAS)

        my_img = ImageTk.PhotoImage(btn_img2)
        b_menu = Button(root,image=my_img,command = self.menu)

        b_menu.place(x = 5,y = 5)

        self.canva_tree = Canvas(self.frame,width = 400,height = 300,background="#B0E0E6")
        self.canva_tree.pack(expand = True,fill = "both")

        self.tree.draw_tree(self.canva_tree)

        #Boutons
        frame_btns = Frame(self.frame,height=83,width=400,background="#B0E0E6")

        btn_img1 = Image.open("keyboard.jpg") #clavier.png
        btn_img1 = btn_img1.resize((40, 30), Image.ANTIALIAS)

        my_img2 = ImageTk.PhotoImage(btn_img1)

        self.input = Entry(self.root,font = f_Calibri)
        self.b_clavier = Button(frame_btns,image=my_img2,font = f_Calibri,command = self.clavier)
        self.b_ajout = Button(frame_btns,font = f_Calibri,width = 15, text= "Ajouter",command = self.ajouter)
        self.b_supp = Button(frame_btns,font = f_Calibri, text= "Supprimer",width = 15, command = self.supprimer)
        self.b_recherche = Button(frame_btns, font=f_Calibri, text="Rechercher",width = 15, command = self.rechercher)
        self.b_new = Button(frame_btns, font=f_Calibri, text="Nouvel arbre" ,width = 15,command = self.nouvel_arbre)

        self.input.place(x = 130,y=270)
        self.b_clavier.place(x = 183,y=30)
        self.b_ajout.place(x = 30,y=10)
        self.b_supp.place(x = 250,y=10)
        self.b_recherche.place(x = 250,y=55)
        self.b_new.place(x = 30,y=55)

        frame_btns.pack(expand = True,fill = "both")

        self.frame.pack(expand = True,fill = "both")
        self.root.mainloop()

    def clavier(self):
        import tkinter as tk
        from tkinter import ttk

        key = Toplevel(self.root)  #Nom de la fenêtre clé
        key.title('Clavier')  #Nom de la fenêtre tkinter dediée au clavier

        def delete():
            tmp = self.input.get()
            equation.set(tmp[:-1])

        def press(num):
            tmp = self.input.get()
            tmp  += str(num)
            equation.set(tmp)

        #Configuration de la taille de la fenêtre
        key.geometry('581x180')  #Taille de la fenêtre
        key.maxsize(width=581, height=180)  #Taille maximale
        key.minsize(width=581, height=180)  #Taille minimale


        key.configure(bg='#75827e')

        equation = tk.StringVar()
        self.input['textvariable'] = equation

        A = ttk.Button(key, text='A', width=6, command=lambda: press('A'))
        A.grid(row=1, column=0, ipadx=6, ipady=10)

        Z = ttk.Button(key, text='Z', width=6, command=lambda: press('Z'))
        Z.grid(row=1, column=1, ipadx=6, ipady=10)

        E = ttk.Button(key, text='E', width=6, command=lambda: press('E'))
        E.grid(row=1, column=2, ipadx=6, ipady=10)

        R = ttk.Button(key, text='R', width=6, command=lambda: press('R'))
        R.grid(row=1, column=3, ipadx=6, ipady=10)

        T = ttk.Button(key, text='T', width=6, command=lambda: press('T'))
        T.grid(row=1, column=4, ipadx=6, ipady=10)

        Y = ttk.Button(key, text='Y', width=6, command=lambda: press('Y'))
        Y.grid(row=1, column=5, ipadx=6, ipady=10)

        U = ttk.Button(key, text='U', width=6, command=lambda: press('U'))
        U.grid(row=1, column=6, ipadx=6, ipady=10)

        I = ttk.Button(key, text='I', width=6, command=lambda: press('I'))
        I.grid(row=1, column=7, ipadx=6, ipady=10)

        O = ttk.Button(key, text='O', width=6, command=lambda: press('O'))
        O.grid(row=1, column=8, ipadx=6, ipady=10)

        P = ttk.Button(key, text='P', width=6, command=lambda: press('P'))
        P.grid(row=1, column=9, ipadx=6, ipady=10)

        #2ème ligne

        Q = ttk.Button(key, text='Q', width=6, command=lambda: press('Q'))
        Q.grid(row=2, column=0, ipadx=6, ipady=10)

        S = ttk.Button(key, text='S', width=6, command=lambda: press('S'))
        S.grid(row=2, column=1, ipadx=6, ipady=10)

        D = ttk.Button(key, text='D', width=6, command=lambda: press('D'))
        D.grid(row=2, column=2, ipadx=6, ipady=10)

        F = ttk.Button(key, text='F', width=6, command=lambda: press('F'))
        F.grid(row=2, column=3, ipadx=6, ipady=10)

        G = ttk.Button(key, text='G', width=6, command=lambda: press('G'))
        G.grid(row=2, column=4, ipadx=6, ipady=10)

        H = ttk.Button(key, text='H', width=6, command=lambda: press('H'))
        H.grid(row=2, column=5, ipadx=6, ipady=10)

        J = ttk.Button(key, text='J', width=6, command=lambda: press('J'))
        J.grid(row=2, column=6, ipadx=6, ipady=10)

        K = ttk.Button(key, text='K', width=6, command=lambda: press('K'))
        K.grid(row=2, column=7, ipadx=6, ipady=10)

        L = ttk.Button(key, text='L', width=6, command=lambda: press('L'))
        L.grid(row=2, column=8, ipadx=6, ipady=10)

        gi = ttk.Button(key, text='<-', width=6,command = delete)
        gi.grid(row=2, column=9, ipadx=6, ipady=10)

        #3ème ligne

        W = ttk.Button(key, text='W', width=6, command=lambda: press('W'))
        W.grid(row=3, column=0, ipadx=6, ipady=10)

        X = ttk.Button(key, text='X', width=6, command=lambda: press('X'))
        X.grid(row=3, column=1, ipadx=6, ipady=10)

        C = ttk.Button(key, text='C', width=6, command=lambda: press('C'))
        C.grid(row=3, column=2, ipadx=6, ipady=10)

        V = ttk.Button(key, text='V', width=6, command=lambda: press('V'))
        V.grid(row=3, column=3, ipadx=6, ipady=10)

        B = ttk.Button(key, text='B', width=6, command=lambda: press('B'))
        B.grid(row=3, column=4, ipadx=6, ipady=10)

        N = ttk.Button(key, text='N', width=6, command=lambda: press('N'))
        N.grid(row=3, column=5, ipadx=6, ipady=10)

        M = ttk.Button(key, text='M', width=6, command=lambda: press('M'))
        M.grid(row=3, column=6, ipadx=6, ipady=10)

        space = ttk.Button(key, text='Espace', width=6, command=lambda: press(' '))
        space.grid(row = 3 , column = 7,columnspan = 3 , ipadx = 65 , ipady = 10)

        #4ème ligne

        one = ttk.Button(key, text='1', width=6, command=lambda: press('1'))
        one.grid(row=4, column=0, ipadx=6, ipady=10)

        two = ttk.Button(key, text='2', width=6, command=lambda: press('2'))
        two.grid(row=4, column=1, ipadx=6, ipady=10)

        three = ttk.Button(key, text='3', width=6, command=lambda: press('3'))
        three.grid(row=4, column=2, ipadx=6, ipady=10)

        four = ttk.Button(key, text='4', width=6, command=lambda: press('4'))
        four.grid(row=4, column=3, ipadx=6, ipady=10)

        five = ttk.Button(key, text='5', width=6, command=lambda: press('5'))
        five.grid(row=4, column=4, ipadx=6, ipady=10)

        six = ttk.Button(key, text='6', width=6, command=lambda: press('6'))
        six.grid(row=4, column=5, ipadx=6, ipady=10)

        seven = ttk.Button(key, text='7', width=6, command=lambda: press('7'))
        seven.grid(row=4, column=6, ipadx=6, ipady=10)

        eight = ttk.Button(key, text='8', width=6, command=lambda: press('8'))
        eight.grid(row=4, column=7, ipadx=6, ipady=10)

        nine = ttk.Button(key, text='9', width=6, command=lambda: press('9'))
        nine.grid(row=4, column=8, ipadx=6, ipady=10)

        zero = ttk.Button(key, text='0', width=6, command=lambda: press('0'))
        zero.grid(row=4, column=9, ipadx=6, ipady=10)


        key.mainloop()
    def menu(self):
        self.frame.destroy()
        Menu(self.root,self.tree.tree)

    def ajouter(self):
        inp = self.input.get()
        self.input.delete(0,END)

        try:
            inp = int(inp)
        except:
            pass

        if inp == "" or (type(inp) == type(str()) and len(inp) > 1):
            tkinter.messagebox.showerror(title="Erreur de saisie",message="Vous devez saisir un nombre compris entre -99 et 99 ou bien un seul caractère pour les lettres")
            return

        tmp = self.tree.tree
        try :
            rep = tmp.insert(int(inp))

            if rep == False:
                tkinter.messagebox.showwarning(title="Attention",message="Vous avez entré le maximum de niveau veuillez en supprimer")
        except:
            rep = tmp.insert(inp[0])

            if rep == False:
                tkinter.messagebox.showwarning(title="Attention",message="Vous avez depassé le nombre maximal de niveaux")

        self.tree = Tree_GUI(tmp)
        self.tree.draw_tree(self.canva_tree)
        self.root.update()

    def supprimer(self):
        inp = self.input.get()
        self.input.delete(0, END)

        try:
            inp = int(inp)
        except:
            pass

        if inp == "" or (type(inp) == type(str()) and len(inp) > 1):
            tkinter.messagebox.showerror(title="Erreur de saisie",
                                         message="Vous devez saisir un nombre compris entre -99 et 99 ou bien un seul caractère pour les lettres")
            return

        tmp = self.tree.tree
        try:
            tmp.deleteNode(int(inp))
        except:
            tmp.deleteNode(inp[0])

        if tmp == None:
            tkinter.messagebox.showwarning(title="Racine",message="Vous ne pouvez pas supprimer la racine")
            return

        lst = tmp.getLargeur()

        new_tree = Arbre(lst[0][0])

        for i in range(1,len(lst)):
            new_tree.insert(lst[i][0])

        self.tree = Tree_GUI(new_tree)
        self.tree.draw_tree(self.canva_tree)
        self.root.update()

    def nouvel_arbre(self):
        inp = self.input.get()
        self.input.delete(0, END)

        try:
            inp = int(inp)
        except:
            pass

        if inp == "" or (type(inp) == type(str()) and len(inp) > 1):
            tkinter.messagebox.showerror(title="Nouvel arbre",
                                         message="Veuillez saisir une valeur correpondant à la racine de l'arbre")
            return

        if type(inp) == type(str()):
            new_tree = Arbre(inp[0])
            self.tree = Tree_GUI(new_tree)
        else:
            new_tree = Arbre(inp)
            self.tree = Tree_GUI(new_tree)

        self.tree.draw_tree(self.canva_tree)

    def rechercher(self):
            inp = self.input.get()
            self.input.delete(0, END)

            try:
                inp = int(inp)
            except:
                pass

            if inp == "" or (type(inp) == type(str()) and len(inp) > 1):
                tkinter.messagebox.showerror(title="Erreur de saisie",
                                             message="Vous devez saisir un noeud qui existe")
                return

            res = self.tree.tree.rechercher(inp)

            if res == False:
                return

            max_nodes = pow(2, res[2])

            r = 27
            x = (200 / max_nodes) + (res[1] - 1) * (400 / max_nodes)
            y = 50 + (res[2] * 50)
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r

            self.tree.draw_tree(self.canva_tree)
            self.canva_tree.create_oval(x0,y0,x1,y1,outline="#ba0f0f")

class Parcours:
    def __init__(self, root, tree = None):
        self.tree = Tree_GUI(tree)
        self.root = root
        self.frame = Frame(root, background="#B0E0E6")
        f_Calibri = ('Calibri',11,'bold')

        #Section principale
        btn_img2 = Image.open("sortie.jpg")
        btn_img2 = btn_img2.resize((30, 30), Image.ANTIALIAS)

        my_img = ImageTk.PhotoImage(btn_img2)
        b_menu = Button(root, image=my_img, command=self.menu)
        b_menu.place(x = 5,y = 5)

        self.canva_tree = Canvas(self.frame,width = 400,height = 300,background="#B0E0E6")
        self.tree.draw_tree(self.canva_tree)

        self.canva_tree.pack(expand = True,fill = "both")

        self.l_par = Label(root, font= f_Calibri,width = 44,height = 2)
        self.l_par.place(x = 25,y=245)

        #Section dédiée aux boutons
        frame_btns = Frame(self.frame,height=83,width=400,background="#B0E0E6")

        self.b_largeur = Button(frame_btns, font=f_Calibri, text="Largeur",width = 15,command = self.parcoursL)
        self.b_infix = Button(frame_btns, font=f_Calibri, text="Préfixe",width = 15,command = self.parcoursPr)
        self.b_sufixe = Button(frame_btns, font=f_Calibri, text="Suffixe",width = 15,command = self.parcoursSuf)
        self.b_postfixe = Button(frame_btns, font=f_Calibri, text="Postfixe",width = 15,command = self.parcoursPost)

        self.b_largeur.place(x = 30,y=10)
        self.b_infix.place(x = 30,y=50)
        self.b_sufixe.place(x = 240,y=10)
        self.b_postfixe.place(x = 240,y=50)

        frame_btns.pack(expand = True,fill = "both")

        self.frame.pack(expand = True,fill = "both")
        self.root.mainloop()

    def animate(self,listo):
        try:
            for ele in listo:
                res = self.tree.tree.rechercher(ele[0])

                if res == False:
                    return

                max_nodes = pow(2, res[2])

                r = 27
                x = (200 / max_nodes) + (res[1] - 1) * (400 / max_nodes)
                y = 50 + (res[2] * 50)
                x0 = x - r
                y0 = y - r
                x1 = x + r
                y1 = y + r


                self.canva_tree.create_oval(x0, y0, x1, y1,tags = "cercle_nihil", outline="#ba0f0f", width=3)
                time.sleep(0.5)
                self.canva_tree.delete("cercle_nihil")
                self.canva_tree.create_oval(x0+2 , y0+2, x1-2, y1-2,tags = "cercle_nihil2", outline="#FFFFF0", width=3)
                time.sleep(0.5)

            self.tree.draw_tree(self.canva_tree)
        except:
            pass

    def parcoursPost(self):
        ret = self.tree.tree.infixe()

        self.l_par['text'] = ""
        self.l_par['text'] += "|"
        for ele in ret:
            self.l_par['text'] += str(ele[0])+"|"

        t = threading.Thread(target=self.animate,args=(ret,))
        t.start()

    def parcoursSuf(self):
        ret = self.tree.tree.sufixe()

        self.l_par['text'] = ""
        self.l_par['text'] += "|"
        for ele in ret:
            self.l_par['text'] += str(ele[0]) + "|"
        t = threading.Thread(target=self.animate, args=(ret,))
        t.start()

    def parcoursPr(self):
        ret = self.tree.tree.prefixe()

        self.l_par['text'] = ""
        self.l_par['text'] += "|"
        for ele in ret:
            self.l_par['text'] += str(ele[0]) + "|"
        t = threading.Thread(target=self.animate, args=(ret,))
        t.start()

    def parcoursL(self):
        ret = self.tree.tree.getLargeur()

        self.l_par['text'] = ""
        self.l_par['text'] += "|"
        for ele in ret:
            self.l_par['text'] += str(ele[0]) + "|"
        t = threading.Thread(target=self.animate, args=(ret,))
        t.start()

    def menu(self):
        self.frame.destroy()
        Menu(self.root,self.tree.tree)


class Tree_GUI:
    def __init__(self,Arbre):
        self.tree = Arbre

    def create_circle(self,x, y, r,val, canvasName):  #Création de cercles avec coordonnées centrées
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r

        cercle = canvasName.create_oval(x0, y0, x1, y1, fill="#FFF")
        label = canvasName.create_text(x,y,fill="#75827e",font="Times 15 italic bold",text=str(val[0]))


        return [cercle,label]

    def draw_lines(self,listo,canvasName): #Création es lignes reliant les éléments de l'arbre
        def getEle(list,n,m):
            for ele in list:
                if ele[1] == n and ele[2]==m:
                    return ele

        for i in range (0,len(listo)):
            max_nodes = pow(2, listo[i][2])
            x1 = (200/max_nodes)+(listo[i][1]-1)*(400/max_nodes)
            y1 = 50+(listo[i][2]*50)

            if listo[i][1] == 1:
                con = getEle(listo,1,listo[i][2]-1)
            else:
                con = getEle(listo, (listo[i][1]/2), listo[i][2] - 1)

            if listo[i][1] == 3 and listo[i][2] == 2:
                con = getEle(listo, 2, 1)

            if listo[i][1] == 5 and listo[i][2] == 3:
                con = getEle(listo, 3, 2)

            if listo[i][1] == 7 and listo[i][2] == 3:
                con = getEle(listo, 4,2)

            elif listo[i][1] == 8 and listo[i][2] == 3:
                con = getEle(listo, 4,2)

            elif listo[i][1] == 3 and listo[i][2] == 3:
                con = getEle(listo, 2,2)

            if con:
                max_nodes = pow(2, con[2])
            else:
                continue
            x2 = (200 / max_nodes) + (con[1] - 1) * (400 / max_nodes)
            y2 = 50 + (con[2] * 50)


            canvasName.create_line(x1,y1,x2,y2, fill="#75827e", width=5)


    def draw_tree(self,canvasName):
        canvasName.delete("all")

        list_nodes = self.tree.getLargeur()
        self.draw_lines(list_nodes,canvasName)


        for node in list_nodes:
            max_nodes = pow(2,node[2])
            self.create_circle((200/max_nodes)+(node[1]-1)*(400/max_nodes), 50+(node[2]*50), 22, node, canvasName)



