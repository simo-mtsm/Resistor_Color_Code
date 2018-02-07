#!/usr/bin/python

class App():
    def __init__(self):
        self.root = Tk()

        # STAR LAWEL

        self.can = Canvas(self.root, width=280, height =100, bg ='white')
        self.can.grid(columnspan =5, pady =5, padx =5)
        self.can.create_line(10, 50, 240, 50, width =5) #
        self.can.create_rectangle(72, 30, 185, 70, fill ='light yellow', width =4)
        self.lab = Label(self.root, text='adkhil ra9m rest : ')
        self.lab.grid()
        self.can.create_rectangle(85,31,85+12,69,fill='black',width=0)
        self.can.create_rectangle(109,31,109+12,69,fill='black',width=0)
        self.can.create_rectangle(133,31,133+12,69,fill='black',width=0)
        self.can.create_rectangle(157,31,157+12,69,fill='black',width=0)

        Button(self.root,width=2, height=1, bg='red', command=lambda s=self, r='red',R='2': s.chR(r,R)).\
             grid(row =2, column =0)
        Button(self.root,width=2, height=1, bg='green', command=lambda s =self, r = 'green',R='4': s.chR(r,R)).\
             grid(row =3, column =0)
        Button(self.root,width=2, height=1, bg='blue', command=lambda s =self, r = 'blue': s.chG(r)).\
             grid(row =2, column =1)
        Button(self.root,width=2, height=1, bg='white', command=lambda s =self, r = 'white': s.chG(r)).\
             grid(row =3, column =1)
        Button(self.root,width=2, height=1, bg='yellow', command=lambda s =self, r = 'yellow': s.chk(r)).\
             grid(row =2, column =2)

        Button(self.root,width=2, height=1, bg='brown', command=lambda s =self, r = 'brown': s.chk(r)).\
             grid(row =3, column =2)



        self.root.mainloop()
    def chR(self, f,R):

        for x in range(85,109,24):#star stop step
            self.ligne.append(self.can.create_rectangle(x,30,x+12,70,fill=f,width=0))

    def chG(self, f):

        for x in range(109,133,24):#star stop step
            self.ligne.append(self.can.create_rectangle(x,30,x+12,70,fill=f,width=0))
    def chk(self, f):

        for x in range(133,157,24):#star stop step
            self.ligne.append(self.can.create_rectangle(x,30,x+12,70,fill=f,width=0))

        self.root.mainloop()
if __name__== '__main__':
    from Tkinter import *
    f = App()