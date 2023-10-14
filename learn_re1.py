# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(?P<blockIndent>[ ]+)(?P<severity>(public|private|protected)[ ]+)(?P<returnType>[^\s]+)[ ]+(?P<methodName>[\w]+)[ ]*"

test_str = ("using System;\n"
	"import Cell\n\n"
	"public class Level {\n"
	"    private int floorCell;\n"
	"    private int width;\n"
	"    private int height;\n"
	"    private Cell[,] map;\n"
	"    private int cratesCount;\n"
	"    private Random rand;\n\n"
	"    public Level(int crates = 2) {\n"
	"        rand = new Random();\n"
	"        cratesCount = crates;\n"
	"        width = rand.Next(2,4) * 3 + 2;\n"
	"        height = width;\n"
	"    }")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("     Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
