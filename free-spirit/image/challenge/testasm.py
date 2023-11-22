from pwn import *
context.arch = 'amd64'
a = '''
   mov rsi, rdx
   mov rdx,100
   syscall
'''
x = asm(a)

print len(x)
