from time import sleep
from os import system
from os import path

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
  print(
    "This Function Will Edit All Save-Data Files Found In The Currect Directory."
  )
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
  print(
    "This Function Will Edit All Save-Data Files Found In The Currect Directory."
  )
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
  print(
    "This Function Will Edit All Save-Data Files Found In The Currect Directory."
  )
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
  print(
    "This Function Will Edit All Save-Data Files Found In The Currect Directory."
  )
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Answers (Or less).")
  print(" ")
  number = int(input("Enter An Integer for Battery: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Menu()


def Greybase():
  global clear
  global check0
  global check1
  global check2
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
  global check0
  global check1
  global check2
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
  global check0
  global check1
  global check2
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
  global check0
  global check1
  global check2
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
  global check0
  global check1
  global check2
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
  global check0
  global check1
  global check2
  system(clear)
  if check0 == True:
    byt = b'\x01\x00\x00\x00'
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      byt = b'\x00\x00\x00\x00'
      bin_file.seek(52)
      bin_file.write(byt)
      byt = b'\x02\x00\x00\x00'
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    byt = b'\x01\x00\x00\x00'
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      byt = b'\x00\x00\x00\x00'
      bin_file.seek(52)
      bin_file.write(byt)
      byt = b'\x02\x00\x00\x00'
      bin_file.seek(60)
      bin_file.write(byt)

  if check2 == True:
    byt = b'\x01\x00\x00\x00'
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      byt = b'\x00\x00\x00\x00'
      bin_file.seek(52)
      bin_file.write(byt)
      byt = b'\x02\x00\x00\x00'
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  FixMenu()













def Jacket1():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x04\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Jacket()

def Jacket2():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x00\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Jacket()

def Jacket3():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x06\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Jacket()

def Jacket4():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x05\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Jacket()

def Jacket5():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x07\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Jacket()

def Jacket6():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x03\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(52)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Jacket()

















def Backpack1():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x04\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Backpack()

def Backpack2():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x02\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Backpack()

def Backpack3():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x06\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Backpack()

def Backpack4():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x05\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Backpack()

def Backpack5():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x07\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Backpack()

def Backpack6():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x03\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Backpack()













































def Hack0():
  global clear
  system(clear)
  global check0
  global check1
  global check2


def Hack1():
  global clear
  system(clear)
  global check0
  global check1
  global check2


def Hack2():
  global clear
  system(clear)
  global check0
  global check1
  global check2


def Hack3():
  global clear
  system(clear)
  global check0
  global check1
  global check2


def Hack4():
  global clear
  system(clear)
  global check0
  global check1
  global check2
























def Trousers1():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x04\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Trousers()

def Trousers2():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x01\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Trousers()

def Trousers3():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x06\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Trousers()

def Trousers4():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x05\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Trousers()

def Trousers5():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x07\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Trousers()

def Trousers6():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  byt = b'\x03\x00\x00\x00'
  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)

  if check1 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  Trousers()





























def HackedClothes():  # THE HACKED CLOTHES ARE NOT FINISHED.
  global clear
  subsys = [1, 2, 3, 4, 5, 6]
  system(clear)
  print("Hacked Clothing/Apparel Menu (v1.0 - Hacked)")
  print(" ")
  print("1 = Beige Clothes")
  print("2 = Black CLothes")
  print("3 = Brown Clothes")
  print("4 = Green Clothes")
  print("5 = Red Clothes")
  print("6 = Retun To Menu")
  print(" ")
  useri = int(input("Select Choice: "))

  if useri not in subsys:
    HackedClothes()

  if useri == 6:
    ClothMenu()

  if useri == 1:
    Hack0()

  if useri == 2:
    Hack1()

  if useri == 3:
    Hack2()

  if useri == 4:
    Hack3()

  if useri == 5:
    Hack4()


def notava():
  system(clear)
  print("NOTICE: This Menu is Under Construction!")
  print("Should Be Avaliable In The Next Update!")
  print(' ')
  input("Press 'Any' Key To Return To Menu.")
  Menu()

























def Backpack():
  global clear
  subsys = [1, 2, 3, 4, 5, 6, 7]
  system(clear)
  print("Clothing/Apparel Menu (v1.0 - Backpack)")
  print(" ")
  print("1 = Military Backpack")
  print("2 = Defualt Backpack")
  print("3 = Arctic Backpack")
  print("4 = Kvlar Backpack")
  print("5 = Bling Backpack")
  print("6 = Camo Backpack")
  print("7 = Return To Menu")
  print(" ")
  useri = int(input("Select Choice: "))

  if useri not in subsys:
    Backpack()

  if useri == 7:
    ClothMenu()

  if useri == 6:
    Backpack6()
  
  if useri == 5:
    Backpack5()

  if useri == 4:
    Backpack4()

  if useri == 3:
    Backpack3()

  if useri == 2:
    Backpack2()

  if useri == 1:
    Backpack1()


def Trousers():
  global clear
  subsys = [1, 2, 3, 4, 5, 6, 7]
  system(clear)
  print("Clothing/Apparel Menu (v1.0 - Trousers)")
  print(" ")
  print("1 = Military Trousers")
  print("2 = Defualt Trousers")
  print("3 = Arctic Trousers")
  print("4 = Kvlar Trousers")
  print("5 = Bling Trousers")
  print("6 = Camo Trousers")
  print("7 = Return To Menu")
  print(" ")
  useri = int(input("Select Choice: "))

  if useri not in subsys:
    Trousers()

  if useri == 7:
    ClothMenu()

  if useri == 6:
    Trousers6()
  
  if useri == 5:
    Trousers5()

  if useri == 4:
    Trousers4()

  if useri == 3:
    Trousers3()

  if useri == 2:
    Trousers2()

  if useri == 1:
    Trousers1()


def Jacket():
  global clear
  subsys = [1, 2, 3, 4, 5, 6, 7]
  system(clear)
  print("Clothing/Apparel Menu (v1.0 - Jackets)")
  print(" ")
  print("1 = Military Jacket")
  print("2 = Defualt Jacket")
  print("3 = Arctic Jacket")
  print("4 = Kvlar Jacket")
  print("5 = Bling Jacket")
  print("6 = Camo Jacket")
  print("7 = Return To Menu")
  print(" ")
  useri = int(input("Select Choice: "))

  if useri not in subsys:
    Jacket()

  if useri == 7:
    ClothMenu()

  if useri == 6:
    Jacket6()
  
  if useri == 5:
    Jacket5()

  if useri == 4:
    Jacket4()

  if useri == 3:
    Jacket3()

  if useri == 2:
    Jacket2()

  if useri == 1:
    Jacket1()


def ClothMenu():
  subsys = [1, 2, 3, 4, 5]
  global clear
  system(clear)
  print("Clothing/Apparel Menu (v1.0)")
  print(" ")
  print("1 = Edit Jacket")
  print("2 = Edit Trousers")
  print("3 = Edit Backpack")
  print("4 = Hacked Clothes Menu")
  print("5 = Return To Menu")
  print(" ")
  useri = int(input("Select Choice: "))

  if useri not in subsys:
    ClothMenu()

  if useri == 1:
    Jacket()

  if useri == 2:
    Trousers()

  if useri == 3:
    Backpack()

  if useri == 5:
    Menu()

  if useri == 4:
    notava()



def notDeveloped():
  global clear
  system(clear)
  print("WARNING: You Selected A Clothes Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  ClothMenu()


def FixMenu():
  global clear
  subsys = [1, 2, 3, 4]
  system(clear)
  print("Save Fixer Menu (v1.3)")
  print(" ")
  print("1 = Fix Spawn Point")
  print("2 = Fix Open-Sector Data")
  print("3 = Fix Clothing/Apparel")
  print("4 = Return To Menu")
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
  subsys = [1, 2, 3, 4]
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
  print("WARNING: You Selected A Coordinates Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  LocationMenu()


def notice():
  global clear
  system(clear)
  print(
    "NOTICE: The Save-Fixer Function Does NOT Guarentee That Your Save-Data Files Will Be Fixed."
  )
  print(
    "It Will Attempt To Fix It As Best It Can Using The Edits It Provides.")
  print(" ")
  print(
    "NOTE: It's Always Advised To Get A Full Understanding of A Save-File Before Editing It Manually."
  )
  print(
    "This Function Will Edit All Save-Data Files Found In The Currect Directory."
  )
  print(" ")
  input("Press 'Enter' To Continue. ")
  FixMenu()


def Menu2():
  spectrum0 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
  system(clear)
  print("Ice Station Z Save Editor + Fixer (Console Window)")
  print("Press 1-6 To Select Your Options. (And Then Hit 'Enter')")
  print(" ")
  print("1 = Edit Health")
  print("2 = Edit Thirst")
  print("3 = Edit Hunger")
  print("4 = Edit Battery")
  print("5 = Edit Days Survived")
  print("6 = Edit Modified Date")
  print(" ")
  print("7 = Fitness Menu (v1.0)")
  print("8 = Active Slots Menu (v1.4)")
  print("0 = Previous Page (Current Page '2/2')")
  print(" ")
  user_u = int(input("Selected Choice: "))

  if user_u == 0:
    Menu()

  if user_u not in spectrum0:
    Menu2()

  if user_u == 1:
    Health()

  if user_u == 2:
    Water()

  if user_u == 3:
    Food()

  if user_u == 4:
    Battery()














def Menu2Warn():
    system(clear)
    print('NOTICE: This Menu Is Not Finished.')
    print('This new menu will include new features!')
    print('Come Back Soon ;)')
    print(" ")
    input("Press 'Any' Key To Return To Menu.")
    Menu()




















def Menu():
  spectrum0 = [1, 2, 3, 4, 5, 6, 7, 0]
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
  print("0 = Next Page (Current Page '1/2')")
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

  if user_i == 0:
    Menu2Warn()


def Load():
  sleep(1)
  print("Created By:  r       ")
  sleep(0.15)
  system(clear)
  print("Created By:  r c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c    8")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o298")
  sleep(0.15)
  system(clear)
  print("Created By: Cracko298")
  sleep(4)
  system(clear)
  Menu()


Load()