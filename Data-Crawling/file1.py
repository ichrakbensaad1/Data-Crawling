
import pandas as pd
import numpy as np
from tkinter import * 
import tkinter as tk
from tkinter import filedialog






class myFrame1(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        frame = startPage(container, self)  
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[startPage] = frame

        self.show_frame(startPage)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()




class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        label = tk.Label(self, text = "-------------StartPage: This is the draft -------------------")
        label.pack(pady = 10, padx = 10)

        b0 = tk.Button(self, text="Read in Data", command = self.readData )
        b0.pack(padx=5, pady=5)
        b0.config(width = 30, bg = 'GRAY')

        
        b1 = tk.Button(self, text = "Agree and go to next page", command = test)
        b1.pack()


    tkcalc = pd.DataFrame()
    tkidname = ['0-----0']

    def readData(self):
        global tkcalc
        global tkidname
        filename = filedialog.askopenfilename(filetypes=[("csv file", ".csv")],defaultextension=".csv")
        tkcalc = pd.read_csv(filename)
        print (tkcalc.head())


def test():

    # df = pd.DataFrame(np.random.randn(20, 15), columns=list('ABCDEFGHIJKLMNO'))



    def cbc(tex):
        return lambda : callback(tex)

    def callback(tex):
        myreturn = var1.get().split('------')[0]
        df = tkcalc.ix[tkcalc.loanid == int(myreturn), 2:]
        s = '-'*80 + "print of loanid = " + var1.get() + '-'*60 + "\n"*2 + df.to_string(index = False) + "\n"*3
        tex.insert(tk.END, s)
        tex.see(tk.END)             # Scroll if necessary

    popup = tk.Tk()
    tex = tk.Text(master=popup, width=240, height=50)
    tex.pack(side='bottom', expand = True)

    lst1 = tkidname
    var1 = tk.StringVar(popup)
    var1.set(lst1[0])
    dropdown = tk.OptionMenu(popup, var1, *lst1)
    dropdown.config(width = 60, bg = 'GREEN')
    dropdown.pack(side='top', padx=5, pady=5)


    b = tk.Button(popup, text="Print Select Loan Calculation", command=cbc(tex) )
    b.pack(padx=5, pady=5)
    b.config(width = 30, bg = 'GRAY')

    b1 = tk.Button(popup, text='Exit Program', command=popup.destroy)
    b1.pack(padx=5, pady=5)
    b1.config(width = 30, bg = 'WHITE')
    popup.mainloop()



app1 = myFrame1()
app1.mainloop()