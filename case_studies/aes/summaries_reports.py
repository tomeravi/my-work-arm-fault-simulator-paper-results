#go over all reports/*rpt 
#print summary of faults per type 
#and create a raw temp summary report for other python post processing
import os
import sys
from collections import Counter
from pathlib import Path

a =["Permanent", "Transient"]
b =["Instruction" ]
c =["Skip", "Byte-Set","Bit-Flip","Byte-Clear"]
#build all fault type
fault_types = []
for a1 in a:
    for b1 in b:
        for c1 in c:
            fault = a1+" "+b1+" "+c1
            fault_types.append(fault)
print(fault_types)

for p in Path('reports').glob('*.rpt'):
    print(f"#########\n{p.name}\n")
    text = p.read_text()
    sum_faults = 0
    for fault in fault_types:
        num = text.count(fault)
        sum_faults += num
        print("Number of "+fault+" : "+str(num)) 
    print("all faults : "+str(sum_faults))
    #create the summary report by this line
    #grep "|" 0_naked_armv7-m_O1.rpt |grep " Instruction "  | awk -F'[:|]' '{printf $1 " : " $3 "\n"}' |sort > summary_report.txt
    os.system("grep \"|\" reports/"+p.name+" |grep \" Instruction \"  | awk -F'[:|]' '{printf $1 \" : \" $3 \"\\n\"}' |sort > reports/"+p.name+"_tmp_summary")
