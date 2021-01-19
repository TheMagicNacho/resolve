import knowns as k
import angle as a
import os.path
import time

#user must validate version
def user_knowns():
    try:
        Te = input("What is the engines' thrust in Newtons? ")
    except:
        print ("boo - resart validate loop - Error Code: Write_knowns Te")
        knowns_exist()
    try:
        Bt = input("What is the Engines' burn time in seconds? ")
    except ValueError:
        print("boo - resart validate loop - Error Code:  Write_knowns Bt")
        knowns_exist()
    try:
        Mv = input("What is the Mass of the Vehicle in Kilograms? ")
    except ValueError:
        print("boo - resart validate loop - Error Code:  Write_knowns Mv")
        knowns_exist()
    try:
        title = input("What is the Rockets' nomenclature? ")
    except ValueError:
        print("boo - resart validate loop - Error Code:  Write_knowns Nomenclature")
        knowns_exist()
    try:
        version = input("What is your versioning id? ")
    except:
        print("boo - resart validate loop - Error Code:  Write_knowns Version")
        knowns_exist()
    # OUTPUTS
    # Write file re-validate
    f = open("knowns.py", "w")
    f.write("rocket = {" +"\n")
    f.write("'title': ' " + title + " '," +"\n")
    f.write("'Te': int(" + Te + ")," + "\n")
    f.write("'Bt': int(" + Bt + ")," + "\n")
    f.write("'Mv':  " + Mv + " ," + "\n")
    f.write("'version': ' " + version + "'," + "\n")
    f.write("}")
    f.close()
    print("\n")
    print("SUCESS:  Knowns File Written")
    time.sleep(1)
    display_knowns()

# does path exist?
def knowns_exist():
    if os.path.exists('knowns.py')==True and os.path.getsize('knowns.py')>83:
        print("VALIDATE KNOWS DATA:  pass")
        print("\n")
        check_knowns_version()
    else:
        print("VALIDATE KNOWS DATA: fail- Rocket knowns is missing. \n Please fill out knowns")
        user_knowns()

def check_knowns_version():
    print("TITLE: ", k.rocket['title'])
    print("VERSION: ", k.rocket['version'])
    verify_version = input("Is this the correct information for friendly ballistics? ['y' for yes]? ")
    print("\n")
    if verify_version == 'y':
        print("Initiate Primary Resolve Loop")
    else:
        print("Please define known rocket values.")
        user_knowns()

def display_knowns():
    #for x in k.rocket:
    #    print(k.rocket[x])
    save = input("Type 'y' to save. All else restarts dictionary.")
    if save == 'y': print("Knowns Dictionary Saved \n")
    else: user_knowns()

# INPUT
# VALIDATE IMPORTS ARE WORKING
# if knowns = digit print good
class validate_data():
    if k.rocket['Te'] > 0.00001: print("VALIDATE PRESENCE OF KNOWS FILE:  pass")
    else:
        print("ERROR: Rocket knowns data missing.")
        user_knowns()
# if angle = digit print good
    if a.eny_x < 0: print("ERROR: Enemy inputs produce negative on X access.")
    else:
    #pull functions
        knowns_exist()
