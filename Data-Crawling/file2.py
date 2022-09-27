from asyncio.windows_events import NULL
from datetime import date
from re import T
from tkinter import * 
import tkinter as tk
import tkinter
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np 
from tkinter import filedialog

import pandas as pd 
import os 
from sklearn.decomposition import PCA 
import seaborn as sns
from tkinter import ttk
from tkinter.messagebox import showinfo
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
        
        #fil= list(data.columns)
        fil= data.isnull().sum()
        print(data.info())
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
# TextBox Creation

def replace_min():

        global data1
        x=att_search.get()
        data[x]=data[x].fillna(data[x].min()) 
        data1=data[x]
        fil= data.isnull().sum()
        text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
        text_box.insert(1.0,fil)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=4)
        min_text.set("min")  
        """if save_btn == True :
            data.to_csv(data2,index=False) """
        return data1

mustfreq_text = tk.StringVar()
mustfreq_btn = tk.Button(root, textvariable=mustfreq_text,command=lambda:mustfreq(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
mustfreq_text.set("must_freq")
mustfreq_btn.grid(column=4, row=3)
canvas = tk.Canvas(root,width=600, height=250)
canvas.grid(columnspan=5)
def mustfreq():
    global data 
    feature = list(data.columns)
    #my_tree["columns"] = [i for i in df.columns]
    data6=data[feature].fillna(data[feature].value_counts().index[0], inplace = True)
    fil= data6.isnull().sum()
    text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
    text_box.insert(1.0,fil)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=4)

    mustfreq_text.set("must_freq")

max_text = tk.StringVar()
max_btn = tk.Button(root, textvariable=max_text, command=lambda:replace_max(),font="Raleway", bg="#20bebe", fg="white", height=1, width=5)
max_text.set("max")
max_btn.grid(column=2, row=3)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=2)  
def replace_max():
    global data 
    x=att_search.get()
    data[x]=data[x].fillna(data[x].max())        
    
    fil= data.isnull().sum()
    text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
    text_box.insert(1.0,fil)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=4)

    max_text.set("max")
    
mean_text = tk.StringVar()
mean_btn = tk.Button(root, textvariable=mean_text,command=lambda:replace_mean(),font="Raleway", bg="#20bebe", fg="white",height=1, width=5)
mean_text.set("mean")
mean_btn.grid(column=3, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=5)

def replace_mean():
            global data 
            x=att_search.get()
            data[x]=data[x].fillna(data[x].mean()) 
            fil= data.isnull().sum()
            #imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
            #imputer = Imputer.fit(imputer,X[:,1:3])
            #X[:, 1:3] = Imputer.transform(imputer,X[:, 1:3])
            text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
            text_box.insert(1.0,fil)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=4)

            mean_text.set("mean")
            
drop_text = tk.StringVar()
drop_btn = tk.Button(root, textvariable=drop_text,command=lambda:drop(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
drop_text.set("drop")
drop_btn.grid(column=4, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=1)


def drop():
            global data 
            x=att_search.get()
            data[x]=data[x].fillna(data[x].dropna) 
            data1=data.read()
            fil= data.isnull().sum()
            text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
            text_box.insert(1.0,fil)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=4)
            drop_text.set("drop")
             


replcts_text = tk.StringVar()

replcts_btn = tk.Button(root, textvariable=replcts_text,command=lambda:replace_constat(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
replcts_text.set("replace_constat")
replcts_btn.grid(column=3, row=3)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=2)


def replace_constat():
            global data 
            x=att_search.get()
            data[x]=data[x].fillna(value='x') 
            
            fil= data.isnull().sum()
            text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
            text_box.insert(1.0,fil)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=4)
            replcts_text.set("replace_constat")
            
                

            
save_text = tk.StringVar()
save_btn = tk.Button(root, textvariable=save_text,command=lambda:savedb(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
save_text.set("save")
save_btn.grid(column=4, row=4)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)










def savedb():
   
    data1.to_csv('data6.csv', index=False)
       
       

             
sca_text = tk.StringVar()
sca_btn = tk.Button(root, textvariable=sca_text,command=lambda:scaling(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
sca_text.set("scaling")
sca_btn.grid(column=0, row=4)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=2)
       
def scaling():
    scaler= StandardScaler()
    fill1=scaler.fit_transform(data)
    fil= fill1.isnull().sum()
    print(fill1)
    
    
    
    text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
    text_box.insert(1.0,fil)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=4)
    sca_text.set("sca")
            
z_score_text = tk.StringVar()
z_score_btn = tk.Button(root, textvariable=z_score_text,command=lambda:z_score(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
z_score_text.set("z_score")
z_score_btn.grid(column=0, row=3)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

#outliers=[]            
def z_score():
        x=att_search.get()

        #threshold=3
        mean=np.mean(data[x])
        std=np.std(data[x])
        
        z_score=(data[x]-mean)/std
        print(z_score)

        """if np.abs(z_score)>threshold:
                outliers.append(i)"""
        text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
        text_box.insert(1.0,z_score)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=4)
        z_score_text.set("z_score")
        

#Detecting Outliers
def DBscan ():
    
    scaler = StandardScaler()
    scaled_X = scaler.fit_transform(data)
    X =data[[col for col in data. Columns if data[col].dtypes != "str"  ]]
    #categorical_features=[list(data.columns)]
    outlier_percent = []

    for eps in np.linspace(0.001,3,50):
    
    # Create Model
        dbscan = DBSCAN(eps=eps,min_samples=2*scaled_X.shape[1])
        dbscan.fit(scaled_X)

   
     
    # Log percentage of points that are outliers
    perc_outliers = 100 * np.sum(dbscan.labels_ == -1) / len(dbscan.labels_)
    
    outlier_percent.append(perc_outliers)
    fil=sns.lineplot(x=np.linspace(0.001,3,50),y=outlier_percent)
    
    print(scaled_X)
    #X = pd.get_dummies(data.iloc[:,0:4],columns = categorical_features) 

    pca = PCA(n_component =2)
    X_principal = pca.fit_transform(X)

    db = DBSCAN(metric='euclidean',eps=0.3,min_samples=10,algorithm='auto').fit(X_principal)#it can be ball_tree, kd_tree, brute
    fil = db.labels_
    n_clusters = len (set(labels))- (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)
    print(n_clusters)


    text_box = tk.Text(root, height=10, width=60, padx=20, pady=15)
    text_box.insert(1.0,fil)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=4)
    dbsc_text.set("dbsc")
            
dbsc_text = tk.StringVar()
dbsc_btn = tk.Button(root, textvariable=dbsc_text,command=lambda:DBscan(),font="Raleway", bg="#20bebe", fg="white", height=1, width=8)
dbsc_text.set("dbsc")
dbsc_btn.grid(column=0, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

frame_search = root


lbl_search = Label(frame_search, text='le nom de attribut ',
                   font=('bold', 12), pady=25)
lbl_search.grid(row=0, column=0)
att_search = StringVar()
att_search_entry = Entry(frame_search, textvariable=att_search)
att_search_entry.grid(row=0, column=1)


root.mainloop()


