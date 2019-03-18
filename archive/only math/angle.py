"""
This script will resolve the angle of attack for a direct fire mission of a rocket to an ENY location.
All units are in metric, except for the degree translation

REF:
https://www.mathsisfun.com/algebra/trig-finding-angle-right-triangle.html
https://betterexplained.com/articles/intuitive-trigonometry/

"""
# Import required libraries
import math as m

# Input
# ENY Location
eny_x = int(5) #constant for development / X displacement for Range or distance from Launcher
eny_y = int(3) #constant for developmeny / Y displacement for Altitude or Above Ground Level Height

# Calculate
# Angle of Attack
rad = m.atan(eny_y / eny_x)
deg = m.degrees(attack_rad)

# Output
# Print Angle of Attack
print ("Angle of Attack (rad): ", attack_rad)
print ("Angle of Attack (deg): ", attack_deg)
