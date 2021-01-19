import cmath

Teny = 32 #made up number in meters. Pretend that this data comes from radar
Deny = 45 #made up number in deg.

Aeny = cmath.cos(Teny) * Deny #trig to find enemy AGL

print(Aeny)