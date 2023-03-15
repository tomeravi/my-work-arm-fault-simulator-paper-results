import pandas as pd
import os

target_base_file="0_naked_armv7-m_O1"

def get_most_vulnerable_addresses():
    input_file="reports/"+target_base_file+".rpt_tmp_summary"
    pd.set_option("display.max_rows",1000)
    raw_df = pd.read_csv(input_file,delimiter="\s+",header = None)
    raw_df = raw_df.iloc[:,[0,4]]
    raw_df.columns = ["address","op"]
    raw_df.address = raw_df.address.astype(str)
    raw_df = raw_df.sort_values("address")
    #raw_df.to_csv("raw.csv") 

    counts_df = raw_df.groupby(raw_df.columns.tolist()).size().unstack()
    counts_df["total"] = counts_df.sum(axis=1)
    counts_df = counts_df.sort_values("address")
    counts_df.columns.name = None
    #counts_df.index = counts_df.index+"_"
    #counts_df.to_csv("counts.csv") 
    #counts_df.index = counts_df.index.str.slice(0,-1)
    #get the list of addresses of the highest number of Skip failures
    lis = counts_df.sort_values("Skip",ascending=False)["Skip"].index.tolist()
    print("####>>>>")
    print(counts_df.sort_values("Skip",ascending=False))
    return lis


####
# sync between .s and his corresponding disassembled , in order to find the address of each command
# then we can use this sync to add IgnoreStart/End labels 
####
with open('files/'+target_base_file+'.s') as file_1:
    file_s_lines = file_1.readlines()

with open('files/'+target_base_file+'_disassembled.txt') as file_2:
    file_disasm_lines = file_2.readlines()

s_lines = list()
for line in file_s_lines:
    line = line.replace("\t"," ").strip()
    #print(line)
    s_lines.append(line)

#search for first command in .s file
i = 0
while i < len(s_lines):
    line = s_lines[i]

    if not line or line[0] == "." or line[-1] == ":" or line[0] == "@":
        i += 1
        continue
    else:    
        break
first_command=line
print("First command is: "+first_command)

#search first command in disassembly txt file
address_list = list()
command_list = list()
found = False
for line in file_disasm_lines:
    line = line.replace("\t"," ").strip()
    if not found and line.strip().find(first_command.strip()) != -1:
        print("first command found in disassm file: "+line)
        found = True
        #break
    if line and line[4] == ":":
        x=line.split(":")
        #print(x[0])

        #special care for line with ".word"
        #.word must appear in address align to 4 ,if that not the case - the compiler add a nop
        #in .s file it MAY add a nop by add line of .align 2 ,b/c it not sure where will be the final address
        #so when .word appear need to check if nop add before
        if line.find(".word") != -1:
            #print(line)
            lastadd=address_list[-1]
            nn=int(lastadd,16)
            #print("last "+lastadd+" is "+str(nn)+" which is "+str(nn%4))
            if nn%4 != 0 and command_list[-1].find("nop") != -1:
                print("remove from command list the prev (nop?) command: "+command_list[-1])
                address_list.pop()
                command_list.pop()
        address_list.append(x[0])
        command_list.append(x[1])

    #print(line)

#index of the input address is the location, e.g. #5 means the fifth command
high_failures_list = get_most_vulnerable_addresses()
print(high_failures_list[:10])
high_failures_list_indexes = list()
#choose how many address with the highest faulire you take from high_failures_list
for failure_address in high_failures_list[:20]:
    try:
        ix = address_list.index(failure_address)
    except:
        ix = -1
    if ix != -1:
        print("in index: "+str(ix)+" address: "+address_list[ix] +" --> command: "+command_list[ix])
        high_failures_list_indexes.append(ix)
    else:
        print(failure_address +" not found :-(")


#look for the i command in s lines
i = 0
command_index=0
print("look for commands in: ")
print(high_failures_list_indexes)
new_s_lines = list()
#add label of "start" in the begining

new_s_lines.append("@IgnoreStart")
while i < len(s_lines):
    line = s_lines[i]
    #if line[0:8] == ".align 2":
    #    print(line)
    if (not line or line[0] == "." or line[-1] == ":" or line[0] == "@") and line[0:5] != ".word" :
        i += 1
        new_s_lines.append(line)
        continue
    elif command_index in high_failures_list_indexes:
        print("found_command  at index:"+str(command_index)+" is: "+line)
        new_s_lines.append("@IgnoreEnd")
        new_s_lines.append(line)
        new_s_lines.append("@IgnoreStart")
        command_index += 1
        i += 1
        continue
    else:
        #print(str(command_index)+" : "+line)
        new_s_lines.append(line)
        command_index += 1
        i += 1
new_s_lines.append("@IgnoreEnd")

if i == len(s_lines):
    print("index not found !")
#else:
#    found_command=line
#    print("found_command  is: "+found_command)

#print(new_s_lines)
new_s_filename="files/"+target_base_file+"_minimal_replacment.s"
new_s_filename_tmp=new_s_filename+".tmp"

with open(new_s_filename_tmp, "wt") as file:
    for line in new_s_lines:
        if line and line[-1] != ":":
            file.write("    ")

        file.write(line+"\n")

os.system("python3 ../protect_with_replacement.py "+new_s_filename_tmp+" r5 "+new_s_filename)