#!/bin/sh

set -e
#https://www.ti.com/lit/ds/symlink/lm3s811.pdf
#sources: https://balau82.wordpress.com/2010/02/28/hello-world-for-bare-metal-arm-using-qemu/
rm -rf *.o *.bin *.elf


arm-none-eabi-as -c -mthumb -mlittle-endian -march=armv7-m -mcpu=cortex-m3 startup.s -o startup.o
arm-none-eabi-gcc -c -mthumb -ffreestanding -mlittle-endian -march=armv7-m -mcpu=cortex-m3 main.c -o main.o
arm-none-eabi-gcc -c -mthumb -ffreestanding -mlittle-endian -march=armv7-m -mcpu=cortex-m3 printf.c -o printf.o

#arm-none-eabi-gcc -c -mthumb -ffreestanding -mlittle-endian -march=armv7-m -mcpu=cortex-m3 aes.c -o aes.o
arm-none-eabi-as -c -mthumb -mlittle-endian -march=armv7-m -mcpu=cortex-m3 aes.s -o aes.o

arm-none-eabi-ld -T test.ld aes.o printf.o main.o startup.o /usr/lib/gcc/arm-none-eabi/9.2.1/thumb/v7/nofp/libgcc.a -o test.elf

qemu-system-arm -M lm3s811evb -m 128M  -kernel test.elf -nographic

#sample to build aes assembly file
#arm-none-eabi-gcc -Wall -Wpedantic -std=c11 -ffreestanding -nostdlib -mthumb -march=armv7-m -O1 -ffixed-r5 -S aes.c -o aes.s
