import angle
import knowns as k
import validator
import rmax
import resolve

print("MAIN SCRIPT:  open")

validator.validate_data()
print ("VALIDATION:  pass")

print ("engine type: ", k.rocket['title'])

def main():
    while True:
        main_loop()

def main_loop():
    angle.angle_print()
    print("Imported Angle of Attack (rad): ", angle.attack_angle.rad)
    angle.angle_errors()

    rmax.rprint()
    print("Max Range of rocket: ", rmax.range.direct_fire)
    resolve.eny_range()

if __name__ == '__main__': main()
