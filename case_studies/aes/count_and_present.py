
#get input files from  reports/*tmp_summary , count each error and present 
#in graph according to occurences in address 
import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def get_summary_graph(filename,sources_dir):
    pd.set_option("display.max_rows",1000)
    file_path=sources_dir+"/"+filename
    raw_df = pd.read_csv(file_path,delimiter="\s+",header = None)
    raw_df = raw_df.iloc[:,[0,4]]
    raw_df.columns = ["address","op"]
    raw_df.address = raw_df.address.astype(str)
    raw_df = raw_df.sort_values("address")
    #raw_df.to_csv("raw.csv") 

    counts_df = raw_df.groupby(raw_df.columns.tolist()).size().unstack()
    counts_df["total"] = counts_df.sum(axis=1)
    counts_df = counts_df.sort_values("address")
    counts_df.columns.name = None
    counts_df.index = counts_df.index+"_"
    #counts_df.to_csv("counts.csv") 
    counts_df.index = counts_df.index.str.slice(0,-1)

    plt.close("all")
    """
    #present # of faults per type
    f,ax = plt.subplots(figsize=(16,12))
    raw_df.groupby("op").size().plot.bar(ax=ax)
    ax.title("counts")
    ax.grid()
    plt.title(filename)
    plt.savefig(file_path+"_total.png")
    plt.close("all")
    """
    f,ax = plt.subplots(figsize= (16,12))
    counts_df.iloc[:50,:-1].plot.bar(ax=ax,stacked=False)
    plt.title(filename)
    plt.savefig(file_path+"_leading_50.png")
    plt.close("all")
    
    f,ax = plt.subplots(figsize= (16,12))
    counts_df.iloc[:,:-1].plot.bar(ax=ax,stacked=False)
    plt.title(filename)
    plt.savefig(file_path+"_all.png")
    plt.close("all")


    plt.close("all")
    add_counts = raw_df.address.value_counts()
    add_gb = raw_df.groupby("address")
    plt.close("all")
    """
    f,ax = plt.subplots(figsize= (16,12))
    counts_df.iloc[:25,:-1].plot.bar(ax=ax,stacked=True)
    plt.title(filename)
    plt.savefig(file_path+"_hist.png")

    plt.close("all")
    f,ax = plt.subplots(figsize=(16,12))
    percents_df = counts_df.div(counts_df.total,axis=0)*100
    percents_df[percents_df.isnull()]=0
    percents_df.iloc[:,:-1].plot(ax=ax)
    ax.set_ylabel("percents(%)")
    ax.grid()
    plt.title(filename)
    plt.savefig(file_path+"_percents.png")
    """

    f,ax = plt.subplots(figsize=(16,12))
    percents_df = counts_df.copy()
    percents_df[percents_df.isnull()]=0
    percents_df.iloc[:,:-1].plot(ax=ax)
    ax.set_ylabel("# count")
    ax.grid()
    plt.title(filename)
    plt.savefig(file_path+"_counts.png")

    #cleaning step
    #os.remove("raw.csv")
    #os.remove("counts.csv")

sources_dir="reports"
for f in sorted(os.listdir(sources_dir)):
    if f.endswith("tmp_summary"):
        print(f)
        get_summary_graph(f,sources_dir)
