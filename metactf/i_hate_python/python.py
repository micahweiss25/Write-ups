import random

def do_thing(a, b):
    return ((a << 1) & b) ^ ((a << 1) | b)
    # &: set each bit to 1 if both bits are 1
    # ^: xor
    # >>: signed shift right, rightmost falls off
    # |: OR: sets each bit to one if one of two bits is one
    # 1001
    #  
def test(usr_input):
    x = usr_input #input("What's the password? ") # len(x) = 25
    if len(x) != 25:
        print("WRONG!!!!!")
    else:
        random.seed(997) # will always get 0.465698983134 as the first random number because the seed is 997
        
        k = [random.randint(0, 256) for _ in range(len(x))] # random.randint() isn't very random when you know the seed... 
        # k = [238, 229, 153, 143, 89, 184, 100, 182, 101, 33, 48, 246, 216, 6, 234, 193, 0, 103, 204, 162, 9, 2, 167, 52, 220]
        
        a = { b: do_thing(ord(c), d) for (b, c), d in zip(enumerate(x), k) } # b is the position and c is the value of x
        # zip_output = (0,{x[0]},238),(1,{x[1]},229)
        # b = 0, c = {x[0]}, d = 238, a[0] = 9
        # a = {0: do_thing(ord({x[0]}), 238), 1: do_thing(ord({x[1]}), 229),...,24: ?}

        b = list(range(len(x)))
        # b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        random.shuffle(b) 
        # b = [20, 13, 4, 15, 3, 23, 22, 10, 17, 0, 16, 7, 21, 12, 1, 2, 18, 19, 6, 11, 5, 8, 9, 24, 14]
        
        c = [a[i] for i in b[::-1]]
        # b[::-1] = [14, 24, 9, 8, 5, 11, 6, 19, 18, 2, 1, 12, 21, 7, 16, 0, 17, 10, 22, 23, 3, 15, 4, 13, 20]
        # c = [a[14],a[24],...,a[20]]
        kn = [47, 123, 113, 232, 118, 98, 183, 183, 77, 64, 218, 223, 232, 82, 16, 72, 68, 191, 54, 116, 38, 151, 174, 234, 127]
        valid = list(filter(lambda s: kn[s[0]] == s[1], enumerate(c)))
        return valid
        # kn[0] == c[0], kn[1] = c[1], kn[2] = c[2]
        # kn[0] == a[14], kn[1] = a[24],
        #[a[14]=47,a[24]=123]
        # a[1]=k[14], a[2]=

        if valid == len(x):
            print("Password is correct! Flag:", x)
        else:
            print("less wrong")
tot_len = 13

psw = ''
x = chr(70)
a_len = 'a'*(24-len(psw))
payload = psw + x + a_len
num_correct = 0

print(len(test(psw + '^'+'~'*(24-len(psw)))))
print(len(psw))
print(len(psw + x + a_len))
while num_correct < 125:
    for i in range(33,127):
        if len(test(psw+chr(i)+'~'*(24-len(psw)))) > num_correct:
            psw += chr(i)
            num_correct += 1
            print(chr(i))

'''
print(len(psw))
while 
for i in range(33,126):
    if len((test(psw+chr(i)+'a'*(11)))) == 14:
        print(psw+chr(i))
'''

#(8,77)(19,116)
MetaCTF{yOu_w!N_th1$_0n3}