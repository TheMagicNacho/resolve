"""
This script will resolve the angle of attack for a direct fire mission of a rocket to an ENY location.
All units are in metric, except for the degree translation

REF:
https://www.mathsisfun.com/algebra/trig-finding-angle-right-triangle.html
https://betterexplained.com/articles/intuitive-trigonometry/

"""
# Import required libraries
# from colorama import Fore, Back, Style
import math as m
import eny as e

# Input
# ENY Location
try:
    eny_x = float ( e.pos['x'] ) #constant for development / X displacement for Range or distance from Launcher
except:
    print("Enemy DISTANCE not properly defined-- In the future create loop function")
try:
    eny_y = float ( e.pos['y'] )  # constant for developmeny / Y displacement for Altitude or Above Ground Level Height
except:
    print("Enemy ALTITUDE not properly defined-- In the future create loop function")

# Calculate
# Angle of Attack
class attack_angle():
    rad = m.atan( eny_y / eny_x )
    deg = m.degrees(rad)

    #detect errors
def angle_errors():
    if attack_angle.rad < 0.00000001:  print("Radar Erorr = Enemy input is a negative number")
    else: print("Angle of Attack Values Positive")

# Output
# Print Angle of Attack
def angle_print():
    print("~ANGLE SCRIPT~")
    print ("Angle of Attack (rad): ", attack_angle.rad)
    print ("Angle of Attack (deg): ", attack_angle.deg)
    print("Angle of Attack Resolved From Angle Script")
