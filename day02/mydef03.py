from random import random
def myRandom():
    rnd = random()
    if rnd > 0.5:
        return 1
    else:
        return 0
    
rnd = myRandom()
print(rnd)