# Some Assembly Required
- Category: Web
- Points: 70
- Flag: picoCTF{cb688c00b5a2ede7eaedcae883735759}

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
I used https://deobfuscate.io/ to deobfuscate the script.
```
const raquela = ["value", "2wfTpTR", "instantiate", "275341bEPcme", "innerHTML", "1195047NznhZg", "1qfevql", "input", "1699808QuoWhA", "Correct!", "check_flag", "Incorrect!", "./JIFxzHyW8W", "23SMpAuA", "802698XOMSrr", "charCodeAt", "474547vVoGDO", "getElementById", "instance", "copy_char", "43591XxcWUl", "504454llVtzW", "arrayBuffer", "2NIQmVj", "result"];
const trilby = function (jarret, semere) {
  jarret = jarret - 470;
  let dejanai = raquela[jarret];
  return dejanai;
};
(function (gerold, daedalus) {
  const kenderrick = trilby;
  while (!![]) {
    try {
      const eino = -parseInt(kenderrick(491)) + parseInt(kenderrick(493)) + -parseInt(kenderrick(475)) * -parseInt(kenderrick(473)) + -parseInt(kenderrick(482)) * -parseInt(kenderrick(483)) + -parseInt(kenderrick(478)) * parseInt(kenderrick(480)) + parseInt(kenderrick(472)) * parseInt(kenderrick(490)) + -parseInt(kenderrick(485));
      if (eino === daedalus) break; else gerold.push(gerold.shift());
    } catch (marquet) {
      gerold.push(gerold.shift());
    }
  }
}(raquela, 627907));
let exports;
(async () => {
  const lashawanda = trilby;
  let aleksy = await fetch(lashawanda(489)), aramie = await WebAssembly[lashawanda(479)](await aleksy[lashawanda(474)]()), jasir = aramie[lashawanda(470)];
  exports = jasir.exports;
})();
function onButtonPress() {
  const videlle = trilby;
  let lanyia = document.getElementById(videlle(484))[videlle(477)];
  for (let ivalee = 0; ivalee < lanyia.length; ivalee++) {
    exports[videlle(471)](lanyia[videlle(492)](ivalee), ivalee);
  }
  exports.copy_char(0, lanyia.length), exports[videlle(487)]() == 1 ? document[videlle(494)](videlle(476))[videlle(481)] = videlle(486) : document[videlle(494)](videlle(476))[videlle(481)] = videlle(488);
}
```
still not really able to make anything out but I see a clear compare - if (eino == daedalus) break; - so I wanted to see if I could step through the code in the browser using the firefox web tools debugger in order to find what is stored in these variables. 
![](some_assembly_required.png) While stepping through, right around when there is a while loop forming the string for a variable, it took me to file I hadn't seen before. I control-F'ed it for picoCTF and found the flag.

## Right Path
Although I didn't come at this challenge from the correct angle, I learned what I should have done after further inspection. As the title suggests, this is a web assembly challenge. 

## Solve
open debug, step through until code is compiled to web assembly and exported, control f the web assembly for the flag


## Thoughts
### what is web assembly
code that can be ran in web browsers and is a compilation target for source languages like C, C++, Rust, etc. (A compiler takes the source files and turns them into web assembly. Ref below). In the js script, there is a wasmcall, which I'm sure means web asm and result in a file being compiled to web assembly. I think this happens when export is called, but I'm not sure how to replicate this in a harder challenge outside of just stepping through until export or some assembly call is made. 


https://developer.mozilla.org/en-US/docs/WebAssembly/Concepts


"Compilers are, in essence, translators that take input in one language and produce output in another. For example, Eiffel Software's compiler takes Eiffel-language input and produces C. GCC for Intel reads C-language input and produces x86 assembly. The GAS assembler for Intel takes x86 assembly and produces x86 object code. All three of these things are technically compilers.

Regardless of format, the input read by a compiler is called the source and the output is called the target. The latter term is taken from one of its definitions, "intended result."

The majority of compilers are designed to produce assembly or object code for a particular processor or architecture. Because of that, target is often used to refer to the architecture itself rather than the output format.

The target of a compiler does not need to be the same as the architecture where it runs, and in instances where that happens, the program is called a cross-compiler. (For example, GCC can be built to run on x86 systems to compile C into ARM assembly.)

Additionally, there are single compilers capable of producing output for different targets depending on input such as switches on the command line. These are called multi-target compilers" - Blrfl, StackExchange
