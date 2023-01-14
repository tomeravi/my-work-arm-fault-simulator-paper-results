    .arch armv7-m
    .eabi_attribute 20, 1
    .eabi_attribute 21, 1
    .eabi_attribute 23, 3
    .eabi_attribute 24, 1
    .eabi_attribute 25, 1
    .eabi_attribute 26, 1
    .eabi_attribute 30, 1
    .eabi_attribute 34, 1
    .eabi_attribute 18, 4
    .file "aes.c"
    .text
    .align 1
    .syntax unified
    .thumb
    .thumb_func
    .fpu softvfp
    .type key_expansion, %function
key_expansion:
    @ args = 0, pretend = 0, frame = 0
    @ frame_needed = 0, uses_anonymous_args = 0
    stmdb sp, {r4, r6, r7, lr} @ stmdb sp!, {r4, r6, r7, lr}
    stmdb sp, {r4, r6, r7, lr}
    sub r5, sp, #16
    sub r5, sp, #16
    mov sp, r5
    mov sp, r5
    mov r2, r0 @ mov r2, r0
    mov r2, r0
    add r4, r1, #16 @ add r4, r1, #16
    add r4, r1, #16
.L2:
    ldrb r3, [r1] @ ldrb r3, [r1]
    ldrb r3, [r1]
    strb r3, [r0] @ strb r3, [r0]
    strb r3, [r0]
    ldrb r3, [r1, #1] @ ldrb r3, [r1, #1]
    ldrb r3, [r1, #1]
    strb r3, [r0, #1] @ strb r3, [r0, #1]
    strb r3, [r0, #1]
    ldrb r3, [r1, #2] @ ldrb r3, [r1, #2]
    ldrb r3, [r1, #2]
    strb r3, [r0, #2] @ strb r3, [r0, #2]
    strb r3, [r0, #2]
    ldrb r3, [r1, #3] @ ldrb r3, [r1, #3]
    ldrb r3, [r1, #3]
    strb r3, [r0, #3] @ strb r3, [r0, #3]
    strb r3, [r0, #3]
    adds r5, r1, #4 @ adds r1, r1, #4
    adds r5, r1, #4
    mov r1, r5
    mov r1, r5
    adds r5, r0, #4 @ adds r0, r0, #4
    adds r5, r0, #4
    mov r0, r5
    mov r0, r5
    cmp r1, r4 @ cmp r1, r4
    cmp r1, r4
    bne .L2 @ bne .L2
    bne .L2
    movs r7, #4 @ movs r7, #4
    movs r7, #4
    ldr ip, .L9 @ ldr ip, .L9
    ldr ip, .L9
    b .L4 @ b .L4
    b .L4
.L3:
    ldrb lr, [r3] @ ldrb lr, [r3]
    ldrb lr, [r3]
    eor r5, r1, lr @ eor r1, r1, lr
    eor r5, r1, lr
    mov r1, r5
    mov r1, r5
    strb r1, [r3, #16] @ strb r1, [r3, #16]
    strb r1, [r3, #16]
    ldrb r1, [r3, #1] @ ldrb r1, [r3, #1]
    ldrb r1, [r3, #1]
    eors r5, r6, r1 @ eors r6, r6, r1
    eors r5, r6, r1
    mov r6, r5
    mov r6, r5
    strb r6, [r3, #17] @ strb r6, [r3, #17]
    strb r6, [r3, #17]
    ldrb r1, [r3, #2] @ ldrb r1, [r3, #2]
    ldrb r1, [r3, #2]
    eors r5, r4, r1 @ eors r4, r4, r1
    eors r5, r4, r1
    mov r4, r5
    mov r4, r5
    strb r4, [r3, #18] @ strb r4, [r3, #18]
    strb r4, [r3, #18]
    ldrb r1, [r3, #3] @ ldrb r1, [r3, #3]
    ldrb r1, [r3, #3]
    eors r5, r0, r1 @ eors r0, r0, r1
    eors r5, r0, r1
    mov r0, r5
    mov r0, r5
    strb r0, [r3, #19] @ strb r0, [r3, #19]
    strb r0, [r3, #19]
    adds r5, r7, #1 @ adds r7, r7, #1
    adds r5, r7, #1
    mov r7, r5
    mov r7, r5
    adds r5, r2, #4 @ adds r2, r2, #4
    adds r5, r2, #4
    mov r2, r5
    mov r2, r5
    cmp r7, #44 @ cmp r7, #44
    cmp r7, #44
    beq .L8 @ beq .L8
    beq .L8
.L4:
    mov r3, r2 @ mov r3, r2
    mov r3, r2
    ldrb r1, [r2, #12] @ ldrb r1, [r2, #12]
    ldrb r1, [r2, #12]
    ldrb r6, [r2, #13] @ ldrb r6, [r2, #13]
    ldrb r6, [r2, #13]
    ldrb r4, [r2, #14] @ ldrb r4, [r2, #14]
    ldrb r4, [r2, #14]
    ldrb r0, [r2, #15] @ ldrb r0, [r2, #15]
    ldrb r0, [r2, #15]
    tst r7, #3 @ tst r7, #3
    tst r7, #3
    bne .L3 @ bne .L3
    bne .L3
    ldrb lr, [ip, r6] @ ldrb lr, [ip, r6]
    ldrb lr, [ip, r6]
    ldrb r6, [ip, r4] @ ldrb r6, [ip, r4]
    ldrb r6, [ip, r4]
    ldrb r4, [ip, r0] @ ldrb r4, [ip, r0]
    ldrb r4, [ip, r0]
    ldrb r0, [ip, r1] @ ldrb r0, [ip, r1]
    ldrb r0, [ip, r1]
    add r1, ip, r7, lsr #2 @ add r1, ip, r7, lsr #2
    add r1, ip, r7, lsr #2
    ldrb r5, [r1, #256] @ ldrb r1, [r1, #256]
    ldrb r5, [r1, #256]
    mov r1, r5
    mov r1, r5
    eor r5, lr, r1 @ eor r1, lr, r1
    eor r5, lr, r1
    mov r1, r5
    mov r1, r5
    b .L3 @ b .L3
    b .L3
.L8:
    add r5, sp, #16 @ ldmia sp!, {r4, r6, r7, pc}
    add r5, sp, #16
    mov sp, r5
    mov sp, r5
    sub r5, sp, #16
    sub r5, sp, #16
    ldmia r5, {r4, r6, r7, pc}
    ldmia r5, {r4, r6, r7, pc}
.L10:
    .align 2
.L9:
    .word .LANCHOR0
    .size key_expansion, .-key_expansion
    .align 1
    .syntax unified
    .thumb
    .thumb_func
    .fpu softvfp
    .type add_round_key, %function
add_round_key:
    @ args = 0, pretend = 0, frame = 0
    @ frame_needed = 0, uses_anonymous_args = 0
    @ link register save eliminated.
    stmdb sp, {r4, r6, r7} @ stmdb sp!, {r4, r6, r7}
    stmdb sp, {r4, r6, r7}
    sub r5, sp, #12
    sub r5, sp, #12
    mov sp, r5
    mov sp, r5
    lsls r5, r0, #4 @ lsls r0, r0, #4
    lsls r5, r0, #4
    mov r0, r5
    mov r0, r5
    adds r6, r1, #4 @ adds r6, r1, #4
    adds r6, r1, #4
    add ip, r1, #20 @ add ip, r1, #20
    add ip, r1, #20
.L12:
    subs r3, r6, #4 @ subs r3, r6, #4
    subs r3, r6, #4
    adds r4, r2, r0 @ adds r4, r2, r0
    adds r4, r2, r0
.L13:
    ldrb r1, [r3] @ ldrb r1, [r3]
    ldrb r1, [r3]
    ldrb r7, [r4] @ ldrb r7, [r4], #1
    ldrb r7, [r4]
    add r5, r4, #1 @ add r4, r4, #1
    add r5, r4, #1
    mov r4, r5
    mov r4, r5
    eors r5, r1, r7 @ eors r1, r1, r7
    eors r5, r1, r7
    mov r1, r5
    mov r1, r5
    strb r1, [r3] @ strb r1, [r3], #1
    strb r1, [r3]
    add r5, r3, #1 @ add r3, r3, #1
    add r5, r3, #1
    mov r3, r5
    mov r3, r5
    cmp r3, r6 @ cmp r3, r6
    cmp r3, r6
    bne .L13 @ bne .L13
    bne .L13
    adds r5, r0, #4 @ adds r0, r0, #4
    adds r5, r0, #4
    mov r0, r5
    mov r0, r5
    adds r5, r6, #4 @ adds r6, r6, #4
    adds r5, r6, #4
    mov r6, r5
    mov r6, r5
    cmp r6, ip @ cmp r6, ip
    cmp r6, ip
    bne .L12 @ bne .L12
    bne .L12
    ldmia sp, {r4, r6, r7} @ ldmia sp!, {r4, r6, r7}
    ldmia sp, {r4, r6, r7}
    add r5, sp, #12
    add r5, sp, #12
    mov sp, r5
    mov sp, r5
    bx lr @ bx lr
    bx lr
    .size add_round_key, .-add_round_key
    .align 1
    .syntax unified
    .thumb
    .thumb_func
    .fpu softvfp
    .type cipher, %function
cipher:
    @ args = 0, pretend = 0, frame = 16
    @ frame_needed = 0, uses_anonymous_args = 0
    stmdb sp, {r4, r6, r7, r8, sb, sl, fp, lr} @ stmdb sp!, {r4, r6, r7, r8, sb, sl, fp, lr}
    stmdb sp, {r4, r6, r7, r8, sb, sl, fp, lr}
    sub r5, sp, #32
    sub r5, sp, #32
    mov sp, r5
    mov sp, r5
    sub r5, sp, #16 @ sub sp, sp, #16
    sub r5, sp, #16
    mov sp, r5
    mov sp, r5
    mov r4, r0 @ mov r4, r0
    mov r4, r0
    mov r2, r1 @ mov r2, r1
    mov r2, r1
    str r1, [sp, #8] @ str r1, [sp, #8]
    str r1, [sp, #8]
    mov r1, r0 @ mov r1, r0
    mov r1, r0
    movs r0, #0 @ movs r0, #0
    movs r0, #0
    adr lr, .L1000 @ bl add_round_key
    adr lr, .L1000
    orr lr, #1
    orr lr, #1
    b add_round_key
    b add_round_key
.L1000:
    movs r6, #1 @ movs r6, #1
    movs r6, #1
    adds r3, r4, #4 @ adds r3, r4, #4
    adds r3, r4, #4
    str r3, [sp, #4] @ str r3, [sp, #4]
    str r3, [sp, #4]
    b .L18 @ b .L18
    b .L18
.L32:
    ldr r2, [sp, #8] @ ldr r2, [sp, #8]
    ldr r2, [sp, #8]
    mov r1, r4 @ mov r1, r4
    mov r1, r4
    mov r0, r6 @ mov r0, r6
    mov r0, r6
    adr lr, .L1001 @ bl add_round_key
    adr lr, .L1001
    orr lr, #1
    orr lr, #1
    b add_round_key
    b add_round_key
.L1001:
    adds r5, r6, #1 @ adds r6, r6, #1
    adds r5, r6, #1
    mov r6, r5
    mov r6, r5
    uxtb r5, r6 @ uxtb r6, r6
    uxtb r5, r6
    mov r6, r5
    mov r6, r5
    cmp r6, #10 @ cmp r6, #10
    cmp r6, #10
    beq .L31 @ beq .L31
    beq .L31
.L18:
    str r4, [sp, #12] @ str r4, [sp, #12]
    str r4, [sp, #12]
    mov r2, r4 @ mov r2, r4
    mov r2, r4
.L23:
    movs r3, #0 @ movs r3, #0
    movs r3, #0
.L19:
    ldrb r1, [r2, r3, lsl #2] @ ldrb r1, [r2, r3, lsl #2]
    ldrb r1, [r2, r3, lsl #2]
    ldr r0, .L33 @ ldr r0, .L33
    ldr r0, .L33
    ldrb r5, [r0, r1] @ ldrb r1, [r0, r1]
    ldrb r5, [r0, r1]
    mov r1, r5
    mov r1, r5
    strb r1, [r2, r3, lsl #2] @ strb r1, [r2, r3, lsl #2]
    strb r1, [r2, r3, lsl #2]
    adds r5, r3, #1 @ adds r3, r3, #1
    adds r5, r3, #1
    mov r3, r5
    mov r3, r5
    cmp r3, #4 @ cmp r3, #4
    cmp r3, #4
    bne .L19 @ bne .L19
    bne .L19
    adds r5, r2, #1 @ adds r2, r2, #1
    adds r5, r2, #1
    mov r2, r5
    mov r2, r5
    ldr r3, [sp, #4] @ ldr r3, [sp, #4]
    ldr r3, [sp, #4]
    cmp r2, r3 @ cmp r2, r3
    cmp r2, r3
    bne .L23 @ bne .L23
    bne .L23
    ldrb r3, [r4, #1] @ ldrb r3, [r4, #1]
    ldrb r3, [r4, #1]
    ldrb r2, [r4, #5] @ ldrb r2, [r4, #5]
    ldrb r2, [r4, #5]
    strb r2, [r4, #1] @ strb r2, [r4, #1]
    strb r2, [r4, #1]
    ldrb r2, [r4, #9] @ ldrb r2, [r4, #9]
    ldrb r2, [r4, #9]
    strb r2, [r4, #5] @ strb r2, [r4, #5]
    strb r2, [r4, #5]
    ldrb r2, [r4, #13] @ ldrb r2, [r4, #13]
    ldrb r2, [r4, #13]
    strb r2, [r4, #9] @ strb r2, [r4, #9]
    strb r2, [r4, #9]
    strb r3, [r4, #13] @ strb r3, [r4, #13]
    strb r3, [r4, #13]
    ldrb r3, [r4, #2] @ ldrb r3, [r4, #2]
    ldrb r3, [r4, #2]
    ldrb r2, [r4, #10] @ ldrb r2, [r4, #10]
    ldrb r2, [r4, #10]
    strb r2, [r4, #2] @ strb r2, [r4, #2]
    strb r2, [r4, #2]
    strb r3, [r4, #10] @ strb r3, [r4, #10]
    strb r3, [r4, #10]
    ldrb r3, [r4, #6] @ ldrb r3, [r4, #6]
    ldrb r3, [r4, #6]
    ldrb r2, [r4, #14] @ ldrb r2, [r4, #14]
    ldrb r2, [r4, #14]
    strb r2, [r4, #6] @ strb r2, [r4, #6]
    strb r2, [r4, #6]
    strb r3, [r4, #14] @ strb r3, [r4, #14]
    strb r3, [r4, #14]
    ldrb r3, [r4, #3] @ ldrb r3, [r4, #3]
    ldrb r3, [r4, #3]
    ldrb r2, [r4, #15] @ ldrb r2, [r4, #15]
    ldrb r2, [r4, #15]
    strb r2, [r4, #3] @ strb r2, [r4, #3]
    strb r2, [r4, #3]
    ldrb r2, [r4, #11] @ ldrb r2, [r4, #11]
    ldrb r2, [r4, #11]
    strb r2, [r4, #15] @ strb r2, [r4, #15]
    strb r2, [r4, #15]
    ldrb r2, [r4, #7] @ ldrb r2, [r4, #7]
    ldrb r2, [r4, #7]
    strb r2, [r4, #11] @ strb r2, [r4, #11]
    strb r2, [r4, #11]
    strb r3, [r4, #7] @ strb r3, [r4, #7]
    strb r3, [r4, #7]
    add sl, r4, #16 @ add sl, r4, #16
    add sl, r4, #16
    mov r2, r4 @ mov r2, r4
    mov r2, r4
.L21:
    ldrb r3, [r2] @ ldrb r3, [r2]
    ldrb r3, [r2]
    ldrb r1, [r2, #1] @ ldrb r1, [r2, #1]
    ldrb r1, [r2, #1]
    eor sb, r3, r1 @ eor sb, r3, r1
    eor sb, r3, r1
    ldrb lr, [r2, #2] @ ldrb lr, [r2, #2]
    ldrb lr, [r2, #2]
    ldrb r0, [r2, #3] @ ldrb r0, [r2, #3]
    ldrb r0, [r2, #3]
    eor r8, lr, r0 @ eor r8, lr, r0
    eor r8, lr, r0
    eor r7, sb, r8 @ eor r7, sb, r8
    eor r7, sb, r8
    lsr ip, sb, #7 @ lsr ip, sb, #7
    lsr ip, sb, #7
    lsl fp, ip, #1 @ lsl fp, ip, #1
    lsl fp, ip, #1
    add r5, ip, fp @ add ip, ip, fp
    add r5, ip, fp
    mov ip, r5
    mov ip, r5
    add r5, ip, ip, lsl #3 @ add ip, ip, ip, lsl #3
    add r5, ip, ip, lsl #3
    mov ip, r5
    mov ip, r5
    eor r5, ip, sb, lsl #1 @ eor ip, ip, sb, lsl #1
    eor r5, ip, sb, lsl #1
    mov ip, r5
    mov ip, r5
    eor sb, r3, r7 @ eor sb, r3, r7
    eor sb, r3, r7
    eor r5, ip, sb @ eor ip, ip, sb
    eor r5, ip, sb
    mov ip, r5
    mov ip, r5
    strb ip, [r2] @ strb ip, [r2]
    strb ip, [r2]
    eor sb, r1, lr @ eor sb, r1, lr
    eor sb, r1, lr
    lsr ip, sb, #7 @ lsr ip, sb, #7
    lsr ip, sb, #7
    lsl fp, ip, #1 @ lsl fp, ip, #1
    lsl fp, ip, #1
    add r5, ip, fp @ add ip, ip, fp
    add r5, ip, fp
    mov ip, r5
    mov ip, r5
    add r5, ip, ip, lsl #3 @ add ip, ip, ip, lsl #3
    add r5, ip, ip, lsl #3
    mov ip, r5
    mov ip, r5
    eor r5, ip, sb, lsl #1 @ eor ip, ip, sb, lsl #1
    eor r5, ip, sb, lsl #1
    mov ip, r5
    mov ip, r5
    eors r5, r1, r7 @ eors r1, r1, r7
    eors r5, r1, r7
    mov r1, r5
    mov r1, r5
    eor r5, ip, r1 @ eor ip, ip, r1
    eor r5, ip, r1
    mov ip, r5
    mov ip, r5
    strb ip, [r2, #1] @ strb ip, [r2, #1]
    strb ip, [r2, #1]
    lsr r1, r8, #7 @ lsr r1, r8, #7
    lsr r1, r8, #7
    lsl ip, r1, #1 @ lsl ip, r1, #1
    lsl ip, r1, #1
    add r5, r1, ip @ add r1, r1, ip
    add r5, r1, ip
    mov r1, r5
    mov r1, r5
    add r5, r1, r1, lsl #3 @ add r1, r1, r1, lsl #3
    add r5, r1, r1, lsl #3
    mov r1, r5
    mov r1, r5
    eor r5, r1, r8, lsl #1 @ eor r1, r1, r8, lsl #1
    eor r5, r1, r8, lsl #1
    mov r1, r5
    mov r1, r5
    eor r5, lr, r7 @ eor lr, lr, r7
    eor r5, lr, r7
    mov lr, r5
    mov lr, r5
    eor r5, r1, lr @ eor r1, r1, lr
    eor r5, r1, lr
    mov r1, r5
    mov r1, r5
    strb r1, [r2, #2] @ strb r1, [r2, #2]
    strb r1, [r2, #2]
    eor r1, r3, r0 @ eor r1, r3, r0
    eor r1, r3, r0
    lsrs r3, r1, #7 @ lsrs r3, r1, #7
    lsrs r3, r1, #7
    lsl ip, r3, #1 @ lsl ip, r3, #1
    lsl ip, r3, #1
    add r5, r3, ip @ add r3, r3, ip
    add r5, r3, ip
    mov r3, r5
    mov r3, r5
    add r5, r3, r3, lsl #3 @ add r3, r3, r3, lsl #3
    add r5, r3, r3, lsl #3
    mov r3, r5
    mov r3, r5
    eor r5, r3, r1, lsl #1 @ eor r3, r3, r1, lsl #1
    eor r5, r3, r1, lsl #1
    mov r3, r5
    mov r3, r5
    eors r5, r0, r7 @ eors r0, r0, r7
    eors r5, r0, r7
    mov r0, r5
    mov r0, r5
    eors r5, r3, r0 @ eors r3, r3, r0
    eors r5, r3, r0
    mov r3, r5
    mov r3, r5
    strb r3, [r2, #3] @ strb r3, [r2, #3]
    strb r3, [r2, #3]
    adds r5, r2, #4 @ adds r2, r2, #4
    adds r5, r2, #4
    mov r2, r5
    mov r2, r5
    cmp r2, sl @ cmp r2, sl
    cmp r2, sl
    bne .L21 @ bne .L21
    bne .L21
    b .L32 @ b .L32
    b .L32
.L31:
    ldr sl, [sp, #12] @ ldr sl, [sp, #12]
    ldr sl, [sp, #12]
    ldr r1, .L33 @ ldr r1, .L33
    ldr r1, .L33
    ldr r0, [sp, #4] @ ldr r0, [sp, #4]
    ldr r0, [sp, #4]
.L22:
    movs r3, #0 @ movs r3, #0
    movs r3, #0
.L24:
    ldrb r2, [sl, r3, lsl #2] @ ldrb r2, [sl, r3, lsl #2]
    ldrb r2, [sl, r3, lsl #2]
    ldrb r5, [r1, r2] @ ldrb r2, [r1, r2]
    ldrb r5, [r1, r2]
    mov r2, r5
    mov r2, r5
    strb r2, [sl, r3, lsl #2] @ strb r2, [sl, r3, lsl #2]
    strb r2, [sl, r3, lsl #2]
    adds r5, r3, #1 @ adds r3, r3, #1
    adds r5, r3, #1
    mov r3, r5
    mov r3, r5
    cmp r3, #4 @ cmp r3, #4
    cmp r3, #4
    bne .L24 @ bne .L24
    bne .L24
    add r5, sl, #1 @ add sl, sl, #1
    add r5, sl, #1
    mov sl, r5
    mov sl, r5
    cmp sl, r0 @ cmp sl, r0
    cmp sl, r0
    bne .L22 @ bne .L22
    bne .L22
    ldrb r3, [r4, #1] @ ldrb r3, [r4, #1]
    ldrb r3, [r4, #1]
    ldrb r2, [r4, #5] @ ldrb r2, [r4, #5]
    ldrb r2, [r4, #5]
    strb r2, [r4, #1] @ strb r2, [r4, #1]
    strb r2, [r4, #1]
    ldrb r2, [r4, #9] @ ldrb r2, [r4, #9]
    ldrb r2, [r4, #9]
    strb r2, [r4, #5] @ strb r2, [r4, #5]
    strb r2, [r4, #5]
    ldrb r2, [r4, #13] @ ldrb r2, [r4, #13]
    ldrb r2, [r4, #13]
    strb r2, [r4, #9] @ strb r2, [r4, #9]
    strb r2, [r4, #9]
    strb r3, [r4, #13] @ strb r3, [r4, #13]
    strb r3, [r4, #13]
    ldrb r3, [r4, #2] @ ldrb r3, [r4, #2]
    ldrb r3, [r4, #2]
    ldrb r2, [r4, #10] @ ldrb r2, [r4, #10]
    ldrb r2, [r4, #10]
    strb r2, [r4, #2] @ strb r2, [r4, #2]
    strb r2, [r4, #2]
    strb r3, [r4, #10] @ strb r3, [r4, #10]
    strb r3, [r4, #10]
    ldrb r3, [r4, #6] @ ldrb r3, [r4, #6]
    ldrb r3, [r4, #6]
    ldrb r2, [r4, #14] @ ldrb r2, [r4, #14]
    ldrb r2, [r4, #14]
    strb r2, [r4, #6] @ strb r2, [r4, #6]
    strb r2, [r4, #6]
    strb r3, [r4, #14] @ strb r3, [r4, #14]
    strb r3, [r4, #14]
    ldrb r3, [r4, #3] @ ldrb r3, [r4, #3]
    ldrb r3, [r4, #3]
    ldrb r2, [r4, #15] @ ldrb r2, [r4, #15]
    ldrb r2, [r4, #15]
    strb r2, [r4, #3] @ strb r2, [r4, #3]
    strb r2, [r4, #3]
    ldrb r2, [r4, #11] @ ldrb r2, [r4, #11]
    ldrb r2, [r4, #11]
    strb r2, [r4, #15] @ strb r2, [r4, #15]
    strb r2, [r4, #15]
    ldrb r2, [r4, #7] @ ldrb r2, [r4, #7]
    ldrb r2, [r4, #7]
    strb r2, [r4, #11] @ strb r2, [r4, #11]
    strb r2, [r4, #11]
    strb r3, [r4, #7] @ strb r3, [r4, #7]
    strb r3, [r4, #7]
    ldr r2, [sp, #8] @ ldr r2, [sp, #8]
    ldr r2, [sp, #8]
    mov r1, r4 @ mov r1, r4
    mov r1, r4
    movs r0, #10 @ movs r0, #10
    movs r0, #10
    adr lr, .L1002 @ bl add_round_key
    adr lr, .L1002
    orr lr, #1
    orr lr, #1
    b add_round_key
    b add_round_key
.L1002:
    add r5, sp, #16 @ add sp, sp, #16
    add r5, sp, #16
    mov sp, r5
    mov sp, r5
    @ sp needed
    add r5, sp, #32 @ ldmia sp!, {r4, r6, r7, r8, sb, sl, fp, pc}
    add r5, sp, #32
    mov sp, r5
    mov sp, r5
    sub r5, sp, #32
    sub r5, sp, #32
    ldmia r5, {r4, r6, r7, r8, sb, sl, fp, pc}
    ldmia r5, {r4, r6, r7, r8, sb, sl, fp, pc}
.L34:
    .align 2
.L33:
    .word .LANCHOR0
    .size cipher, .-cipher
    .align 1
    .global report_error
    .syntax unified
    .thumb
    .thumb_func
    .fpu softvfp
    .type report_error, %function
report_error:
    @ Volatile: function does not return.
    @ args = 0, pretend = 0, frame = 0
    @ frame_needed = 0, uses_anonymous_args = 0
    @ link register save eliminated.
.L36:
    b .L36 @ b .L36
    b .L36
    .size report_error, .-report_error
    .align 1
    .global report_done
    .syntax unified
    .thumb
    .thumb_func
    .fpu softvfp
    .type report_done, %function
report_done:
    @ Volatile: function does not return.
    @ args = 0, pretend = 0, frame = 0
    @ frame_needed = 0, uses_anonymous_args = 0
    stmdb sp, {r3, lr} @ stmdb sp!, {r3, lr}
    stmdb sp, {r3, lr}
    sub r5, sp, #8
    sub r5, sp, #8
    mov sp, r5
    mov sp, r5
    adr lr, .L1003 @ bl report_done
    adr lr, .L1003
    orr lr, #1
    orr lr, #1
    b report_done
    b report_done
.L1003:
    .size report_done, .-report_done
    .align 1
    .global AES_ECB_encrypt
    .syntax unified
    .thumb
    .thumb_func
    .fpu softvfp
    .type AES_ECB_encrypt, %function
AES_ECB_encrypt:
    @ Volatile: function does not return.
    @ args = 0, pretend = 0, frame = 176
    @ frame_needed = 0, uses_anonymous_args = 0
    stmdb sp, {lr} @ stmdb sp!, {lr}
    stmdb sp, {lr}
    sub r5, sp, #4
    sub r5, sp, #4
    mov sp, r5
    mov sp, r5
    sub r5, sp, #180 @ sub sp, sp, #180
    sub r5, sp, #180
    mov sp, r5
    mov sp, r5
    mov r4, r1 @ mov r4, r1
    mov r4, r1
    mov r1, r0 @ mov r1, r0
    mov r1, r0
    mov r0, sp @ mov r0, sp
    mov r0, sp
    adr lr, .L1004 @ bl key_expansion
    adr lr, .L1004
    orr lr, #1
    orr lr, #1
    b key_expansion
    b key_expansion
.L1004:
    mov r1, sp @ mov r1, sp
    mov r1, sp
    mov r0, r4 @ mov r0, r4
    mov r0, r4
    adr lr, .L1005 @ bl cipher
    adr lr, .L1005
    orr lr, #1
    orr lr, #1
    b cipher
    b cipher
.L1005:
    adr lr, .L1006 @ bl report_done
    adr lr, .L1006
    orr lr, #1
    orr lr, #1
    b report_done
    b report_done
.L1006:
    .size AES_ECB_encrypt, .-AES_ECB_encrypt
    .section .rodata
    .align 2
    .set .LANCHOR0,. + 0
    .type sbox, %object
    .size sbox, 256
sbox:
    .ascii	"c|w{\362ko\3050\001g+\376\327\253v\312\202\311}\372"
    .ascii	"YG\360\255\324\242\257\234\244r\300\267\375\223&6?\367"
    .ascii	"\3144\245\345\361q\3301\025\004\307#\303\030\226\005"
    .ascii	"\232\007\022\200\342\353'\262u\011\203,\032\033nZ\240"
    .ascii	"R;\326\263)\343/\204S\321\000\355 \374\261[j\313\276"
    .ascii	"9JLX\317\320\357\252\373CM3\205E\371\002\177P<\237\250"
    .ascii	"Q\243@\217\222\2358\365\274\266\332!\020\377\363\322"
    .ascii	"\315\014\023\354_\227D\027\304\247~=d]\031s`\201O\334"
    .ascii	"\"*\220\210F\356\270\024\336^\013\333\3402:\012I\006"
    .ascii	"$\\\302\323\254b\221\225\344y\347\3107m\215\325N\251"
    .ascii	"lV\364\352ez\256\010\272x%.\034\246\264\306\350\335"
    .ascii	"t\037K\275\213\212p>\265fH\003\366\016a5W\271\206\301"
    .ascii	"\035\236\341\370\230\021i\331\216\224\233\036\207\351"
    .ascii	"\316U(\337\214\241\211\015\277\346BhA\231-\017\260T"
    .ascii	"\273\026"
    .type rcon, %object
    .size rcon, 11
rcon:
    .ascii	"\215\001\002\004\010\020 @\200\0336"
    .ident "GCC: (15:9-2019-q4-0ubuntu1) 9.2.1 20191025 (release) [ARM/arm-9-branch revision 277599]"
