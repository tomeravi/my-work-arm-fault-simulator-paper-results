#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdatomic.h>
#include "cmsis/ARMCM3.h"

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

typedef struct {
    uint8_t REG_8;
    uint16_t REG_16;
    uint32_t REG_32;
    union {
        uint32_t REG_32BITFIELD;
        struct {
            unsigned int field1:1;
            unsigned int field2:2;
            unsigned int field3:3;
            unsigned int field4:4;
            unsigned int :4;
            unsigned int field5:5;
            unsigned int field6:6;
            unsigned int field7:7;
        };
    };
    uint8_t gap[5];
    uint64_t REG_TEST_FIELD_BITNESS_AND_BITMASKS;
} __attribute__((packed)) FAKE_PERIPHERAL_TYPE;

FAKE_PERIPHERAL_TYPE *FAKE_PERIPHERAL = (FAKE_PERIPHERAL_TYPE *)0x20001800;
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wmissing-noreturn"

const uint64_t TEST64_BIT_VALUES[] = {
    -1LL/*MINUS_ONE*/,
    5LL/*5_OR_13_OR_21*/,
    6LL/*DEF_VALUE*/,
    13LL/*5_OR_13_OR_21*/,
    21LL/*5_OR_13_OR_21*/,
    0b100101LL/*DEF_VALUE*/,
    0LL/*Last must be zero*/,
};

static atomic_uint myTicks = 0;

void SysTick_Handler(void) {
  myTicks++;
  //printf("SysTick_Handler\n");
  //printf("...myTicks = %lu; SysTick->VAL = %lu\n", myTicks, SysTick->VAL);
}

void AES_ECB_encrypt(const u8 master_key[16], u8 buf[16]);

int main(void) {
    
  char buf[16];
  int sum_results,c,counter = 10;
  int i,len = 1000000;
  int copy_once =1;
  unsigned int start_time =0, stop_time=0,cycle_count =0;
  
    printf("Size of the peripheral struct %d\n", sizeof(*FAKE_PERIPHERAL));
    SystemInit();
    SysTick_Config(SystemCoreClock/1000);
    printf("init done\n");
 sum_results = 0;
 copy_once = 1;

 for(c=0;c<counter;c++)
 {
    
    start_time = myTicks;  
    //key[0] = 0x0; //uncomment in order to check that that encryption works !

    for (i = 0; i < len; i++) {
      //printf("line: %d\n",__LINE__);
      AES_ECB_encrypt(key, plaintext);
      //printf("line: %d\n",__LINE__);

      // #### please notice that adding printf will disrupt/spoil the results !!!!
      if(copy_once)
      {
        //printf("line: %d\n",__LINE__); 
        memcpy(plaintext1,plaintext,16);
        copy_once = 0;
      }
      //printf("line: %d\n",__LINE__);
    }

    stop_time = myTicks; 
    if (memcmp(ciphertext, plaintext1, 16) == 0) {
       printf("equal\n");
    } else {
       printf("not equal\n");
    }
    cycle_count = stop_time-start_time; // Calculates the time taken
    printf("time: %d-%d = %d\n",stop_time,start_time,cycle_count);
    sum_results += cycle_count;
    
   }
   printf("average of %d times: %d \n",counter,sum_results/counter);
/*
    FAKE_PERIPHERAL->REG_32BITFIELD = 0xABCDEF79;
    FAKE_PERIPHERAL->REG_8 = 0xCC;
    FAKE_PERIPHERAL->REG_16 = 0xBCBC;
    FAKE_PERIPHERAL->REG_32 = 0xAA55C396;
    FAKE_PERIPHERAL->field5 = 9;
    FAKE_PERIPHERAL->REG_TEST_FIELD_BITNESS_AND_BITMASKS = -1LL;
    for (int i = 0, idx64Val = 0; 1; ++i, ++idx64Val) {
        FAKE_PERIPHERAL->REG_TEST_FIELD_BITNESS_AND_BITMASKS = TEST64_BIT_VALUES[idx64Val];
        if(TEST64_BIT_VALUES[idx64Val]==0LL) {
            idx64Val = -1;
        }
        FAKE_PERIPHERAL->REG_16++;
        printf("Hello, World!!! %x\n", i);
        for (long  j = 0; j < 100000000L; j++) {
            __asm__("nop");
        }
    }
   */ 
}

#pragma clang diagnostic pop


// Redirect file handlers to UART0
// TI LM3S-specific address is used
// Nor readiness check, nor configuration - this stuff works fine under qemu

#define UART0_DR *((uint32_t *) 0x4000c000)

__attribute__((unused)) int _write(__attribute__((unused))int file, const char *data, int len) {
    for (int i = 0; i < len; i++) {
        UART0_DR = data[i];
    }
    return len;
}

