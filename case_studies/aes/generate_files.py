#!/usr/bin/python3

OPTIMIZATIONS = ["O1"] #, "O2", "O3", "Os"]
ARCHS = ["armv7-m"]
OPTS = "-Wall -Wpedantic -std=c11 -ffreestanding -nostdlib -mthumb"

################################################################
############## DO NOT CHANGE ANYTHING BELOW ####################
################################################################

from subprocess import Popen, PIPE
import os
import sys

def run(cmd):
    p = Popen(cmd.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    output = output.decode('UTF-8')
    err = err.decode('UTF-8')
    if p.returncode != 0:
        print(output)
        print(err)
        sys.exit(1)
    return output, err


os.makedirs("files", exist_ok=True)
for a in ARCHS:
    for o in OPTIMIZATIONS:
        if not all(x in " "+a+" "+o for x in sys.argv[1:]): continue
        print("Processing:",a,o)
        opts = OPTS+ " -"+o+" -march="+a

        unprotected_name = "files/0_naked_"+a+"_"+o+".s"
        replacement_name = "files/1_replacement_"+a+"_"+o+".s"
        control_flow_name = "files/2_control_flow_"+a+"_"+o+".s"
        combined_name = "files/3_combined_"+a+"_"+o+".s"

        #print("arm-none-eabi-gcc "+opts+" -ffixed-r5 -S aes.c -o " + unprotected_name)
        os.system("arm-none-eabi-gcc "+opts+" -ffixed-r5 -S aes.c -o " + unprotected_name)
        #copy this file for later refference 
        #os.system("cp "+unprotected_name +" " + unprotected_name+"_special_build_for_replacement")
        os.system("python3 ../protect_with_replacement.py "+unprotected_name+" r5 "+replacement_name)
        #now generate replacment from pre-build file
        #temp_unprotected_name="files/0_naked_armv7-m_O1.s_build_for_replacement"
        #temp_replacement_name="files/1_replacement_armv7-m_O1_with_ignore_areas.s"
        #os.system("python3 ../protect_with_replacement.py "+temp_unprotected_name+" r5 "+temp_replacement_name)

#        os.system("arm-none-eabi-gcc "+opts+" -ffixed-r5 -ffixed-r6 -ffixed-r7 -S aes.c -o " + unprotected_name)
#        os.system("python3 ../protect_control_flow.py "+unprotected_name+" r5 r6 r7 "+control_flow_name)

#        os.system("arm-none-eabi-gcc "+opts+" -ffixed-r5 -ffixed-r6 -ffixed-r7 -S aes.c -o " + unprotected_name)
#        os.system("python3 ../protect_control_flow.py "+unprotected_name+" r5 r6 r7 "+combined_name)
#        os.system("python3 ../protect_with_replacement.py "+combined_name+" r5 "+combined_name)

        os.system("arm-none-eabi-gcc "+opts+" -ffixed-r5 -S aes.c -o " + unprotected_name)

