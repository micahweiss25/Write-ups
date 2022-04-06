passwords = []

with open("/home/wei/CTF/pico/pico22/crypto/cred/passwords.txt","r") as file:
    for line in file:
        passwords.append(line.strip())
usernames = []
with open("/home/wei/CTF/pico/pico22/crypto/cred/usernames.txt", "r") as file:
    for line in file:
        usernames.append(line.strip())
index = usernames.index("cultiris")
print(usernames[377])
print(index)
encoded = passwords[index]
print(encoded)
print(passwords[:5])
print(usernames[:5])

counter = 0 
for i in usernames:
    print(i)