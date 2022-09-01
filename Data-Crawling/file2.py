from asyncio.windows_events import NULL
from re import T
from tkinter import * 
import tkinter as tk
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np 
from tkinter import filedialog
import pandas as pd 
#from sklearn.preprocessing import Imputer

root = tk.Tk()
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=1)
canvas = tk.Canvas(root, width=200, height=50)
canvas.grid(columnspan=3)
def open_file():
    global data
    browse_text.set("loading...")
    filepath = filedialog.askopenfilename(initialdir="file.py",
                                          title="Open file okay?",
                                          filetypes= (("fils csv","*.csv"),
                                          ("fils xml","*.xml")))
    file = open(filepath,'rb') 
    
    
    if file:
        
        data = pd.read_csv(file)
       

        fil= data.isnull().sum()
        #text box
        text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
        text_box.insert(1.0,fil)
        text_box.tag_configure("left", justify="center")
        text_box.tag_add("left", 1.0, "end")
        text_box.grid(column=1, row=3)
        browse_text.set("Browse")
       


min_text = tk.StringVar()
min_btn = tk.Button(root, textvariable=min_text, command=lambda:replace_min(),font="Raleway", bg="#20bebe", fg="white", height=1, width=5)
min_text.set("min")
min_btn.grid(column=2, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=2)         
        
def replace_min():
        
        data2=data.fillna(data.min())
        fil= data2.isnull().sum()
        text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
        text_box.insert(1.0,fil)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        min_text.set("min")  
mustfreq_text = tk.StringVar()
mustfreq_btn = tk.Button(root, textvariable=mustfreq_text,command=lambda:mustfreq(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
mustfreq_text.set("must_freq")
mustfreq_btn.grid(column=4, row=3)
canvas = tk.Canvas(root,width=600, height=250)
canvas.grid(columnspan=5)
def mustfreq():
    feature = list(data.columns)
    #my_tree["columns"] = [i for i in df.columns]
    data6=data[feature].fillna(data[feature].value_counts().index[0], inplace = True)
    fil= data6.isnull().sum()
    text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
    text_box.insert(1.0,fil)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=3)

    mustfreq_text.set("must_freq")

max_text = tk.StringVar()
max_btn = tk.Button(root, textvariable=max_text, command=lambda:replace_max(),font="Raleway", bg="#20bebe", fg="white", height=1, width=5)
max_text.set("max")
max_btn.grid(column=2, row=3)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=2)  
def replace_max():       
    data3=data.fillna(data.max())
    fil= data3.isnull().sum()
    text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
    text_box.insert(1.0,fil)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=3)

    max_text.set("max")
    
mean_text = tk.StringVar()
mean_btn = tk.Button(root, textvariable=mean_text,command=lambda:replace_mean(),font="Raleway", bg="#20bebe", fg="white",height=1, width=5)
mean_text.set("mean")
mean_btn.grid(column=3, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=5)

def replace_mean():
            data1=data.fillna(data.mean())
            fil= data1.isnull().sum()
            #imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
            #imputer = Imputer.fit(imputer,X[:,1:3])
            #X[:, 1:3] = Imputer.transform(imputer,X[:, 1:3])
            text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
            text_box.insert(1.0,fil)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=3)

            mean_text.set("mean")
            
drop_text = tk.StringVar()
drop_btn = tk.Button(root, textvariable=drop_text,command=lambda:drop(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
drop_text.set("drop")
drop_btn.grid(column=4, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=1)


def drop():
            
            data1=data.dropna(axis=0,how='any')
            fil= data1.isnull().sum()
            text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
            text_box.insert(1.0,fil)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=3)
            max_text.set("drop")



replcts_text = tk.StringVar()
replcts_btn = tk.Button(root, textvariable=replcts_text,command=lambda:replace_constat(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
replcts_text.set("replace_constat")
replcts_btn.grid(column=3, row=3)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=2)


def replace_constat():
            data4=data.fillna(value='x')
            fil= data4.isnull().sum()
            text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
            text_box.insert(1.0,fil)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=3)
            replcts_text.set("replace_constat")
            
             
sca_text = tk.StringVar()
sca_btn = tk.Button(root, textvariable=sca_text,command=lambda:scaling(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
sca_text.set("scaling")
sca_btn.grid(column=4, row=4)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)
       
def scaling():
    scaler= MinMaxScaler()
    #fill=scaler.fit(data)
    fill1=scaler.transform(data)
    fil=data.head(3)
    
    text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
    text_box.insert(1.0,fil)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=4)
    sca_text.set("sca")
            
    













root.mainloop()


