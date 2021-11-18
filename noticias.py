from tkinter import *
import os
from tkinter import ttk

site = "site.com"
mes = "mes"

class Tela:

    def __init__(self, event):

        cab = PhotoImage(file="cab.png")
        self.lb_cab = Label(janela, image=cab)
        self.lb_cab.cab = cab
        self.lb_cab.place(x=0,y=0)

        self.cab2 = Label(janela, text="Notícias Google")
        self.cab2["font"] = ("roboto", "30", "italic")
        self.cab2.config(foreground="#191970")
        self.cab2.place(x=220,y=100)

        self.palavra = Label(janela, text="Buscar por:")
        self.palavra["font"] = ("lucida console", "20")
        self.palavra.config(foreground="#DC143C")
        self.palavra.place(x=110,y=210)

        self.palavraE = Entry(janela)
        self.palavraE["font"] = ("lucida console", "18")
        self.palavraE.config(foreground="#696969", bg="lightgrey")
        self.palavraE.place(x=300,y=212, width=370)

        self.mes = Label(janela, text="Mês da publicação:")
        self.mes["font"] = ("lucida console", "20")
        self.mes.config(foreground="black")
        self.mes.place(x=110,y=290)

        meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
        self.mesE = ttk.Combobox(janela, values=meses)
        self.mesE["font"] = ("Helvetica", "17")
        self.mesE.place(x=410,y=290, width=200)

        self.site = Label(janela, text="Site:")
        self.site["font"] = ("lucida console", "20")
        self.site.config(foreground="black")
        self.site.place(x=315,y=370)

        sites = ["R7 Notícias", "G1 Notícias", "Notícias UOL", "Terra Notícias", "CNN Brasil"]
        self.siteE = ttk.Combobox(janela, values=sites)
        self.siteE["font"] = ("Helvetica", "17")
        self.siteE.place(x=410,y=370, width=200)

        bt_buscar = Button(janela, text="Buscar")
        bt_buscar["font"] = ("Lucida Console", "20")
        bt_buscar.config(bg="green", foreground="white")
        bt_buscar.place(x=410, y=470)
        bt_buscar.bind("<Button-1>", self.buscar)

        bt_limpar = Button(janela, text="Limpar")
        bt_limpar["font"] = ("Lucida Console", "20")
        bt_limpar.config(bg="brown", foreground="white")
        bt_limpar.place(x=230, y=470)
        bt_limpar.bind("<Button-1>", self.limpar)

        bt_limpabusca = Button(janela, text="X")
        bt_limpabusca["font"] = ("Lucida Console", "18")
        bt_limpabusca.config(bg="black", foreground="red")
        bt_limpabusca.place(x=685, y=212, height=25, width=25)
        
        bt_limpabusca.bind("<Button-1>", self.limpar2)

    def limpar(self, event):

        self.palavraE.delete(0, "end")
        self.mesE.delete(0, "end")
        self.siteE.delete(0, "end")

    def limpar2(self, event):

        self.palavraE.delete(0, "end")

    def buscar(self, event):

        global site
        global mes
        
        busca = self.palavraE.get()
        mes = self.mesE.get()
        site = self.siteE.get()

        if site == "R7 Notícias":
            site = "r7.com"
            
        if site == "G1 Notícias":
            site = "g1.globo.com"

        if site == "Notícias UOL":
            site = "noticias.uol.com.br"

        if site == "Terra Notícias":
            site = "terra.com.br"

        if site == "CNN Brasil":
            site = "cnnbrasil.com.br"
            
        
        
        if mes == "JANEIRO":
            mes = "01"

        if mes == "FEVEREIRO":
            mes = "02"

        if mes == "MARÇO":
            mes = "03"

        if mes == "ABRIL":
            mes = "04"

        if mes == "MAIO":
            mes = "05"
            
        if mes == "JUNHO":
            mes = "06"

        if mes == "JULHO":
            mes = "07"

        if mes == "AGOSTO":
            mes = "08"

        if mes == "SETEMBRO":
            mes = "09"

        if mes == "OUTUBRO":
            mes = "10"

        if mes == "NOVEMBRO":
            mes = "11"

        if mes == "DEZEMBRO":
            mes = "12"



        pesquisa = ("https://www.google.com/search?q=site%3A{}+intext%3A{}+intext%3A{}%2F2021".format(site,busca,mes))
        os.system("start chrome {}".format(pesquisa))
        
        
        


janela = Tk()
Tela(janela)
janela.resizable(width=False, height=False)
janela.title("Notícias")
janela.geometry("750x550")
janela.mainloop()

