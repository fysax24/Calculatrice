#coding:utf-8
# from fonctions import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Calculatrice(object):
	def __init__(self,fen):
		super(Calculatrice, self).__init__()
		self.fen = fen
		self.fen.title("Calculatrice")
		w = 400
		h = 500
		ws =  int(self.fen.winfo_screenwidth()) 
		hs =  int(self.fen.winfo_screenheight())
		x = int((ws/2) - (w/2)) 
		y = int((hs/2) - (h/2) )
		self.fen.geometry("{}x{}+{}+{}".format(w,h,x,y))#1024,768
		self.fen.resizable(False, False)
		self.equation = StringVar()
		self.expression = ""
		
		
		def click(bouton):
			if bouton == "=":
				calcul()
				return
			self.expression += bouton
			self.LabelShow.config(text = self.expression)
		
		def calcul():
			try:
				total = str(eval(self.expression))
				self.LabelShow.config(text = total)
			except:
				self.LabelShow.config(text = "Erreur")
				self.expression = ""
		self.FrameShow = Frame(self.fen,height= 80,bg="black")
		self.FrameShow.pack(side="top",fill="x")
		self.LabelShow = Label(self.FrameShow,text=self.equation,fg="#FFFFFF",font=('Georgia',18,'bold'),bg="yellow")
		self.LabelShow.pack(expand=1,fill="both",ipady=20)
		
		self.FrameCalcul =Frame(self.fen,bg="red")
		self.FrameCalcul.pack(side="top",fill="both")
		
		self.FrameDel =Frame(self.fen,height=80,bg="blue")
		self.FrameDel.pack(side="top",fill="x")
		self.LabelDel = Label(self.FrameDel,text="Delete",fg="#FFFFFF",font=('Georgia',18,'bold'),bg="blue")
		self.LabelDel.pack(expand=1,fill="both",ipady=20)
		
		buttons = (("7",0,0),("8",0,1),("9",0,2),("*",0,3),
					("4",1,0),("5",1,1),("6",1,2),("-",1,3),
					("1",2,0),("2",2,1),("3",2,2),("+",2,3),
					("0",3,0),(".",3,1),("/",3,2),("=",3,3),
		)
		for elt in buttons:
			b = Label(self.FrameCalcul,text = elt[0],fg="#FFFFFF",bg=self.FrameCalcul["bg"],font=('Georgia',14,'bold'))
			b.grid(sticky="w",row=elt[1],column=elt[2],ipadx=40,ipady=30)
			b.bind("<Button-1>",lambda e,bouton = elt[0]:click(bouton))
if __name__ == "__main__":
    root = Tk()
    application = Calculatrice(root)
    root.mainloop()