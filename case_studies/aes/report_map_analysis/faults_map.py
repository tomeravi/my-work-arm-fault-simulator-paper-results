import csv
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

#fn = r"0_naked_armv7-m_O1.rpt.txt"
#fn = r'1_replacement_armv7-m_O1.rpt.txt'
#fn = r"faults_map_secureboot_case_studies.txt"
fn = r"faults_map_aes_case_studies.txt"
#fn="x-y-data.txt"
#read from file , set columns names and choose to select column number 0,1,2
df = pd.read_csv(fn, delimiter="-", header=None, names=['Address', 'Time', 'Fault_type'], usecols=[0, 1, 2])
# df = data.drop(data.columns[0], axis=1)  # drop column 0 which is nan ( because the line begin with space )
df['Address'] = df['Address'].apply(int, base=16)
df['Time'] = df['Time'].apply(int)

#print(df)
# plotly style
fig = px.scatter(df, x='Address', y='Time', title="Faults Map : "+ fn, color='Fault_type', hover_data=['Fault_type'])
#fig.update_xaxes(tickmode = 'array',
#                 tickvals = df['Address'],
#                 ticktext= '0x'+df['Address'])
fig.show()

#x,y = [], []
#with open('x-y-data.txt','r') as csvfile:
#    reader = csv.reader(csvfile,delimiter=' ')
#    for row in reader:
#        x.append(int(row[0],16))
#        y.append(int(row[1]))
#print ( x,y )

#paint points
# Draw point based on above x, y axis values.
#plt.scatter(x, y, s=10)
# Set chart title.
#plt.title("Faults Map ")
# Set x, y label text.
#plt.xlabel("Address")
#plt.ylabel("Time")
#plt.show()
