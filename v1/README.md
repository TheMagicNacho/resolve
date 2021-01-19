# resolve
“””
I was originally trying to calculate for indirect fire, but there are too many variables required to resolve those trajectories.
So I decided to develop the calculations to resolve for a direct fire mission instead. It’s simpler.

Need to do more work on error handelings.

“””


Overarching Logic
Are known files present and acurate? ask user to input -jp
Are known Files present and acurate? Yes -jp

Is the system armed? No (loop for arm check again)
Is the system armed? Yes (conduct detect, resolve, attack routine)

-DETECT-
Does the system see the enemy? No (continue loop radar scan routine) -jp
Does the system see the enemy (with drone hover filter)? Yes


- RESOLVE -
Can the system calculate angle of attack? No (loop to radar scan routine)
Can the system calculate angle of attack? Yes -jp

Is the enemy within range? No (loop to radar scan routine)
Is the enemy within range? Yes -jp

Is the abort switch on? No (trigger attack routine)

- ATTACK -
Translate Angle of Attack and Azmuth inputs to fire instructions for servo, send to servo.

Do fire instructions on system match requirement? Loop translation script
Do fire instructions on system match requirement? Yes

Fire pin to “1”

~~~~~~~
~~~~~~~
~~~~~~~

INPUT (Detect and Understand)
Understand Rocket Capabilities -
0.1 - Rocket distance capability
0.2 - Attack rocket V-Max
0.3 - Attack rocket appogee
0.4 - Establish grid reference point for navigation XXX

Understand Place in Space

Understand Enemy Location and Targets


CALCULATE KINEMATICS (Resolve)
2 - Filter for drones
2.1 - If hover
2.2 - If velocity matches drone profile
2.3 - If distance

3 - Calculate trajectory for attack XXX
3.1 - Find Angle of AttackX

LOGIC

OUTPUT



References:
REF Angle:
https://www.mathsisfun.com/algebra/trig-finding-angle-right-triangle.html
https://betterexplained.com/articles/intuitive-trigonometry/

https://davidson.weizmann.ac.il/en/online/maagarmada/physics/rocket-trajectories-and-interceptions
https://betterexplained.com/articles/intuitive-trigonometry/
REF Performance:
https://www.raketenmodellbau-klima.de/Raketenmodellbau/Motoren-Treibsaetze/Motor-B4-4-6-Stueck-.htm?shop=raketenklima&SessionId=&a=article&ProdNr=0244&t=23&c=712&p=712
https://www.quora.com/What-is-the-ratio-of-max-height-to-range-of-projectile
https://www.sciencelearn.org.nz/resources/397-calculating-rocket-acceleration
http://hyperphysics.phy-astr.gsu.edu/hbase/traj.html


//// SCRATCH ////
1- Detect the Enemy Drone?
1.1 - how far away is the drone?
1.2 - what is the altitude of the drone?



rocket = {
‘title’: ‘ Klama B4-4 ‘,
‘Te’: int(5),
‘Bt’: int(1.3),
‘Mv’:  0.05 ,
‘version’: ‘ 20190318’,
}

