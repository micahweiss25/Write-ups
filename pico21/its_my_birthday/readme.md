# It's My Birthday
- Category: Web
- Points: 100
- Flag: picoCTF{c0ngr4ts_u_r_1nv1t3d_aebcbf39}
## Challenge
### Description
I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, 
and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. 
Anyway, see if you're invited by submitting 2 PDFs to my website. http://mercury.picoctf.net:48746/
### Hints
- How may a PHP site check the rules in the description?
- Look at the category of this problem.

## First Steps
Inspect source code. Nothing. <br />
I tried figuring out how the php site validates that the two files are pdf. I figured
it probably just checks the extension, so I created two empty files and added pdf extensions 
to them. Instead of getting the "Not a PDF!" alert, I got "Files are not different!"
So, I know I just need to file with pdf extensions that come out to the same md5 hash. 
## Right Path
Google.
I read a couple articles and found out that getting a collision between two different files is not very hard with md5. 

refs
-https://github.com/corkami/collisions#pdf
## Solve
I found an example of two different files that had the same hash, downloaded them, submitted, and got the flag. 
## Thoughts
I feel slightly guilty for just using two files that where the same 
instead of making my own two files that collided, but I'm not a crypto guy.
