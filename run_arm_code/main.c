#include <stdio.h>
#include <time.h>

volatile unsigned int *const UART0DR = (unsigned int *)0x101f1000;
typedef unsigned char u8;

void print_uart0(const char *s) {
  while (*s != '\0') {             /* Loop until end of string */
    *UART0DR = (unsigned int)(*s); /* Transmit char */
    s++;                           /* Next char */
  }
}

void print_hex_uart0(u8 *s, int len) {
  char str[4];
  while (len > 0) { /* Loop until end of string */
    // sprintf(str, "%X", *s);
    *UART0DR = (unsigned int)(*str);       /* Transmit char */
    *UART0DR = (unsigned int)(*(str + 1)); /* Transmit char */
    len--;                                 /* Next char */
  }
}

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

void AES_ECB_encrypt(const u8 master_key[16], u8 buf[16]);
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

__int64_t get_ticks() {
  unsigned int pmccntr = 0;
  unsigned int pmuseren = 0;
  unsigned int pmcntenset = 0;
  // Read the user mode perf monitor counter access permissions.
  asm volatile("mrc p15, 0, %0, c9, c14, 0" : "=r"(pmuseren));
  if (pmuseren & 1) {  // Allows reading perfmon counters for user mode code.
    asm volatile("mrc p15, 0, %0, c9, c12, 1" : "=r"(pmcntenset));
    if (pmcntenset & 0x80000000ul) {  // Is it counting?
      asm volatile("mrc p15, 0, %0, c9, c13, 0" : "=r"(pmccntr));
      //  The counter is set up to count every 64th cycle
      return (__int64_t)(pmccntr)*64;  // Should optimize to << 6
    }
    return -22;
  }
  return -11;
}
#include <sys/time.h>
void c_entry() {
  char buf[16];
  static int rawtime = 0;
  struct timeval tv;

  // print_uart0("Hello world!\n");
  print_uart0("encrypt...\n");
  // print_hex_uart0(plaintext, 16);
  AES_ECB_encrypt(key, plaintext);
  // print_hex_uart0(plaintext, 16);
#if defined(__ARM_ARCH)

#if (__ARM_ARCH >= 6)
  ggg
#endif
#endif
      rawtime = gettimeofday(&tv, NULL);  // get_ticks();
  sprintf(buf, "%d\n", __ARM_ARCH);
  print_uart0((const char *)buf);

  if (mymemcmp(ciphertext, plaintext, 16) == 0) {
    print_uart0("equal\n");
  } else {
    print_uart0("Not equal\n");
  }
  // exit(0);
}
