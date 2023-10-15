# import random
# import math
# import sys
from Level import Level

class Program:
    def Main(self, *args):
        level = Level()

        level.generate()
        level.print()
        print()

        level.postProcess()
        level.print()

        #export()

    def export(self):
        for i in range(0, 10):
            level = Level()
            level.generate()
            complete = level.postProcess()

            while complete != True:
                level.generate()
                complete = level.postProcess()

            path = "./exports/" + i.ToString() + ".txt"; 
            try:
                # Create the file, overwrite if the file exists.
                with open(path, 'w') as fs:
                    info = UTF8Encoding(True).GetBytes(level.ToString())
                    # Add some information to the file.
                    fs.Write(info, 0, info.Length)

                print("Level " + i.ToString() + " exported.")
            
            except Exception as ex:
                print(str(ex))
            


