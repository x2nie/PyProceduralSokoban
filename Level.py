import random
import math
import sys
from utils import *
import Cell

class Level:
    floorCell = None
    width = None
    height = None
    map = None
    cratesCount = None
    rand = None

    def __init__(self, crates = 2):
        self.rand = Random()
        self.cratesCount = crates
        self.width = self.rand.Next(2,4) * 3 + 2
        self.height = self.width

    def generate(self):
        self.map = [None for j in range(self.width,self.height)]
        self.floorCell = 0

        #Wall generation around level
        for x in range(0, self.width):
            self.map[0,x] = Cell.Wall
            self.map[self.height-1,x] = Cell.Wall

        for y in range(1, self.height-1):
            self.map[y,0] = Cell.Wall
            self.map[y,self.width-1] = Cell.Wall

        
        #Template generation
        attempt = 0
        for x in range(1, self.width-2, 3):
            for y in range(1, self.height-2, 3):
                self.randomTemplate = Templates.getRandom()
                self.randomTemplate.randomRotation()

                while self.placementAllowed(self.randomTemplate,x,y) != True:
                    self.randomTemplate = Templates.getRandom()
                    self.randomTemplate.randomRotation()
                    if attempt > 100:
                        print("Max attemp reach, self.generate again")
                        return

                    attempt += 1

                
                self.placeTemplate(self.randomTemplate, x, y)



    def spawnCrates(self, n):
        x = 0

        y = 0

        surroundWall = 0

        attempt = 0
        for i in range(0, n):
            while True:
                x = self.rand.Next(2, self.width-2)
                y = self.rand.Next(2, self.height-2)

                surroundWall = 0
                surroundWall += 1 if self.map[x-1,y] == Cell.Wall else 0
                surroundWall += 1 if self.map[x+1,y] == Cell.Wall else 0
                surroundWall += 1 if self.map[x,y-1] == Cell.Wall else 0
                surroundWall += 1 if self.map[x,y+1] == Cell.Wall else 0

                if attempt >= self.floorCell:
                    print("Can't self.generate crates ! Max attempt reach")
                    return False

                attempt += 1

                if not (self.map[x,y] != Cell.Floor or surroundWall >= 2):
                    break

            self.map[x,y] = Cell.Crate

        return True

    def spawnPlayer(self):
        x = 0

        y = 0

        attempt = 0
        while True:
            x = self.rand.Next(1, self.width-1)
            y = self.rand.Next(1, self.height-1)

            if attempt >= self.floorCell:
                print("Can't self.generate player ! Max attempt reach")
                return False

            attempt += 1

            if not (self.map[x,y] != Cell.Floor):
                break

        self.map[x,y] = Cell.Player
        return True

    def spawnGoals(self, n):
        x = 0

        y = 0

        attempt = 0
        for i in range(0, n):
            isValidGoal = False
            while True:
                x = self.rand.Next(1, self.width-1)
                y = self.rand.Next(1, self.height-1)

                if self.map[x, y+1] == Cell.Floor and self.map[x, y+2] == Cell.Floor:
                    isValidGoal = True

                elif self.map[x, y-1] == Cell.Floor and self.map[x, y-2] == Cell.Floor:
                    isValidGoal = True

                elif self.map[x+1, y] == Cell.Floor and self.map[x+2, y] == Cell.Floor:
                    isValidGoal = True

                elif self.map[x-1, y] == Cell.Floor and self.map[x-2, y] == Cell.Floor:
                    isValidGoal = True

                if attempt >= self.floorCell:
                    print("Can't self.generate goals ! Max attemp reach")
                    return False

                attempt += 1

                if not (self.map[x,y] != Cell.Floor or isValidGoal == False):
                    break

            self.map[x,y] = Cell.Goal

        return True

    def postProcess(self):
        complete = False
        self.cleanDeadCell()
        complete |= self.cleanUselessRoom()
        self.cleanAloneWall()
        self.cleanDeadCell()
        #To optimize, spawning crates mark all deadCell
        #Spawn Crate only on non deacCell
        #Need to improve deadCell algorithm too
        complete &= self.spawnCrates(self.cratesCount)
        complete &= self.spawnGoals(self.cratesCount)
        complete &= self.spawnPlayer()
        return complete

    def cleanAloneWall(self):
        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                if self.map[x,y] == Cell.Wall:
                    surroundFloor = 0
                    surroundFloor += 1 if self.map[x-1,y] == Cell.Floor else 0
                    surroundFloor += 1 if self.map[x+1,y] == Cell.Floor else 0
                    surroundFloor += 1 if self.map[x,y-1] == Cell.Floor else 0
                    surroundFloor += 1 if self.map[x,y+1] == Cell.Floor else 0
                    surroundFloor += 1 if self.map[x-1,y-1] == Cell.Floor else 0
                    surroundFloor += 1 if self.map[x+1,y-1] == Cell.Floor else 0
                    surroundFloor += 1 if self.map[x+1,y+1] == Cell.Floor else 0
                    surroundFloor += 1 if self.map[x+1,y-1] == Cell.Floor else 0

                    if surroundFloor > 6:
                        if self.rand.Next(0,100) < 30:
                            self.map[x,y] = Cell.Floor





    def cleanUselessRoom(self):
        filledFloor = 0
        attempt = 0
        x = self.rand.Next(1,self.width-1)
        y = self.rand.Next(1,self.height-1)

        while True:
            self.CellToWall(Cell.FloorFilled)
            while self.map[x,y] != Cell.Floor:
                x = self.rand.Next(1,self.width-1)
                y = self.rand.Next(1,self.height-1)
                if attempt > self.width*self.height:
                    return False

                attempt += 1

            filledFloor += self.floodFill(Cell.Floor, Cell.FloorFilled, x, y)
            if not (filledFloor < int(self).floorCell * 0.5):
                break

        for i in range(1, self.width):
            for j in range(1, self.height):
                if self.map[i,j] == Cell.Floor:
                    self.map[i,j] = Cell.Wall

                elif self.map[i,j] == Cell.FloorFilled:
                    self.map[i,j] = Cell.Floor


        return True

    def CellToWall(self, type):
        for x in range(1, self.width):
            for y in range(1, self.height):
                if self.map[x,y] == type:
                    self.map[x,y] = Cell.Wall



    def floodFill(self, target, replace, x, y):
        filledFloor = 0
        if target == replace:
            return 0; 

        elif self.map[x,y] != target:
            return 0; 

        else:
            self.map[x,y] = replace
            filledFloor += 1

        if x+1 < self.width-1:
            filledFloor += self.floodFill(target, replace, x-1, y)

        if x-1 > 0:
            filledFloor += self.floodFill(target, replace, x+1, y)

        if y+1 < self.height-1:
            filledFloor += self.floodFill(target, replace, x, y+1)

        if y-1 > 0:
            filledFloor += self.floodFill(target, replace, x, y-1)

        return filledFloor

    def cleanDeadCell(self):
        for x in range(1, self.width - 1):
            for y in range(1, self.height -1):
                if self.map[x,y] == Cell.Floor:
                    surroundWall = 0
                    surroundWall += 1 if self.map[x-1,y] == Cell.Wall else 0
                    surroundWall += 1 if self.map[x+1,y] == Cell.Wall else 0
                    surroundWall += 1 if self.map[x,y-1] == Cell.Wall else 0
                    surroundWall += 1 if self.map[x,y+1] == Cell.Wall else 0
                    if surroundWall >= 3:
                        self.map[x,y] = Cell.Wall




    def placementAllowed(self, template, x, y):
        allowed = True

        for i in range(-1, 4):
            if x+i > -1 and x+i < self.width:
                upperCellMap = self.map[x+i,y-1]
                lowerCellMap = self.map[x+i,y+3]
                if upperCellMap != Cell.Null or lowerCellMap != Cell.Null:
                    upperCell = template.GetCell(i+1,0)
                    lowerCell = template.GetCell(i+1,4)
                    
                    if upperCell != Cell.Null and lowerCell != Cell.Null:
                        if upperCell != upperCellMap or lowerCell != lowerCellMap:
                            allowed = False
                            break




        for j in range(0, 4):
            if y+j < self.height:
                leftCellMap = self.map[x-1,y+j]
                rigthCellMap = self.map[x+3,y+j]
                if leftCellMap != Cell.Null or rigthCellMap != Cell.Null:
                    leftCell = template.GetCell(0,j+1)
                    rigthCell = template.GetCell(4,j+1)
                    if leftCell != Cell.Null and rigthCell != Cell.Null:
                        if leftCell != leftCellMap or rigthCell != rigthCellMap:
                            allowed = False
                            break



        return allowed

    def placeTemplate(self, template, x, y):
        for i in range(-1, 4):
            for j in range(-1, 4):
                if x+i > 0 and y+j > 0 and x+i < self.width-1 and y+j < self.height-1:
                    cell = template.GetCell(i+1,j+1)
                    if cell != Cell.Null:
                        if cell == Cell.Floor:
                            self.floorCell += 1

                        self.map[x+i,y+j] = cell




    def print(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                match self.map[x,y]:
                    case Cell.Floor:
                        print(" ", end='')
                    case Cell.Wall:
                        print("#", end='')
                    case Cell.Crate:
                        print("$", end='')
                    case Cell.Goal:
                        print(".", end='')
                    case Cell.Player:
                        print("@", end='')

            print()


    def ToString(self):
        ret = ""
        for x in range(0, self.width):
            for y in range(0, self.height):
                match self.map[x,y]:
                    case Cell.Floor:
                        ret += " "
                    case Cell.Goal:
                        ret += "."
                    case Cell.Wall:
                        ret += "#"
                    case Cell.Player:
                        ret += "@"
                    case Cell.Crate:
                        ret += "$"

            ret += "\n"

        return ret

