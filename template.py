from utils import *

class Template:
    template = None

    def __init__(self, content):
        self.template = [[] for j in range(len(content))]

        for x in range(0, len(content)):
            newer = [None for j in range(len(content[x]))]
            ArrayCopy(content[x], newer, len(content[x]))
            self.template[x] = newer


    def GetCell(self, x, y):
        return self.template[x][y]; 

    def randomRotation(self):
        r = Random()
        for i in range(0, r.Next(5)):
            self.rotate()


    def clockwiseRotation(self, n):
        for i in range(0, n):
            self.rotate()


    def rotate(self):
        width = len(self.template)
        heigth = len(self.template[0])
        # Array transposition
        for y in range(0, heigth):
            for x in range(y, width):
                tmpCell = self.template[y][x]
                self.template[y][x] = self.template[x][y]
                self.template[x][y] = tmpCell


        # Reverse each row
        for y in range(0, heigth):
            for x in range(0, width/2):
                tmpCell = self.template[y][x]
                self.template[y][x] = self.template[y][width-1-x]
                self.template[y][width-1-x] = tmpCell



