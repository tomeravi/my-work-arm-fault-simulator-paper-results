
#https://jasonblog.github.io/note/arm_emulation/hello_world_for_bare_metal_arm_using_qemu.html


arm-none-eabi-as -mcpu=arm926ej-s -g startup.s -o startup.o
arm-none-eabi-gcc -c -mcpu=arm926ej-s -g test.c --specs=nosys.specs -o test.o
arm-none-eabi-gcc -c -mcpu=arm926ej-s -g aes.c -o aes.o
arm-none-eabi-ld -T test.ld aes.o test.o startup.o /usr/lib/gcc/arm-none-eabi/9.2.1/libgcc.a -o test.elf
arm-none-eabi-objcopy -O binary test.elf test.bin

#To run my program in the emulator, the command is:

# qemu-system-arm -M versatilepb -m 128M -nographic -kernel test.bin
##The -M option specifies the emulated system. The program prints �Hello world!� in the terminal and runs indefinitely; to exit QEMU, press �Ctrl + a� and then �x�.