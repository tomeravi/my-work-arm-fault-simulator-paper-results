
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
#p = Path(r".")
pd.set_option("display.max_rows",1000)
raw_df = pd.read_csv(r"SummaryTransientInstructionInNakedReport.txt",delimiter="\s+",header = None)
raw_df = raw_df.iloc[:,[0,4]]
raw_df.columns = ["address","op"]
raw_df.address = raw_df.address.astype(str)
raw_df = raw_df.sort_values("address")
raw_df.to_csv("raw.csv") 

counts_df = raw_df.groupby(raw_df.columns.tolist()).size().unstack()
counts_df["total"] = counts_df.sum(axis=1)
counts_df = counts_df.sort_values("address")
counts_df.columns.name = None
counts_df.index = counts_df.index+"_"
counts_df.to_csv("counts.csv") 
counts_df.index = counts_df.index.str.slice(0,-1)


plt.close("all")
f,ax = plt.subplots(figsize=(16,12))
raw_df.groupby("op").size().plot.bar(ax=ax)
ax.set_title("counts")
ax.grid()
plt.savefig("total.png")
plt.close("all")

f,ax = plt.subplots(figsize= (16,12))
counts_df.iloc[:25,:-1].plot.bar(ax=ax,stacked=False)
plt.savefig("leading_25.png")
plt.close("all")

f,ax = plt.subplots(figsize= (16,12))
counts_df.iloc[:,:-1].plot.bar(ax=ax,stacked=False)
plt.savefig("all.png")
plt.close("all")


plt.close("all")
add_counts = raw_df.address.value_counts()
add_gb = raw_df.groupby("address")
plt.close("all")



f,ax = plt.subplots(figsize= (16,12))
counts_df.iloc[:25,:-1].plot.bar(ax=ax,stacked=True)
plt.savefig(r"hist.png")


plt.close("all")
f,ax = plt.subplots(figsize=(16,12))
percents_df = counts_df.div(counts_df.total,axis=0)*100
percents_df[percents_df.isnull()]=0
percents_df.iloc[:,:-1].plot(ax=ax)
ax.set_ylabel("percents(%)")
ax.grid()
plt.savefig("percents.png")


f,ax = plt.subplots(figsize=(16,12))
percents_df = counts_df.copy()
percents_df[percents_df.isnull()]=0
percents_df.iloc[:,:-1].plot(ax=ax)
ax.set_ylabel("# count")
ax.grid()
plt.savefig("counts.png")