set -e
#https://jasonblog.github.io/note/arm_emulation/hello_world_for_bare_metal_arm_using_qemu.html

#clean
rm -rf *.o *.bin *.elf

CPU=arm926ej-s 
OPTS="-Wall -Wpedantic -std=c11 -ffreestanding -nostdlib -mthumb"

arm-none-eabi-as -mcpu=$CPU -g startup.s -o startup.o
arm-none-eabi-gcc -c -mcpu=$CPU -g main.c --specs=nosys.specs -o main.o
arm-none-eabi-gcc -c -mcpu=$CPU -g aes.c -o aes.o
arm-none-eabi-gcc -c -mcpu=$CPU -g printf.c -o printf.o

arm-none-eabi-ld -T test.ld printf.o aes.o main.o startup.o /usr/lib/gcc/arm-none-eabi/9.2.1/libgcc.a  -o main.elf
arm-none-eabi-objcopy -O binary main.elf main.bin

#To run my program in the emulator, the command is:
qemu-system-arm -M versatilepb -m 128M -nographic -kernel main.bin
##The -M option specifies the emulated system. The program prints �Hello world!� in the terminal and runs indefinitely; to exit QEMU, press �Ctrl + a� and then �x�.