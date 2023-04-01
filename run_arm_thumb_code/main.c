#include <stdio.h>
#include <time.h>
#include <sys/time.h>
#include "printf.h"

typedef unsigned char u8; 

u8 plaintext1[16] = {
    0x67, 0x45, 0x8b, 0x6b, 0x69, 0x98, 0x3c, 0x64,
    0x51, 0xdc, 0xb0, 0x74, 0x4a, 0x94, 0xe8, 0x2a,
};
u8 plaintext[16] = {
    0x67, 0x45, 0x8b, 0x6b, 0x69, 0x98, 0x3c, 0x64,
    0x51, 0xdc, 0xb0, 0x74, 0x4a, 0x94, 0xe8, 0x2a,
};
u8 key[16] = {
    0xc6, 0x23, 0x7b, 0x32, 0x73, 0x48, 0x33, 0x66,
    0xff, 0x5c, 0x49, 0x19, 0xec, 0x58, 0x55, 0x62,
};
u8 ciphertext[16] = {
    0x46, 0x38, 0x83, 0x97, 0xe4, 0xe4, 0xd5, 0x03,
    0x64, 0xaf, 0x54, 0x4f, 0x08, 0x02, 0x92, 0x2c,
};

volatile unsigned int *const UART0DR = (unsigned int *)0x4000c000;
volatile unsigned int *const RTCADDR = (unsigned int *)0x101E8000;

void AES_ECB_encrypt(const u8 master_key[16], u8 buf[16]);

int mymemcpy(u8 *dest, u8 *src, int len);

void print_uart0(const char *s) {
  while (*s != '\0') {             /* Loop until end of string */
    *UART0DR = (unsigned int)(*s); /* Transmit char */
    s++;                           /* Next char */
  }
}

void print_time() {
  unsigned int t = *RTCADDR;
  printf("time: %d",t);
}

int mymemcpy(u8 *dest, u8 *src, int len) {
  int i;
  for (i = 0; i < len; i++) {
    dest[i] = src[i];
  }
  return 0;
}

int mymemcmp(u8 *a, u8 *b, int len) {
  int i;
  for (i = 0; i < len; i++) {
    if (a[i] != b[i]) break;
  }
  if (i == len)
    return 0;
  else
    return 1;
}

void c_entry() {
  char buf[16];
  int i,len = 1;
  unsigned int t1,t2;

  print_uart0("encrypt...\n");
  //start time
  t1 = *RTCADDR;   
  //key[0] = 0x0;
  print_uart0("1\n");
  for (i = 0; i < len; i++) {
    print_uart0("2\n");
    AES_ECB_encrypt(key, plaintext);
  }
  print_uart0("3\n");
  //end time
  t2 = *RTCADDR;
  printf("time: %d-%d = %d\n",t2,t1,t2-t1); 
   
  if (mymemcmp(ciphertext, plaintext, 16) == 0) {
    print_uart0("equal\n");
  } else {
    print_uart0("not equal\n");
  }
  while(1);
}
