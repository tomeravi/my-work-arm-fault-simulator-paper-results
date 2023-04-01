#!/bin/sh

set -e
#https://www.ti.com/lit/ds/symlink/lm3s811.pdf

rm -rf *.o *.bin *.elf


arm-none-eabi-as -c -mthumb -mlittle-endian -march=armv7-m -mcpu=cortex-m3 startup.s -o startup.o
arm-none-eabi-gcc -c -mthumb -ffreestanding -mlittle-endian -march=armv7-m -mcpu=cortex-m3 main.c -o main.o
arm-none-eabi-gcc -c -mthumb -ffreestanding -mlittle-endian -march=armv7-m -mcpu=cortex-m3 printf.c -o printf.o

#arm-none-eabi-gcc -c -mthumb -ffreestanding -mlittle-endian -march=armv7-m -mcpu=cortex-m3 aes.c -o aes.o
arm-none-eabi-as -c -mthumb -mlittle-endian -march=armv7-m -mcpu=cortex-m3 0_naked_armv7-m_O1.s -o aes.o

arm-none-eabi-ld -T test.ld aes.o printf.o main.o startup.o /usr/lib/gcc/arm-none-eabi/9.2.1/thumb/v7/nofp/libgcc.a -o test.elf

qemu-system-arm -M lm3s811evb -kernel test.elf -nographic

#
##CPU="arm926ej-s" cortex-m33
#CPU="cortex-m3  -mthumb" 
#OPTS="-Wall -Wpedantic -std=c11 -ffreestanding -nostdlib -mthumb"
#
#arm-none-eabi-as -mcpu=$CPU -g startup.s -o startup.o
#arm-none-eabi-gcc -c -mcpu=$CPU -g main.c --specs=nosys.specs -o main.o
#
##arm-none-eabi-gcc -c -mcpu=$CPU -g aes.c -o aes.o
#
##arm-none-eabi-gcc -c -mcpu=$CPU -S aes.c -o aes.s
##arm-none-eabi-gcc -c -mcpu=$CPU -g aes.s -o aes.o
#
##arm-none-eabi-as -mcpu=$CPU -g 0_naked_armv7-m_O1.s -o aes1.o
#
##arm-none-eabi-gcc -c -mcpu=$CPU -g printf.c -o printf.o
##/usr/lib/gcc/arm-none-eabi/9.2.1/libgcc.a - for non thumb
#arm-none-eabi-ld -T test.ld  main.o startup.o /usr/lib/gcc/arm-none-eabi/9.2.1/thumb/v7/nofp/libgcc.a  -o main.elf
#arm-none-eabi-objcopy -O binary main.elf main.bin
#
##To run my program in the emulator, the command is:
#qemu-system-arm -M lm3s6965evb -cpu cortex-m3 -m 256M -nographic -kernel main.bin 
##qemu-system-arm -M versatilepb -m 128M -nographic -kernel main.bin
###The -M option specifies the emulated system. The program prints �Hello world!� in the terminal and runs indefinitely; to exit QEMU, press �Ctrl + a� and then �x�.