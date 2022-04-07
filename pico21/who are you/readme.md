# Who Are You
- Category: Web
- Flag: picoCTF
- Points: 100

## Challenge
### Description
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn http://mercury.picoctf.net:34588/
### Hint
It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616

## First Steps
look at the hint. Find out that it's extremely dense.
## Right Path
The website says you must be using PicoBrowser (very similar to https://github.com/micahweiss25/Write-ups/tree/main/pico21/picobrowser). This time
I found out you can change what User-Agent firefox shows by going to about:config and creating "general.useragent.override" and assigning it
PicoBrowser. That takes you to the next page which says it doesn't trust someone from another website. This alludes to the referer header.
After looking extensively, I couldn't figure out how to change referer in the browser without an extension, so I moved to burp suite. 
In burp suite, I used proxy, intercept, and changed the request headers there. ![]()
