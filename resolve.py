import math
import rmax
import eny as e

def eny_range():
    k =  math.sqrt( e.pos['x']**2 + e.pos['y']**2 )
    pos = k

    if rmax.range.direct_fire > pos:
        print ("FIRE:", pos)
        exit()
    else:
        print("loop back", pos)