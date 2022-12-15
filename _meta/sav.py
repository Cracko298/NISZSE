from time import sleep
from os import system
from os import path
from random import randint

check0 = path.exists("Data0")
check1 = path.exists("Data1")
check2 = path.exists("Data2")

check_win = path.exists("C:\Windows\SysWOW64")
if check_win == True:
    clear = 'cls'
else:
    clear = 'clear'

if check0 == False:
    if check1 == False:
        if check2 == False:
            print("NOTICE: No Save-Data Was Found In Current Directory!")
            print("The Application Is Useless Unless Provided With Save-Data.")
            sleep(5)
            print(" ")
            print("The Application Will Now Close...")
            sleep(2)
            exit()




def Health():
    global check0
    global check1
    global check2
    global clear
    system(clear)
    print("WARNING: You Selected A Save-Data Editing Option!")
    print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
    input("Press 'Enter' To Continue. ")
    system(clear)
    print("This Program Only Accepts 4-Byte Answers (Or less).")
    print(" ")
    number = int(input("Enter An Integer for Health: "))
    byte_array = bytearray(number.to_bytes(4, byteorder='big'))
    reversed_array = byte_array[::-1]

    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(32)
            bin_file.write(reversed_array)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(32)
            bin_file.write(reversed_array)
    
    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(32)
            bin_file.write(reversed_array)
    print("Wrote Data To File(s).")
    input("Press 'Enter' To Continue. ")
    Menu()


def Water():
    global check0
    global check1
    global check2
    global clear
    system(clear)
    print("WARNING: You Selected A Save-Data Editing Option!")
    print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
    input("Press 'Enter' To Continue. ")
    system(clear)
    print("This Program Only Accepts 4-Byte Answers (Or less).")
    print(" ")
    number = int(input("Enter An Integer for Thirst: "))
    byte_array = bytearray(number.to_bytes(4, byteorder='big'))
    reversed_array = byte_array[::-1]

    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(40)
            bin_file.write(reversed_array)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(40)
            bin_file.write(reversed_array)

    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(40)
            bin_file.write(reversed_array)
    print("Wrote Data To File(s).")
    input("Press 'Enter' To Continue. ")
    Menu()


def Food():
    global check0
    global check1
    global check2
    global clear
    system(clear)
    print("WARNING: You Selected A Save-Data Editing Option!")
    print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
    input("Press 'Enter' To Continue. ")
    system(clear)
    print("This Program Only Accepts 4-Byte Answers (Or less).")
    print(" ")
    number = int(input("Enter An Integer for Hunger: "))
    byte_array = bytearray(number.to_bytes(4, byteorder='big'))
    reversed_array = byte_array[::-1]

    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(36)
            bin_file.write(reversed_array)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(36)
            bin_file.write(reversed_array)

    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(36)
            bin_file.write(reversed_array)
    print("Wrote Data To File(s).")
    input("Press 'Enter' To Continue. ")
    Menu()


def Battery():
    global check0
    global check1
    global check2
    global clear
    system(clear)
    print("WARNING: You Selected A Save-Data Editing Option!")
    print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
    input("Press 'Enter' To Continue. ")
    system(clear)
    print("This Program Only Accepts 4-Byte Answers (Or less).")
    print(" ")
    number = int(input("Enter An Integer for Battery: "))
    byte_array = bytearray(number.to_bytes(4, byteorder='big'))
    reversed_array = byte_array[::-1]

    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(48)
            bin_file.write(reversed_array)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(48)
            bin_file.write(reversed_array)

    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(48)
            bin_file.write(reversed_array)
    print("Wrote Data To File(s).")
    input("Press 'Enter' To Continue. ")
    Menu()


def Greybase():
    global clear
    system(clear)
    byt = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4'
    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)

    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)
    print("Wrote Coordinates To File(s).")
    input("Press 'Enter' To Continue. ")
    LocationMenu()

def oilRig():
    global clear
    system(clear)
    byt = b'\x4A\x42\xC7\x79\xE8\x41\xCE\xA7\x35\xC5'
    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)

    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)
    print("Wrote Coordinates To File(s).")
    input("Press 'Enter' To Continue. ")
    LocationMenu()


def Submarine():
    global clear
    system(clear)
    byt = b'\x09\x44\x37\x1A\x84\x40\x1D\xC0\xD1\xC4'
    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)

    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)
    print("Wrote Coordinates To File(s).")
    input("Press 'Enter' To Continue. ")
    LocationMenu()


def FixOpen():
    global clear
    system(clear)
    byt = b'\x01\x00\x00\x00'
    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(00)
            bin_file.write(byt)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(00)
            bin_file.write(byt)

    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(00)
            bin_file.write(byt)
    print("Wrote Data Fix To File(s).")
    input("Press 'Enter' To Continue. ")
    FixMenu()

def SpawnFix():
    global clear
    system(clear)
    byt = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4'
    if check0 == True:
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)

    if check1 == True:
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)

    if check2 == True:
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(22)
            bin_file.write(byt)
    print("Wrote Non-Broken Coordinates To File(s).")
    input("Press 'Enter' To Continue. ")
    FixMenu()

def FixCloth():
    global clear
    system(clear)
    if check0 == True:
        byt = b'\x00\x00\x00\x00'
        with open('Data0', 'rb+') as bin_file:
            bin_file.seek(52)
            bin_file.write(byt)
            byt = b'\x01\x00\x00\x00'
            bin_file.seek(56)
            bin_file.write(byt)
            byt = b'\x02\x00\x00\x00'
            bin_file.seek(60)
            bin_file.write(byt)

    if check1 == True:
        byt = b'\x00\x00\x00\x00'
        with open('Data1', 'rb+') as bin_file:
            bin_file.seek(52)
            bin_file.write(byt)
            byt = b'\x01\x00\x00\x00'
            bin_file.seek(56)
            bin_file.write(byt)
            byt = b'\x02\x00\x00\x00'
            bin_file.seek(60)
            bin_file.write(byt)

    if check2 == True:
        byt = b'\x00\x00\x00\x00'
        with open('Data2', 'rb+') as bin_file:
            bin_file.seek(52)
            bin_file.write(byt)
            byt = b'\x01\x00\x00\x00'
            bin_file.seek(56)
            bin_file.write(byt)
            byt = b'\x02\x00\x00\x00'
            bin_file.seek(60)
            bin_file.write(byt)
    print("Wrote Clothing Data To File(s).")
    input("Press 'Enter' To Continue. ")
    FixMenu()












































































def ClothMenu():
    global clear
    system(clear)
    print("Clothing/Apparel Menu (v1.0)")
    print(" ")











def notDeveloped():
    global clear
    system(clear)
    print("NOTICE: This Version of The ISZ-Save-Editor Does Not Include This Feature.")
    print("However You Will Be Able To Access It Soon, Possibly After The Next Update.")
    print(" ")
    input("Press The 'Enter' Key To Return To Main-Menu. ")
    Menu()



def FixMenu():
    global clear
    subsys = [1,2,3,4]
    system(clear)
    print("Save Fixer Menu (v1.3)")
    print(" ")
    print("1 = Fix Spawn Point")
    print("2 = Fix Open-Sector Data")
    print("3 = Fix Clothing/Apparel")
    print("4 = Return To Main-Menu")
    print(" ")
    useri = int(input("Select Choice: "))
    
    if useri == 4:
        Menu()
    
    if useri == 2:
        FixOpen()
    
    if useri == 1:
        SpawnFix()
    
    if useri == 3:
        FixCloth()

    if useri not in subsys:
        FixMenu()







def LocationMenu():
    global clear
    system(clear)
    subsys = [1,2,3,4]
    print("Location Menu (v1.0)")
    print(" ")
    print("1 = Greybase Spawn-Point")
    print("2 = Oil-Rig Spawn Point")
    print("3 = Submarine Spawn Point")
    print("4 = Return To Main-Menu")
    print(" ")
    useri = int(input("Select Choice: "))

    if useri not in subsys:
        LocationMenu()

    if useri == 1:
        Greybase()

    if useri == 2:
        oilRig()
    
    if useri == 3:
        Submarine()

    if useri == 4:
        Menu()

def notic():
    global clear
    system(clear)
    print("WARNING: You Selected A Coordinate Editing Option!")
    print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
    input("Press 'Enter' To Continue. ")
    LocationMenu()




def notice():
    global clear
    system(clear)
    print("NOTICE: The Save-Fixer Function Does NOT Guarentee That Your Save-Data Files Will Be Fixed.")
    print("It Will Attempt To Fix It As Best It Can Using The Edits It Provides.")
    print(" ")
    print("NOTE: It's Always Advised To Get A Full Understanding of A Save-File Before Editing It Manually.")
    print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
    print(" ")
    input("Press 'Enter' To Continue. ")
    FixMenu()
    














def Menu():
    spectrum0 = [1,2,3,4,5,6,7]
    system(clear)
    print("Ice Station Z Save Editor + Fixer (Console Window)")
    print("Press 1-6 To Select Your Options. (And Then Hit 'Enter')")
    print(" ")
    print("1 = Edit Health")
    print("2 = Edit Thirst")
    print("3 = Edit Hunger")
    print("4 = Edit Battery")
    print(" ")
    print("5 = Save Fixer Menu (v1.3)")
    print("6 = Clothing/Apparel Menu (v1.1)")
    print("7 = Location Selector Menu (v1.0)")
    print(" ")
    user_i = int(input("Selected Choice: "))

    if user_i not in spectrum0:
        Menu()

    if user_i == 1:
        Health()
    
    if user_i == 2:
        Water()
    
    if user_i == 3:
        Food()
    
    if user_i == 4:
        Battery()

    if user_i == 7:
        notic()

    if user_i == 5:
        notice()

    if user_i == 6:
        notDeveloped()
Menu()