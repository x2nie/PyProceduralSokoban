import cs2py
# import regex
import re
import math

sourceText = """
using System;

public class Level {
    private Cell[,] map;
    private Random rand;

    public Level(int crates = 2) {
        rand = new Random();
        cratesCount = crates;
        width = rand.Next(2,4) * 3 + 2;
        height = width;
    }

    public void generate() {
        map = new Cell[width,height];
        floorCell = 0;
        //Wall generation around level
        for (int x = 0; x < width; x++) {
            map[0,x] = Cell.Wall;
            map[height-1,x] = Cell.Wall;
        }
        for (int y = 1; y < height-1; y++) {
            map[y,0] = Cell.Wall;
            map[y,width-1] = Cell.Wall;
        }
        //Template generation
    }
}
"""
print(sourceText)
print('#'*50)
translator = cs2py.CSharpToPython(useRegex=1)
# print(translator.compile(sourceText))
out = translator.compile(sourceText)
with open('output.py', 'w') as f:
    f.write(out)

# sourceText = regex.sub(r"\n(?P<blockIndent>[ ]*)if[ ]*\((?P<condition>[\S ]*)\){[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}",
#     r"\n\g<blockIndent>if \g<condition>:\n\g<body>", sourceText)
# print(sourceText)
# print(round(math.e))