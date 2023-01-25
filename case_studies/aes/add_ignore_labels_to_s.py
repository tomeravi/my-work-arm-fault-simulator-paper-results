

with open('files/0_naked_armv7-m_O1.s') as file_1:
    file_1_text = file_1.readlines()

with open('files/0_naked_armv7-m_O1_disassembled.txt') as file_2:
    file_2_text = file_2.readlines()

lines = list()
for line in file_1_text:
    line = line.replace("\t"," ").strip()
    #print(line)
    lines.append(line)

i = 0
while i < len(lines):
    line = lines[i]

    if not line or line[0] == "." or line[-1] == ":" or line[0] == "@":
        i += 1
        continue
    break
first_command=line
print("First command is: "+first_command)

#search first command in disassembly txt file
address = list()
for line in file_2_text:
    line = line.replace("\t"," ").strip()
    if line.strip().find(first_command.strip()) != -1:
        print(line)
        #break
    if line and line[4] == ":":
        x=line.split(":")
        print(x[0])
        address.append(x[0])

    #print(line)

