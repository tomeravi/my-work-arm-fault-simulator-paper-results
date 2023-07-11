#create the summary report by this line
#grep "Transient Instruction" 0_naked_armv7-m_O1.rpt | awk -F'[:|]' '{printf $1 " : " $3 "\n"}' |sort > summary_report.txt

import sys
from collections import Counter

lines_list = []
with open(sys.argv[1]) as file:
    for line in file:
        line = line.rstrip("\n").replace(" ","") #remove new line and all spaces
        line_parts = line.split(':')
        lines_list.append(line_parts)
#my_dict = {i:lines.count(i) for i in lines}
#print(lines_list)
uniq_items= sorted(set(map(tuple, lines_list)), reverse=True)

print(uniq_items)
#result_counter = Counter(x[0] for x in lines_list)
#print(result_counter)
print(type(uniq_items[0]))
uniq_items_counter = [0]*len(uniq_items) #create list of 0 as counter  of uniq list
for item in lines_list:
    #print(tuple(item))
    ix = uniq_items.index(tuple(item))
    #print(ix)
    uniq_items_counter[ix] +=1

print(uniq_items_counter)
#add counter to each item in uniq_items
merged_list = []
for counter,item in zip(uniq_items_counter,uniq_items):
    temp=item+(str(counter),)
    merged_list.append(temp)
print(merged_list)

        

