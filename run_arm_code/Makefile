ARMGNU ?= arm-none-eabi
LIBSPEC=-L /usr/lib/arm-none-eabi/newlib
COPS = -Wall -nostartfiles -ffreestanding  -specs=nano.specs  -specs=nosys.specs -march=armv7-m
#COPS = -Wall -nostartfiles -Wpedantic -std=c11 -ffreestanding  -specs=nosys.specs
all : clean main.hex main.bin main.elf

clean :
	rm -f *.o
	rm -f *.bin
	rm -f *.hex
	rm -f *.elf

startup.o : startup.s
	$(ARMGNU)-gcc -c startup.s

main.o : main.c
	$(ARMGNU)-gcc $(COPS) -c main.c -o main.o

aes.o : aes.c
	$(ARMGNU)-gcc $(COPS) -c aes.c -o aes.o

#link using gcc and not ld see https://stackoverflow.com/questions/65161159/errors-compiling-sqrt-function-for-raspberrypi2-and-beableboneblack-with-arm-non
main.elf : test.ld startup.o main.o aes.o
	$(ARMGNU)-gcc  $(COPS)  $(LIBSPEC) -lc startup.o main.o aes.o -T test.ld  -o main.elf 

main.bin : main.elf
	$(ARMGNU)-objcopy main.elf -O binary main.bin

main.hex : main.elf
	$(ARMGNU)-objcopy main.elf -O ihex main.hex