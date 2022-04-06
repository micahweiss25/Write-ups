First, get the file <br />
![this works](img/st3go.png)
then, we use a stego tool because I'm stupid and don't know any other way to do it
```
$ zsteg pico.flag.png
```
which returns <br />
![results](img/zsteg_command.png)
and there we go! There's the flag
picoCTF{7h3r3_15_n0_5p00n_a1062667}

p.s.
this writeup was to practice using markup language. The solution for the challenge actually comes from ->
https://github.com/LambdaMamba/CTFwriteups/tree/main/picoCTF_2022/Forensics/St3g0 <br />
link to tool: https://github.com/zed-0xff/zsteg <br />
more indepth explaination: https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2


# WHY:
## LSB image stenography
the least significant bit of each RBG value was replaced with a bit of the hidden message. Each 8 bit segment of LSB's in the challenge photo converts back into an ascii value. 
