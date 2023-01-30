####
# sync between .s and his corresponding disassembled , in order to find the address of each command
# then we can use this sync to add IgnoreStart/End labels 
####
with open('files/0_naked_armv7-m_O1.s') as file_1:
    file_s_lines = file_1.readlines()

with open('files/0_naked_armv7-m_O1_disassembled.txt') as file_2:
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
        #in .s file it MAY add a nop by add line of .align 2 ,b/c it not sure where will be the final addres
        #so when .word appear need to check if nop add before
        if line.find(".word") != -1:
            #print(line)
            lastadd=address_list[-1]
            nn=int(lastadd,16)
            #print("last "+lastadd+" is "+str(nn)+" which is "+str(nn%4))
            if nn%4 != 0:
                print("remove from command list the prev (nop?) command: "+command_list[-1])
                address_list.pop()
                command_list.pop()
        address_list.append(x[0])
        command_list.append(x[1])

    #print(line)

#index of the input address is the location, e.g. #5 means the fifth command
input_address="823a"
try:
    ix = address_list.index(input_address)
except:
    ix = -1
if ix != -1:
    print("in index: "+str(ix)+" address: "+address_list[ix] +" --> command: "+command_list[ix])
else:
    print(input_address +" not found :-(")

#look for the i command in s lines
i = 0
command_index=0
print("look for command #"+str(ix))
new_s_lines = list()
new_s_lines.append("@IgnoreStart")
while i < len(s_lines):
    line = s_lines[i]
    #if line[0:8] == ".align 2":
    #    print(line)
    if (not line or line[0] == "." or line[-1] == ":" or line[0] == "@") and line[0:5] != ".word" :
        i += 1
        new_s_lines.append(line)
        continue
    elif command_index == ix:
        #print("found")
        new_s_lines.append("@IgnoreEnd")
        new_s_lines.append(line)
        new_s_lines.append("@IgnoreStart")
        break
    else:
        #print(str(command_index)+" : "+line)
        new_s_lines.append(line)
        command_index += 1
        i += 1
new_s_lines.append("@IgnoreEnd")

if i == len(s_lines):
    print("index not found !")
else:
    found_command=line
    print("found_command  is: "+found_command)

#print(new_s_lines)
new_s_filename="temp.s"
with open(new_s_filename, "wt") as file:
    for line in new_s_lines:
        if line and line[-1] != ":":
            file.write("    ")

        file.write(line+"\n")
