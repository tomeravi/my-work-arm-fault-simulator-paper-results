SECTIONS
{
. = 0x0;
.text : {
startup.o(.text)
aes.o(.text)
printf.o(.text)
main.o(.text)
}
. = 0x20000000;
.data : { *(.data) }
.bss : { *(.bss) }
. = ALIGN(8);
. = . + 0x1000;
stack_top = .;
}