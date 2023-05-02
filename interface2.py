#coding:utf-8
# from fonctions import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Test(object):
	def __init__(self,fen):
		super(Test, self).__init__()
		self.fen = fen
		self.fen.title("Test")
		w = 800
		h = 600
		ws =  int(self.fen.winfo_screenwidth()) 
		hs =  int(self.fen.winfo_screenheight())
		x = int((ws/2) - (w/2)) 
		y = int((hs/2) - (h/2) )
		self.fen.geometry("{}x{}+{}+{}".format(w,h,x,y))#1024,768
		#self.fen.maxsize(800,600)
		self.fen.resizable(False, False)

		self.a = StringVar()
		self.b=StringVar()
		self.c=StringVar()
		self.d=StringVar()
		
		def Reset():
			self.a.set("")
			self.b.set("")
			self.c.set("")
			self.d.set("")

			self.LMasseEau.config(text="")
			self.LMasseEc.config(text="")
			self.LMasseVEau.config(text="")
			self.LMasseVEc.config(text="")
			self.LDensite.config(text="")
			self.LDensiteC.config(text="")
		def Calcul():
			try: 
				a = float(self.a.get())
				b= float(self.b.get())
				c = float(self.c.get())
				d = float(self.d.get())

				assert b > 0
				assert a >  0
				assert c > 0
				assert d > 0
				assert b >  a
				assert c > a
			except:
				tkinter.messagebox.showerror("Wholesaler","Erreur de saisie!")
				#Reset()
			else:
				me = b-a
				mec = c-a
				mve = me/d
				mvech = mec/d
				densite = mve/mvech
				densiteC = densite*mve
				self.LMasseEau.config(text = str(me))
				self.LMasseEc.config(text = str(mec))
				self.LMasseVEau.config(text=str(mve))
				self.LMasseVEc.config(text=str(mvech))
				self.LDensite.config(text=str(densite))
				self.LDensiteC.config(text=str(densiteC))
		#------------------------------------------------------
		self.topFrame = Frame(self.fen,height=90,bg= "#55ACEE")
		self.topFrame.pack(fill='x')
		
		self.logoFrameIspm = Frame(self.topFrame,height=90,bg= "#55ACEE")
		self.logoFrameIspm.pack(side="left",ipady=5)
		
		self.titleFrame = Frame(self.topFrame,width=100,height=90,bg= "#55ACEE")
		self.titleFrame.pack(side="left",padx=80,ipady=5)
		
		self.logoFrameCnrit = Frame(self.topFrame,height=90,bg= "#55ACEE")
		self.logoFrameCnrit.pack(side="right",ipady=5)
		
		self.bottomFrame =Frame(self.fen,bg= "#292F33")
		self.bottomFrame.pack(expand=1,fill='both')
		
		self.leftFrame = Frame(self.bottomFrame,bg="#66757F",height=300)
		self.leftFrame.pack(side="left",expand=1,fill="both",padx=10,pady=15)
		
		self.rightFrame = Frame(self.bottomFrame,bg="#66757F",height=300)
		self.rightFrame.pack(side="left",expand=1,fill="both",padx=10,pady=15)
		
		global ispm
		global cnrit
		ispm =  PhotoImage(file="image/logo_ispm.png")
		cnrit =  PhotoImage(file="image/cnrit2.png")
		self.labelispm = Label(self.logoFrameIspm,image=ispm,width=60,height=50,bg=self.topFrame['bg'])
		self.labelispm.pack(side="left",expand=1,padx=5)
		self.labelcnrit = Label(self.logoFrameCnrit,image=cnrit,width=
		60,height=50,bg=self.topFrame['bg'])
		self.labelcnrit.pack(side="left",expand=1,padx=5)
		
		self.titleLabel = Label(self.titleFrame,text= "CALCUL DE LA DENSITE PAR PYCNOMETRE",fg="#FFFFFF",bg=self.topFrame['bg'],font=('Georgia',14,'bold'))
		self.titleLabel.pack(side="left",expand=1,ipady=10)
		#self.formFrame = Frame(self.leftFrame,bg = self.leftFrame['bg'],height=600)
		#self.formFrame.pack(fill="y",pady= 30)

		labels = (('Poids du pycnomètre vide :',0),('Poids du pycnomètre + eau :',2),('Poids du pycnomètre + echantillon :',4),('Volume du pycnomètre :',6))
		for elt in labels:
			Label(self.leftFrame,text=elt[0],fg="#FFFFFF",bg=self.leftFrame['bg'],font=('Georgia',10,'bold')).grid(sticky="w",row=elt[1],column=0,padx=10,pady=15)

		entry = ((1,self.a),(3,self.b),(5,self.c),(7,self.d))
		for elt in entry:
			Entry(self.leftFrame,font=('Georgia',10,'bold'),width=20,textvariable=elt[1]).grid(sticky="w",row=elt[0],column=0,padx=10,pady = 5)

		self.btnFrame = Frame(self.leftFrame,width=100,bg=self.leftFrame['bg'])
		self.btnFrame.grid(sticky="w",row=8,column=0,padx=10,pady = 5)

		self.btnOk = Button(self.btnFrame,justify="center",text="CALCULER",fg='#292F33',bg ="#55ACEE",font=('GEORGIA',10,'bold'),bd=0,command = Calcul)
		self.btnOk.grid(sticky="w",row=0,column=0,pady =20,ipadx=10,ipady=10)
		self.btnReset = Button(self.btnFrame,justify="center",text="REINITIALISER",fg='#292F33',bg ="#55ACEE",font=('GEORGIA',10,'bold'),bd=0,command = Reset)
		self.btnReset.grid(sticky="w",row=0,column=1,padx=10,pady =20,ipadx=10,ipady=10)

		self.labelResultFrame = Frame(self.rightFrame,height=50,bg = "#55ACEE")
		self.labelResultFrame.pack(fill="x")
		self.resultFrame =Frame(self.rightFrame,bg= "#292F33")
		self.resultFrame.pack(expand=1,fill='both')
		
		self.labelResult = Label(self.labelResultFrame,text="RESULTATS",fg="#FFFFFF",bg=self.labelResultFrame['bg'],font=('Georgia',14,'bold'))
		self.labelResult.pack(expand=1,padx=20,pady=10)

		labels1 = (('Masse de l\'eau :',0),('Masse de l\'echantillon :',2),('Masse volumique de l\'eau :',4),('Masse volumique de l\'echantillon :',6),('Densité :',8),('Densité à 15°C :',10))
		for elt in labels1:
			Label(self.resultFrame,text=elt[0],fg="#FFFFFF",bg=self.resultFrame['bg'],font=('Georgia',10,'bold')).grid(sticky="w",row=elt[1],column=0,padx=10,pady=15)

		self.LMasseEau = Label(self.resultFrame,text="",fg="#FFFFFF",bg=self.leftFrame['bg'],width=20,font=('Georgia',12,'bold'))
		self.LMasseEau.grid(sticky="w",row=1,column=0,padx=10,pady=0)
		self.LMasseEc = Label(self.resultFrame,text="",fg="#FFFFFF",bg=self.leftFrame['bg'],width=20,font=('Georgia',12,'bold'))
		self.LMasseEc.grid(sticky="w",row=3,column=0,padx=10,pady=0)
		self.LMasseVEau = Label(self.resultFrame,text="",fg="#FFFFFF",bg=self.leftFrame['bg'],width=20,font=('Georgia',12,'bold'))
		self.LMasseVEau.grid(sticky="w",row=5,column=0,padx=10,pady=0)
		self.LMasseVEc = Label(self.resultFrame,text="",fg="#FFFFFF",bg=self.leftFrame['bg'],width=20,font=('Georgia',12,'bold'))
		self.LMasseVEc.grid(sticky="w",row=7,column=0,padx=10,pady=0)
		self.LDensite = Label(self.resultFrame,text="",fg="#FFFFFF",bg=self.leftFrame['bg'],width=20,font=('Georgia',12,'bold'))
		self.LDensite.grid(sticky="w",row=9,column=0,padx=10,pady=0)
		self.LDensiteC = Label(self.resultFrame,text="",fg="#FFFFFF",bg=self.leftFrame['bg'],width=20,font=('Georgia',12,'bold'))
		self.LDensiteC.grid(sticky="w",row=11,column=0,padx=10,pady=0)
		#------------------------------------------------------	
if __name__ == '__main__':
	root = Tk()
	application = Test(root)
	root.mainloop()