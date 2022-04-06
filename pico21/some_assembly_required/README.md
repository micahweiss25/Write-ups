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
I didn't see anything interesting...
I moved onto checking G82XCw5CX3.js
```
const _0x402c=['value','2wfTpTR','instantiate','275341bEPcme','innerHTML','1195047NznhZg','1qfevql','input','1699808QuoWhA','Correct!','check_flag','Incorrect!','./JIFxzHyW8W','23SMpAuA','802698XOMSrr','charCodeAt','474547vVoGDO','getElementById','instance','copy_char','43591XxcWUl','504454llVtzW','arrayBuffer','2NIQmVj','result'];const _0x4e0e=function(_0x553839,_0x53c021){_0x553839=_0x553839-0x1d6;let _0x402c6f=_0x402c[_0x553839];return _0x402c6f;};(function(_0x76dd13,_0x3dfcae){const _0x371ac6=_0x4e0e;while(!![]){try{const _0x478583=-parseInt(_0x371ac6(0x1eb))+parseInt(_0x371ac6(0x1ed))+-parseInt(_0x371ac6(0x1db))*-parseInt(_0x371ac6(0x1d9))+-parseInt(_0x371ac6(0x1e2))*-parseInt(_0x371ac6(0x1e3))+-parseInt(_0x371ac6(0x1de))*parseInt(_0x371ac6(0x1e0))+parseInt(_0x371ac6(0x1d8))*parseInt(_0x371ac6(0x1ea))+-parseInt(_0x371ac6(0x1e5));if(_0x478583===_0x3dfcae)break;else _0x76dd13['push'](_0x76dd13['shift']());}catch(_0x41d31a){_0x76dd13['push'](_0x76dd13['shift']());}}}(_0x402c,0x994c3));let exports;(async()=>{const _0x48c3be=_0x4e0e;let _0x5f0229=await fetch(_0x48c3be(0x1e9)),_0x1d99e9=await WebAssembly[_0x48c3be(0x1df)](await _0x5f0229[_0x48c3be(0x1da)]()),_0x1f8628=_0x1d99e9[_0x48c3be(0x1d6)];exports=_0x1f8628['exports'];})();function onButtonPress(){const _0xa80748=_0x4e0e;let _0x3761f8=document['getElementById'](_0xa80748(0x1e4))[_0xa80748(0x1dd)];for(let _0x16c626=0x0;_0x16c626<_0x3761f8['length'];_0x16c626++){exports[_0xa80748(0x1d7)](_0x3761f8[_0xa80748(0x1ec)](_0x16c626),_0x16c626);}exports['copy_char'](0x0,_0x3761f8['length']),exports[_0xa80748(0x1e7)]()==0x1?document[_0xa80748(0x1ee)](_0xa80748(0x1dc))[_0xa80748(0x1e1)]=_0xa80748(0x1e6):document[_0xa80748(0x1ee)](_0xa80748(0x1dc))[_0xa80748(0x1e1)]=_0xa80748(0x1e8);}
```

## Right Path
The js file checks the user's input against a value, flag, which is stored locally. So, we need to de-obviscate the code to get the flag
## Solve

## Thoughts
