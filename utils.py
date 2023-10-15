import copy
import random

def ArrayCopy(src, dst, count):
    # https://learn.microsoft.com/en-us/dotnet/api/system.array.copy?view=net-7.0
    for i in range(count):
        dst[i] = copy.copy(src[i])



class Random():
    def Next(self, a, b=None):
        if b is None:
            return random.randrange(a)
        return random.randrange(a, b)