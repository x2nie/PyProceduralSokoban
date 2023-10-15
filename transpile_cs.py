import cs2py
# import regex
import re
import math

# src = 'Program.cs'
src = 'Level.cs'
# src = 'Template.cs'
# src = 'Templates.cs'
with open(src, 'r') as f:
    sourceText = f.read()
# print(sourceText)
# print('#'*50)
translator = cs2py.CSharpToPython(useRegex=1)
# print(translator.compile(sourceText))
out = translator.translate(sourceText)
with open('output.py', 'w') as f:
    f.write(out)

# sourceText = regex.sub(r"\n(?P<blockIndent>[ ]*)if[ ]*\((?P<condition>[\S ]*)\){[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}",
#     r"\n\g<blockIndent>if \g<condition>:\n\g<body>", sourceText)
# print(sourceText)
# print(round(math.e))