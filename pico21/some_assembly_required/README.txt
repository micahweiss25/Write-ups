# Some Assembly Required
- Category: Web
- Points: 70
- Flag: 

## Challenge
http://mercury.picoctf.net:40226/index.html

## First Steps
I pulled the source code of the webpage into a file
```wget http://mercury.picoctf.net:40226/index.html```
which gave me
```
StatusCode        : 200
StatusDescription : OK
Content           : <html>
                    <head>
                    	<meta charset="UTF-8">
                    	<script src="G82XCw5CX3.js"></script>
                    </head>
                    <body>
                    	<h4>Enter flag:</h4>
                    	<input type="text" id="input"/>
                    	<button 
                    onclick="onButtonPress()">Submit</button>
                    	<...
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 235
                    Content-Type: text/html
                    Last-Modified: Tue, 16 Mar 2021 00:38:36 GMT
                    
                    <html>
                    <head>
                    	<meta charset="UTF-8">
                    	<script src="G82XCw5CX3.js"></script>
                    </head>
                    <bod...
Forms             : {}
Headers           : {[Content-Length, 235], [Content-Type, 
                    text/html], [Last-Modified, Tue, 16 Mar 2021 
                    00:38:36 GMT]}
Images            : {}
InputFields       : {@{innerHTML=; innerText=; outerHTML=<INPUT 
                    id=input>; outerText=; tagName=INPUT; 
                    id=input}}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 235
```

## Right Path

## Solve

## Thoughts
