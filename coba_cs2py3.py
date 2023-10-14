import cs2py
# import regex
import re
import math

sourceText = """
using System;

//?halo moto
if (0==1){
    int a = 0;
    bool d = true; int asd = 5; string asd1 = "hello world";
    if (1){
        Console.WriteLine("lol");
        Console.Write("ban");
    }
    while (true){
        if (1){
            a = 0;
        }
        else if (2){
            a = 0; // here is comment
        }
        else{
            a = 0;
            float b = Math.Cos(25) * Math.PI;
            int c = new Random().Next(0, 1000);
            double t = new Random().NextDouble();
            if (!(true || false && 1)) { }
        }
        for (int i = 0; i < 5; i+=1){
            Console.WriteLine(i);
            foreach (var lol in customArray){
                var l = 0;
                if (true){ }
            }
        }
    }
}
interface ITest{
    /* test interface.*/
    void test();
}
class CTest{
    void test2();
}

public class PublicClass {
    private Random rand;
    private Cell[,] map;
    private int floorCell;
    private int width;
    private int height;
    // private Cell[,] map;
    private int cratesCount;
    private Random rand;


    public void Level(int crates = 2) {
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
        //Template generation
    }
    public override string ToString()
    {
        string ret = "";
        for(int x = 0; x < width; x++) {
            for(int y = 0; y < height; y++) {
                switch(map[x,y]) {
                    case Cell.Floor:
                        ret += " ";
                        break;
                    case Cell.Goal:
                        ret += ".";
                        break;
                    case Cell.Wall:
                        ret += "#";
                        break;
                    case Cell.Player:
                        ret += "@";
                        break;
                    case Cell.Crate:
                        ret += "$";
                        break;
                    default:
                        break;
                }
            }
            ret += "\\n";
        }
        return ret;
    }
    for (int y = 1; y < height-1; y++){
        a++7
    }
}
int[] a = {1, 2, 3, 4};

"""
translator = cs2py.CSharpToPython(useRegex=0)
# print(translator.compile(sourceText))
out = translator.compile(sourceText)
with open('output.py', 'w') as f:
    f.write(out)
# sourceText = regex.sub(r"\n(?P<blockIndent>[ ]*)if[ ]*\((?P<condition>[\S ]*)\){[\r\n]+(?P<body>(?P<indent>[ ]*)[^\r\n]+[\r\n]+((?P=indent)[^\r\n]+[\r\n]+)*)(?P=blockIndent)}",
#     r"\n\g<blockIndent>if \g<condition>:\n\g<body>", sourceText)
# print(sourceText)
# print(round(math.e))