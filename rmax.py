"""
https://pypi.org/project/colorama/

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
"""
# Import required libraries
import math
from scipy import constants as sp
import angle as ang
import knowns as k
import eny as e

# Calculate with Kenematics
class physics():
    Wv = k.rocket['Mv']  * sp.g  # Weight in Kg after acceleration of gravity
    Fr = k.rocket['Te'] - Wv   # Force, Resultant
    Ar = Fr / float(k.rocket['Mv'])   # Acceleration (M/S)^2
    Vo = Ar * k.rocket['Bt']   # Velocity of Object after burn

class ymax:
    time = physics.Vo / sp.g
    m = time * physics.Vo
class range:
    idf = (physics.Vo**2 * math.sin(2 * ang.attack_angle.rad)) / sp.g
    # THIS ONE WORKS:  idf = (physics.Vo * physics.Vo * math.sin(2 * ang.attack_angle.deg * math.pi / 180)) / sp.g
    direct_fire = idf / 2


def rprint():
    print("~RMAX SCRIPT~")
    print ("Max Range Direct Fires Mission: ", range.direct_fire)
    print("Max Y displacement: ", ymax.m)
    print("Max Capabilities Resolved From rmax Script")
