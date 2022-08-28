from re import T
from tkinter import * 
import tkinter as tk
import numpy as np 
from tkinter import filedialog
import pandas as pd #Lecture des fichiers csv,etc. tableaux de données Dataframe

root = tk.Tk()

def open_file():
    browse_text.set("loading...")
    filepath = filedialog.askopenfilename(initialdir="file.py",
                                          title="Open file okay?",
                                          filetypes= (("fils csv","*.csv"),
                                          ("fils xml","*.xml")))
    file = open(filepath,'rb') 
    
    
    if file:
        
        data = pd.read_csv(file)

        #replacing missing values 
        data1=data.fillna(data.mean())
        #data1=data.fillna(data.min())
        #data1 = data.fillna(data.max())
        #data1=data.fillna(value='x',inplace=True)
        #data1=data.dropna(how ='any')
        
        #data.fillna(methode='bfill')
        
        #feature = list(data.columns)
        """def replace_most_freq(feature,data):
            data[feature].fillna(data[feature].value_counts().index[0], inplace = True)
            return data1"""


        """def replace_max(data):
            data=data.fillna(data.max())
            
            return data1 
        def replace_mean(data):
            data.fillna(data.mean(),inplace=True)
            return data1
        def replace_min(data):
            data.fillna(data.min(),inplace=True)
            return data1"""

        #data redundancy 
        data1=data.drop_duplicates()        


        #data normalization
        #utilisant Z_score 
        """outliers =[]
        def detect_outliers(data):
            threshold=3
            mean=np.mean(data)
            std=np.std(data)
            for i in data :
                z_score=(i-mean)/std
                if np.abs(z_score)>threshold:
                    outliers.append(i)
            return outliers"""


        #fil= detect_outliers(data)
        
        def replace_min(data):
            data.fillna(data.min(),inplace=True)
            return data1

        min_text.set("min")    

        

        fil= data1.isnull().sum()
        #text box
        text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
        text_box.insert(1.0,fil)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=1)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

min_text = tk.StringVar()
min_btn = tk.Button(root, textvariable=min_text,font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
min_text.set("min")
min_btn.grid(column=2, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=2)

max_text = tk.StringVar()
max_btn = tk.Button(root, textvariable=max_text,font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
max_text.set("max")
max_btn.grid(column=2, row=3)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=2)

mean_text = tk.StringVar()
mean_btn = tk.Button(root, textvariable=mean_text,font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
mean_text.set("mean")
mean_btn.grid(column=3, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=1)

mustfreq_text = tk.StringVar()
mustfreq_btn = tk.Button(root, textvariable=mustfreq_text,font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
mustfreq_text.set("must_freq")
mustfreq_btn.grid(column=4, row=3)
canvas = tk.Canvas(root,width=600, height=250)
canvas.grid(columnspan=2)

drop_text = tk.StringVar()
drop_btn = tk.Button(root, textvariable=drop_text,font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
drop_text.set("drop")
drop_btn.grid(column=4, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=1)

replcts_text = tk.StringVar()
replcts_btn = tk.Button(root, textvariable=replcts_text,font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
replcts_text.set("replace_constat")
replcts_btn.grid(column=3, row=3)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=4)


root.mainloop()


