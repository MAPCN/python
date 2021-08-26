from tkinter import *
class MenuBar(Frame):
	def __init__(self, boss =None):
		Frame.__init__(self, borderwidth =2)
		fileMenu = Menubutton(self, text ='Menu')
		fileMenu.pack(side =LEFT)
		me1 = Menu(fileMenu)
		me1.add_command(label ='START', underline =0,command = boss.effacer)
		me1.add_command(label ='Effacer', underline =0,command = boss.effacer)
		me1.add_command(label ='Terminer', underline =0,command = boss.quit)
		fileMenu.configure(menu = me1)
class Application(Frame):
	def __init__(self, boss =None):
		Frame.__init__(self)
		self.master.title('Fenêtre avec menus')
		mBar = MenuBar(self)
		mBar.pack()
		self.can = Canvas(self, bg='light blue', height=190,width=250, borderwidth =2)
		self.can.pack()
		self.pack()
	def commencer(self):
		self.can.play(ALL)
	def effacer(self):
		self.can.delete(ALL)
if __name__ == '__main__':
	app = Application()
	app.mainloop()