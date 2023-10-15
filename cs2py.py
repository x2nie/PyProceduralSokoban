# -*- coding: utf-8 -*-
# original author: Ethosa
# modified by: x2nie

import re
from retranslator import Translator

class CSharpToPython(Translator):
    def __init__(self, codeString="", extra=[], useRegex=False):
        """initialize class

        Keyword Arguments:
            codeString {str} -- source code on C# (default: {""})
            extra {list} -- include your own rules (default: {[]})
            useRegex {bool} -- this parameter tells you to use regex (default: {False})
        """
        self.codeString = codeString
        self.extra = extra
        self.Transform = self.compile = self.translate # callable objects

        # create little magic ...
        self.rules = CSharpToPython.RULES[:]
        self.rules.extend(self.extra)
        self.rules.extend(CSharpToPython.LAST_RULES)
        # Translator.__init__(self, codeString, self.rules, useRegex)
        super(CSharpToPython, self).__init__(codeString, self.rules, useRegex)

    def translate(self, src=None):
        if not src is None:
            self.codeString = src
        self.expliciteSelf()
        self.codeString = self._resolveProperties(self.codeString)
        self.codeString = self._resolveMethods(self.codeString)
        ret = super(CSharpToPython, self).translate()
        ret = super(CSharpToPython, self).translate()
        ret = self.splitMultipleAssignments(ret)
        return ret

    def expliciteSelf(self):
        self.properties = {}
        self.methods = {}
        self._grepProperties()
        self._grepMethods()
        pass
        for p in self.properties:
            print(p)

    def _grepProperties(self):
        rule = r"(?P<blockIndent>[ ]+)(?P<severity>(public|private|protected)[ ]+)(?P<returnType>[^\s]+[ ]+)(?P<methodName>[\w]+)[ ]*;"
        matches = re.finditer(rule, self.codeString, re.MULTILINE)

        for match in matches:
            # self.properties.append(match.groupdict()['methodName'])
            d = match.groupdict()
            rep = r'self.%(methodName)s' % d #*dict
            pat = r'\w*(?<!%(returnType)s)(?<!\.)%(methodName)s' % d #*dict
            pat = pat.replace('[',r'\[').replace(']',r'\]')
            self.properties[pat] = rep
            # self.properties.append(pat)
            # for name, s in match.groupdict().items():
            #     print(f"     Group {name} `{s}`")

    def _resolveProperties(self, src):
        for pat, rep in self.properties.items():
            src = re.sub(pat, rep, src, 0, re.MULTILINE)
        return src

    def _grepMethods(self):
        rule = r"(?P<start>[\s]+)(?P<severity>(?:public |private |protected |published |override |overload )+)(?P<returnType>\w+[ ]+)(?P<methodName>\w+)[ ]*\((?P<args>[\S ]*)\)"
        matches = re.finditer(rule, self.codeString, re.MULTILINE)

        for match in matches:
            # self.properties.append(match.groupdict()['methodName'])
            d = match.groupdict()
            rep = r'self.%(methodName)s' % d #*dict
            pat = r'\w*(?<!%(returnType)s)(?<!\.)%(methodName)s' % d
            pat = pat.replace('[',r'\[').replace(']',r'\]')
            self.methods[pat] = rep
            # for name, s in match.groupdict().items():
            #     print(f"     Group {name} `{s}`")

    def _resolveMethods(self, src):
        for pat, rep in self.methods.items():
            src = re.sub(pat, rep, src, 0, re.MULTILINE)
        return src

    def splitMultipleAssignments(self, src):
        # return src
        pat = r"(?P<start>[\r\n]+)(?P<blockIndent>[ ]*)(?P<varType>[\w\[\]\.]+)[ ]+(?P<varName1>[^, \(]+)(?P<varNames>(?:,[ ]*[\w]+)+)[ ]*=[ ]+(?P<right>[\w]+)"
        def rep(match):
            d = match.groupdict()
            start = d['start']
            indent = d['blockIndent']
            value = d['right']
            lines = []
            # varNames = d['varNames'].split(',')
            varNames = d['varName1'] + d['varNames']
            varNames = varNames.split(',')
            # print('varNames:', varNames)
            # varNames = [d['varName1']] + varNames
            for varName in varNames:
                varName = varName.strip()
                lines.append(f"{start}{indent}{varName} = {value}")

            # print('\n'.join(lines))
            return '\n'.join(lines)
        
        # src = re.sub(pat, rep, src, 10, re.MULTILINE)
        replaceCount = 0
        src = self.r.sub(pat, rep, src, 1)
        while self.r.search(pat, src):
            if replaceCount+1 > 70:
                break
            replaceCount += 1
            src = self.r.sub(pat, rep, src, 1)
        return src


    RULES = [
        (r"\)\s+\{", r"){", None, 0),  #? strip `) {`
        (r"\)[ ]+\{", r"){", None, 0),  #? strip `) {`
        (r"[ ]+\)", r"(", None, 0),  #? strip ` )`
        (r"\([ ]+", r"(", None, 0),  #? strip `( `
        (r"\{[ ]+", r"{", None, 0),  #? strip `{ `
        (r"\}[ ]+", r"}", None, 0),  #? strip `{ `
        # true
        # True
       (r"(?P<left>[\r\n]+(([^\"\r\n]*\"[^\"\r\n]+\"[^\"\r\n]*)+|[^\"\r\n]+))true", r"\g<left>True", None, 0),
        # false
        # False
       (r"(?P<left>[\r\n]+(([^\"\r\n]*\"[^\"\r\n]+\"[^\"\r\n]*)+|[^\"\r\n]+))false", r"\g<left>False", None, 0),
        # this
        # self
        (r"(?P<left>[\r\n]+(([^\"\r\n]*\"[^\"\r\n]+\"[^\"\r\n]*)+|[^\"\r\n]+))this", r"\g<left>self", None, 0),
        # ||
        # or
        (r"\|\|", r"or", None, 0),
        # a.length
        # len(a)
        (r"([a-zA-Z0-9_]+)[ ]*\.[ ]*length", r"len(\1)", None, 0),
        # &&
        # and
        (r"&&", r"and", None, 0),
        # !(...)
        # not (...)
        (r"(?P<left>[\r\n]+(([^\"\r\n]*\"[^\"\r\n]+\"[^\"\r\n]*)+|[^\"\r\n]+))!\((?P<condition>[\S ]+)\)", 
         r"\g<left>not (\g<condition>)", None, 0),
        # // ...
        # # ...
        (r"//([^\r\n]+)", r"#\1",None, 0),

        #? for (int i = 0; i < 5; i+=2){
        #     ....
        # }
        # for i in range(0, 5, 2):
        #     ....
        (r"(?P<blockIndent>[ ]*)for[ ]*\((?P<varType>[\S]+)[ ]*(?P<varName>[\w]+)[ ]*=[ ]*(?P<variable>[\S]+)[ ]*;[ ]*(?P=varName)[ ]*[\S]+[ ]*(?P<number>[\S ]+)[ ]*;[ ]*(?P=varName)[ ]*([\+\-]{1}=)[ ]*(?P<number2>[\S]+)[ ]*\)[ ]*{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}", 
         r'\g<blockIndent>for \g<varName> in range(\g<variable>, \g<number>, \g<number2>):\n\g<body>', None, 70),

        #? for (int i = 0; i < width; i++){
        #     ....
        # }
        # for i in range(0, width):
        #     ....
        #                       for     (    int                   x                 =      0                 ;      x              <      width      ;      x                       ++) {
        (r"(?P<blockIndent>[ ]*)for[ ]*\((?P<varType>[\S]+)[ ]*(?P<varName>[\w]+)[ ]*=[ ]*(?P<start>[^ ;]+)[ ]*;[ ]*(?P=varName)[ ]*\<[ ]*(?P<stop>[^;]+)[ ]*;[ ]*(?P=varName)[ ]*(?P<increment>[\+\-]+)[ ]*\){[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}", 
         r'\g<blockIndent>for \g<varName> in range(\g<start>, \g<stop>):\n\g<body>', None, 70),

        # (r"(?P<blockIndent>[ ]*)for[ ]*\((?P<varType>[\S]+)[ ]*(?P<varName>\w+)[ ]*=[ ]*(?P<start>[\d]+)[ ]*;[ ]*(?P=varName)[ ]*\<[ ]*(?P<stop>\w+)[ ]*;[ ]*(?P=varName)[ ]*(?P<increment>[\+\-]+)[ ]*", 
        #  r'\g<blockIndent>for \g<varName> in range(\g<start>, \g<stop>):HALO\g<increment>UHUY\nCOY', None, 0),



        #? foreach (var i in array){
        #     ....
        # }
        # for i in array:
        #     ....
        (r"(?P<blockIndent>[ ]*)foreach[ ]*\((?P<varType>[\S]+)[ ]*(?P<varName>[\S]+)[ ]*in[ ]*(?P<array>[\S]+)\){[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}", r'\g<blockIndent>for \g<varName> in \g<array>:\n\g<body>', None, 70),
        # /* ... */
        # """ ... """
        (r"/\*(?P<comment>[\S\s]+)\*/", r'"""\g<comment>"""',None, 0),

        #? else if (...){
        #     ....
        # }
        # elif ...:
        #     ....
        (r"(?P<blockIndent>[ ]*)else if[ ]*\((?P<condition>[\S ]*)\){[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}", 
         r'\g<blockIndent>elif \g<condition>:\n\g<body>', None, 70),

        #? if (...){
        #     ....
        # }
        # if ...:
        #     ....
        (r"(?P<start>[\r\n]+)(?P<blockIndent>[ ]*)if[ ]*\((?P<condition>.+?(?=\)\{))\)\{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)\}", 
        # (r"\n(?P<blockIndent>[ ]*)if[ ]*\((?P<condition>[^\)]*)\)\{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)\}", 
         r'\g<start>\g<blockIndent>if \g<condition>:\n\g<body>', None, 70),

        #? else{
        #     ....
        # }
        # else:
        #     ....
        (r"(?P<blockIndent>[ ]*)else[ ]*{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}", r'\g<blockIndent>else:\n\g<body>', None, 70),



        #? (statement) ? val : alt;
        #* val if (statement) else alt:
        (r"\((?P<statement>[^\)]+)\)[ ]*\?[ ]*(?P<val>[^:]+):[ ]*(?P<alt>[^;]*);",  
         r'\g<val>if \g<statement> else \g<alt>', None, 0),




        #? switch (map[x,y]) { 
        # match map[x,y]
        (r"(?P<start>[\r\n]+)(?P<blockIndent>[ ]*)switch[ ]*\((?P<args>[^\)]*)\)\{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)\}",  
         r'\g<start>\g<blockIndent>match \g<args>:\n\g<body>', None, 70),

        #?     break;
        #? case Foo.Bar:
        #* case Foo.Bar:
        (r"(?P<start>[\r\n]+)(?P<break>[ ]+break[ ]*;[\r\n]+)(?P<blockIndent>[ ]*)case[ ]+(?P<args>[^:]*):",  
         r'\g<start>\g<blockIndent>case \g<args>:', None, 0),

        #?     break;
        #? default:
        #* case _:
        (r"(?P<start>[\r\n]+)(?P<break>[ ]+break[ ]*;[\r\n]+)(?P<blockIndent>[ ]*)default[ ]*:",  
         r'\g<start>\g<blockIndent>case _:', None, 0),


        #? case _:
        #?     break;
        #* 
        (r"(?P<start>[\r\n]+)(?P<break>[ ]*case _:[\r\n]+)(?P<blockIndent>[ ]*)break[ ]*;",  
         r'', None, 0),



        #? do {} while (...)
        # while ...:
        #     ....
        (r"(?P<blockIndent>[ ]*)do\s*{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}[ ]*while[ ]*\((?P<condition>[\S ]*)\)", 
         r'\g<blockIndent>while True:\n\g<body>\g<blockIndent>    if not (\g<condition>):\n\g<blockIndent>        break', None, 70),

        #? while (...){
        #     ....
        # }
        # while ...:
        #     ....
        (r"(?P<blockIndent>[ ]*)while[ ]*\((?P<condition>[\S ]*)\){[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}", 
         r'\g<blockIndent>while \g<condition>:\n\g<body>', None, 70),

        #? interface IInterface{
        #     ....
        # }
        # class IInterface:
        #     ....
        (r"(?P<blockIndent>[ ]*)interface[ ]*(?P<interfaceName>[a-zA-Z0-9_]+)[ ]*{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}", 
         r'\g<blockIndent>class \g<interfaceName>:\n\g<body>', None, 70),

        
        (r"(?P<blockIndent>[ ]*)(?P<severity>(?:public |private |protected |published |override |overload |static )+)?class[ ]*(?P<interfaceName>[a-zA-Z0-9_]+)[ ]*{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}", 
         r'\g<blockIndent>class \g<interfaceName>:\n\g<body>', None, 70),

        #? interface method
        # void test();
        # def test():
        #     pass
        (r"(?P<start>[\r\n]+)(?P<blockIndent>[ ]*)(?P<returnType>\w+)[ ]+(?P<methodName>\w+)[ ]*\((?P<args>[\S ]*)\)\;", 
         r'\g<start>\g<blockIndent>def \g<methodName>(self, \g<args>):\n\g<blockIndent>    pass', None, 0),

        #? public void method(){ }
        (r"(?P<start>[\r\n]+)(?P<blockIndent>[ ]*)(?P<severity>(?:public |private |protected |published |override |overload |static )+)(?P<returnType>\w+)[ ]+(?P<methodName>\w+)[ ]*\((?P<args>[\S ]*)\)[ ]*\{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)\}",  
         r'\g<start>\g<blockIndent>def \g<methodName>(self, \g<args>):\n\g<body>', None, 70),

        #? public ClassName(){ }
        #* def __init__( )
        (r"(?P<start>[\r\n]+)(?P<blockIndent>[ ]*)public (?P<methodName>\w+)[ ]*\((?P<args>[\S ]*)\)\{[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)\}",  
         r'\g<start>\g<blockIndent>def __init__(self, \g<args>):\n\g<body>', None, 70),

        #? property / instance var
        (r"(?P<blockIndent>[ ]+)(?P<severity>(public|private|protected)[ ]+)(?P<returnType>[^\s]+)[ ]+(?P<methodName>[\w]+)[ ]*", 
         r"\g<blockIndent>\g<methodName> = None", None, 0),

        #? cleanup
        (r", [\w\]\[]+ (?P<parameterName>[\w]+)", r", \g<parameterName>", None, 0),
        (r"\(self, \):", r"(self):", None, 0),

        # garbage delete
        # (r"\n\n", r"\n", None, 0),
        (r"\n\n\n", r"\n\n", None, 0),
        (r"(?P<blockIndent>[ ]*)(?P<blockName>[a-z]+)[ ]*\([ ]*(?P<other>[\S ]*)[ ]*\){[\s]*}", 
         r"\g<blockIndent>\g<blockName> \g<other>:\n\g<blockIndent>    pass", None, 0),


        #? int i = 0;
        # i = 0;
       (r"(?P<blockIndent>[ ]*)(?P<varType>[\w\[\]\.]+)[ ]+(?P<varName>[\w\.]+)[ ]*=[ ]+(?P<right>[\w\'\"]+)", 
        r'\g<blockIndent>\g<varName> = \g<right>',None, 0),

        # int[] i = {1, 2, 3};
        # i = [1, 2, 3];
        (r"(?P<blockIndent>[ ]*)(?P<varName>[a-zA-Z0-9_]+)[ ]*=[ ]*{(?P<list>[\S ]+)}",
          r'\g<blockIndent>\g<varName> = [\g<list>]',None, 0),

        #? i++
        # i+=1
        (r"\+\+", r" += 1",None, 0),

        #? i--
        # i-=1
        (r"\-\-", r" -= 1",None, 0),

        #? (int)abc
        #* int(abc)
        (r"\((?P<varType>[a-zA-Z0-9_]+)\)(?P<varName>[a-zA-Z0-9_]+)", 
         r"\g<varType>(\g<varName>)",None, 0),

        #? 98.789f
        #* 98.789
        (r"(?P<float>\d+\.\d)f", 
         r"\1",None, 0),

        #? range(0, abc[]/2)  | range(0, r.Next(5));
        #* range(abc)
        # (r"\((?P<varType>[a-zA-Z0-9_]+)\)(?P<varName>[a-zA-Z0-9_]+)", 
        #  r"\g<varType>(\g<varName>)",None, 0),



        #? new Cell[rows.length][]
        #* [[] for j in range(rows)]
        (r"new (?P<varName>[a-zA-Z0-9_]+)\[(?P<rows>[^\]]+)\]\[\]", 
         r"[[] for j in range(\g<rows>)]",None, 0),

        #? new Cell[content[x].Length];
        #* [[] for j in range(rows)]
        #? ((?P<condition>.+?(?=\)\{))\)\{[\r\n]+(?P<body>(?P<ind
        (r"new (?P<varName>[a-zA-Z0-9_]+)\[(?P<rows>.+?(?=\];))\];", 
         r"[None for j in range(\g<rows>)]",None, 0),

        #? new Cell[rows,cols]
        #* [[0 for i in range(cols)] for j in range(rows)]
        (r"new (?P<varName>[a-zA-Z0-9_]+)\[(?P<rows>[a-zA-Z0-9_]+),(?P<cols>[a-zA-Z0-9_]+)\]", 
         r"[[0 for i\g<cols> in range(\g<cols>)] for j\g<rows> in range(\g<rows>)]",None, 0),
        #  r"[[0 for i\g<cols> in range(\g<cols>)] for j\g<rows> in range(\g<rows>)]",None, 0),

        #? new ClassName()
        #* ClassName()
        (r"new (?P<ClassName>[a-zA-Z0-9_]+)\(", 
         r"\g<ClassName>(",None, 0),

        # better view
        # b==a
        # b == a
        # (r"(\S)(==|!=|<=|<|>|>=|=)(\S)", r"\1 \2 \3", None, 0),
        # (r"(\S)[ ]*(==|!=|<=|<|>|>=|=)[ ]*(\S)", r"\1 \2 \3", None, 0),
        # (r"not \(([\S ]+)(?!and|or)([\S ]+)\)", r"not \1\2", None, 0),

        # ;\n
        # \n
       (r"(?P<indent>[ ]*)(?P<line>[\S \t]*);\n", r"\g<indent>\g<line>\n",None, 0),

        # ;
        # \n
    #    (r"(?P<indent>[ ]*)(?P<line>[\S\t]*);[^\r\n]*;", 
    #     r"\g<indent>\g<line>\n\g<indent>",None, 0),

        # ;
        # \n
       (r"(?P<indent>[ ]*)(?P<line>[\S \t]*);[^\r\n]*#", r"\g<indent>\g<line> #",None, 0),
 
    ]

    LAST_RULES = [
        # python methods:
        (r"Console\.WriteLine\((?P<args>[^\)]+)\)", r"print(\g<args>)", None, 0),
        (r"Console\.Write\((?P<args>[^\)]+)\)", r"sys.stdout.write(\g<args>)", None, 0),
        (r"using[ ]+\w+", r"", None, 0),
        (r"\A", r"import random\nimport math\nimport sys", None, 0),
        (r"([a-zA-Z0-9_]+)\.contains\(([\S ]+)\)", r"\2 in \1", None, 0),
        (r"([a-zA-Z0-9_]+)\.equals\(([\S ]+)\)", r"\1 == \2", None, 0),
        # math module:
        (r"Math\.Abs", r"abs", None, 0),
        (r"Math\.Round", r"round", None, 0),
        (r"Math\.PI", r"math.pi", None, 0),
        (r"Math\.E", r"math.e", None, 0),
        (r"Math\.A(?P<name>[a-z]+)", r"math.a\g<name>", None, 0),
        (r"Math\.B(?P<name>[a-z]+)", r"math.b\g<name>", None, 0),
        (r"Math\.C(?P<name>[a-z]+)", r"math.c\g<name>", None, 0),
        (r"Math\.D(?P<name>[a-z]+)", r"math.d\g<name>", None, 0),
        (r"Math\.E(?P<name>[a-z]+)", r"math.e\g<name>", None, 0),
        (r"Math\.F(?P<name>[a-z]+)", r"math.f\g<name>", None, 0),
        (r"Math\.M(?P<name>[a-z]+)", r"math.m\g<name>", None, 0),
        (r"Math\.R(?P<name>[a-z]+)", r"math.r\g<name>", None, 0),
        (r"Math\.P(?P<name>[a-z]+)", r"math.p\g<name>", None, 0),
        (r"Math\.S(?P<name>[a-z]+)", r"math.s\g<name>", None, 0),
        (r"Math\.T(?P<name>[a-z]+)", r"math.t\g<name>", None, 0),
        # random module:
        # (r"new[ ]+Random\(\)\.Next\((?P<first>\d+)[ ]*,[ ]*(?P<second>\d+)\)", r"random.randint(\g<first>, \g<second>+1)", None, 0),
        # (r"new[ ]+Random\(\)\.NextDouble\(\)", r"random.uniform(0, 1)", None, 0)
    ]