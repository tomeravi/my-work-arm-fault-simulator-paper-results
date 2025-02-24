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
	.file	"secure_boot.c"
	.text
	.align	1
	.global	sha256
	.syntax unified
	.thumb
	.thumb_func
	.fpu softvfp
	.type	sha256, %function
sha256:
	@ args = 0, pretend = 0, frame = 336
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r6, r7, r8, r9, r10, fp, lr}
	sub	sp, sp, #336
	str	r0, [sp, #4]
	mov	r7, r1
	str	r2, [sp, #12]
	add	r4, sp, #304
	ldr	r6, .L20
	ldmia	r6!, {r0, r1, r2, r3}
	stmia	r4!, {r0, r1, r2, r3}
	ldm	r6, {r0, r1, r2, r3}
	stm	r4, {r0, r1, r2, r3}
	str	r7, [sp, #8]
	cmp	r7, #0
	beq	.L3
	mov	r8, #0
	add	ip, sp, #108
	ldr	r3, .L20
	add	r7, r3, #284
	add	r1, sp, #16
	add	lr, sp, #332
	b	.L2
.L19:
	add	r4, r4, r2
	str	r4, [sp, #16]
	ldr	r3, [sp, #32]
	add	r2, r2, r3
	str	r2, [sp, #32]
	cmp	r9, r7
	beq	.L18
.L7:
	ldr	r4, [sp, #32]
	ldr	r3, [sp, #40]
	bic	r2, r3, r4
	ldr	r0, [sp, #36]
	ands	r0, r0, r4
	eors	r2, r2, r0
	ror	r3, r4, #11
	eor	r3, r3, r4, ror #6
	eor	r3, r3, r4, ror #25
	add	r2, r2, r3
	ldr	r3, [sp, #44]
	add	r2, r2, r3
	ldr	r3, [r9, #4]!
	add	r2, r2, r3
	ldr	r3, [r10, #4]!
	add	r2, r2, r3
	ldr	fp, [sp, #16]
	ldr	r0, [sp, #20]
	ldr	r6, [sp, #24]
	ror	r3, fp, #13
	eor	r3, r3, fp, ror #2
	eor	r3, r3, fp, ror #22
	eor	r4, r0, r6
	and	r4, r4, fp
	ands	r0, r0, r6
	eors	r4, r4, r0
	add	r4, r4, r3
	add	r3, sp, #44
.L6:
	ldr	r0, [r3, #-4]
	str	r0, [r3], #-4
	cmp	r3, r1
	bne	.L6
	b	.L19
.L18:
	add	r3, sp, #300
	add	r0, sp, #12
.L8:
	ldr	r2, [r3, #4]!
	ldr	r4, [r0, #4]!
	add	r2, r2, r4
	str	r2, [r3]
	cmp	r3, lr
	bne	.L8
	add	r8, r8, #64
	ldr	r3, [sp, #8]
	cmp	r3, r8
	bls	.L3
.L2:
	ldr	r3, [sp, #4]
	add	r0, r3, r8
	add	r10, sp, #44
	add	r2, sp, #48
	mov	r4, r10
.L4:
	ldrb	r6, [r0]	@ zero_extendqisi2
	ldrb	r3, [r0, #1]	@ zero_extendqisi2
	lsls	r3, r3, #16
	orr	r3, r3, r6, lsl #24
	ldrb	r6, [r0, #3]	@ zero_extendqisi2
	orrs	r3, r3, r6
	ldrb	r6, [r0, #2]	@ zero_extendqisi2
	orr	r3, r3, r6, lsl #8
	str	r3, [r4, #4]!
	adds	r0, r0, #4
	cmp	r4, ip
	bne	.L4
	add	r9, r2, #192
.L5:
	mov	r6, r2
	ldr	r0, [r2, #56]
	ldr	r4, [r2, #4]!
	ror	r3, r0, #19
	eor	r3, r3, r0, ror #17
	eor	r3, r3, r0, lsr #10
	ldr	r0, [r6, #36]
	ldr	r6, [r6]
	add	r0, r0, r6
	add	r3, r3, r0
	ror	r0, r4, #18
	eor	r0, r0, r4, ror #7
	eor	r0, r0, r4, lsr #3
	add	r3, r3, r0
	str	r3, [r2, #60]
	cmp	r2, r9
	bne	.L5
	ldr	r3, [sp, #304]
	str	r3, [sp, #16]
	ldr	r3, [sp, #308]
	str	r3, [sp, #20]
	ldr	r3, [sp, #312]
	str	r3, [sp, #24]
	ldr	r3, [sp, #316]
	str	r3, [sp, #28]
	ldr	r3, [sp, #320]
	str	r3, [sp, #32]
	ldr	r3, [sp, #324]
	str	r3, [sp, #36]
	ldr	r3, [sp, #328]
	str	r3, [sp, #40]
	ldr	r3, [sp, #332]
	str	r3, [sp, #44]
	ldr	r3, .L20
	add	r9, r3, #28
	b	.L7
.L3:
	add	r1, sp, #300
	ldr	r3, [sp, #12]
	add	r0, sp, #332
.L9:
	ldr	r2, [r1, #4]!
	lsrs	r4, r2, #24
	strb	r4, [r3]
	lsrs	r4, r2, #16
	strb	r4, [r3, #1]
	lsrs	r4, r2, #8
	strb	r4, [r3, #2]
	strb	r2, [r3, #3]
	adds	r3, r3, #4
	cmp	r1, r0
	bne	.L9
	add	sp, sp, #336
	@ sp needed
	pop	{r4, r6, r7, r8, r9, r10, fp, pc}
.L21:
	.align	2
.L20:
	.word	.LANCHOR0
	.size	sha256, .-sha256
	.align	1
	.global	report_error
	.syntax unified
	.thumb
	.thumb_func
	.fpu softvfp
	.type	report_error, %function
report_error:
	@ Volatile: function does not return.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
.L23:
	b	.L23
	.size	report_error, .-report_error
	.align	1
	.global	execute_firmware
	.syntax unified
	.thumb
	.thumb_func
	.fpu softvfp
	.type	execute_firmware, %function
execute_firmware:
	@ Volatile: function does not return.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, lr}
	bl	execute_firmware
	.size	execute_firmware, .-execute_firmware
	.align	1
	.global	verify_and_run_firmware
	.syntax unified
	.thumb
	.thumb_func
	.fpu softvfp
	.type	verify_and_run_firmware, %function
verify_and_run_firmware:
	@ args = 0, pretend = 0, frame = 32
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	sub	sp, sp, #32
	mov	r4, r2
	mov	r2, sp
	bl	sha256
	mov	r1, sp
	subs	r3, r4, #1
	adds	r4, r4, #31
.L28:
	ldrb	r2, [r1], #1	@ zero_extendqisi2
	ldrb	r0, [r3, #1]!	@ zero_extendqisi2
	cmp	r0, r2
	bne	.L31
	cmp	r3, r4
	bne	.L28
	bl	execute_firmware
.L31:
	bl	report_error
	.size	verify_and_run_firmware, .-verify_and_run_firmware
	.section	.rodata
	.align	2
	.set	.LANCHOR0,. + 0
.LC0:
	.word	1779033703
	.word	-1150833019
	.word	1013904242
	.word	-1521486534
	.word	1359893119
	.word	-1694144372
	.word	528734635
	.word	1541459225
	.type	constants, %object
	.size	constants, 256
constants:
	.word	1116352408
	.word	1899447441
	.word	-1245643825
	.word	-373957723
	.word	961987163
	.word	1508970993
	.word	-1841331548
	.word	-1424204075
	.word	-670586216
	.word	310598401
	.word	607225278
	.word	1426881987
	.word	1925078388
	.word	-2132889090
	.word	-1680079193
	.word	-1046744716
	.word	-459576895
	.word	-272742522
	.word	264347078
	.word	604807628
	.word	770255983
	.word	1249150122
	.word	1555081692
	.word	1996064986
	.word	-1740746414
	.word	-1473132947
	.word	-1341970488
	.word	-1084653625
	.word	-958395405
	.word	-710438585
	.word	113926993
	.word	338241895
	.word	666307205
	.word	773529912
	.word	1294757372
	.word	1396182291
	.word	1695183700
	.word	1986661051
	.word	-2117940946
	.word	-1838011259
	.word	-1564481375
	.word	-1474664885
	.word	-1035236496
	.word	-949202525
	.word	-778901479
	.word	-694614492
	.word	-200395387
	.word	275423344
	.word	430227734
	.word	506948616
	.word	659060556
	.word	883997877
	.word	958139571
	.word	1322822218
	.word	1537002063
	.word	1747873779
	.word	1955562222
	.word	2024104815
	.word	-2067236844
	.word	-1933114872
	.word	-1866530822
	.word	-1538233109
	.word	-1090935817
	.word	-965641998
	.ident	"GCC: (15:9-2019-q4-0ubuntu1) 9.2.1 20191025 (release) [ARM/arm-9-branch revision 277599]"
