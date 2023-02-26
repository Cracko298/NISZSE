from time import sleep
from os import system
from os import path
from glob import glob
import codecs
from slots import slotsFind
from slots import slotsID
from slots import slotsEdit

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


if glob('*.ISplg'):
  print("NISZSE Detected an .ISplg Plugin File in Current Directory.")
  print("Type The 'File Name' Below to Load It.")
  print(" ")
  decent = input("File Name: ")

  if ".ISplg" in decent:
    print(" ")
  else:
    print(" ")
    decent = decent + ".ISplg"

  with open(decent,'r') as binFile0:
    creator_load = binFile0.readline().rstrip()
    loader0 = binFile0.readline().rstrip()

    if "1" in loader0:
      seek1_load = binFile0.readline().rstrip()
      data1_load = binFile0.readline().rstrip()
      notes_load = binFile0.readline().rstrip()
      creator_final = codecs.decode(creator_load,'rot_13')
      notes_final = codecs.decode(notes_load,'rot_13')
      
      int0 = int(''.join(filter(str.isdigit, seek1_load)))
      int0 = int0 - 32

      int1 = int(''.join(filter(str.isdigit, data1_load)))
      int1 = int1 - 32


      print(f"Plugin Loaded: '{decent}'.")
      sleep(1)
      system(clear)
      print(f"Plugin Created By: {creator_final}.")
      
      if "." in notes_final:
        print(f"Plugin Note: {notes_final}")
      else:
        print(f"Plugin Note: {notes_final}.")

      print(" ")
      print(f"Plugin File Mode: {loader0}.")
      print(f"File Seeks Bytes: {int0}.")
      print(f"Bytes Changed To: {int1}.")
      print(" ")
      input("Press the 'Enter' Key To Continue.")
        
      if check0 == True:
        with open("Data0",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)

      if check1 == True:
        with open("Data1",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)

      if check2 == True:
        with open("Data2",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)
      

    if "2" in loader0:
      seek1_load = binFile0.readline().rstrip()
      data1_load = binFile0.readline().rstrip()
      seek2_load = binFile0.readline().rstrip()
      data2_load = binFile0.readline().rstrip()
      notes_load = binFile0.readline().rstrip()
      creator_final = codecs.decode(creator_load,'rot_13')
      notes_final = codecs.decode(notes_load,'rot_13')
      
      int0 = int(''.join(filter(str.isdigit, seek1_load)))
      int0 = int0 - 32

      int1 = int(''.join(filter(str.isdigit, data1_load)))
      int1 = int1 - 32

      int2 = int(''.join(filter(str.isdigit, seek2_load)))
      int2 = int2 - 32

      int3 = int(''.join(filter(str.isdigit, data2_load)))
      int3 = int3 - 32
      print(f"Plugin Loaded: '{decent}'.")
      sleep(1)
      system(clear)
      print(f"Plugin Created By: {creator_final}.")
      
      if "." in notes_final:
        print(f"Plugin Note: {notes_final}")
      else:
        print(f"Plugin Note: {notes_final}.")

      print(" ")
      print(f"Plugin File Mode: {loader0}.")
      print(f"File Seeks Bytes: {int0}, {int2}.")
      print(f"Bytes Changed To: {int1}. {int3}.")
      print(" ")
      input("Press the 'Enter' Key To Continue.")
        
      if check0 == True:
        with open("Data0",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int3.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int2)
          binaryFile1.write(reversed_array)

      if check1 == True:
        with open("Data1",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int3.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int2)
          binaryFile1.write(reversed_array)

      if check2 == True:
        with open("Data2",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int3.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int2)
          binaryFile1.write(reversed_array)

    if "3" in loader0:
      seek1_load = binFile0.readline().rstrip()
      data1_load = binFile0.readline().rstrip()
      seek2_load = binFile0.readline().rstrip()
      data2_load = binFile0.readline().rstrip()
      seek3_load = binFile0.readline().rstrip()
      data3_load = binFile0.readline().rstrip()
      notes_load = binFile0.readline().rstrip()
      
      creator_final = codecs.decode(creator_load,'rot_13')
      notes_final = codecs.decode(notes_load,'rot_13')
      
      int0 = int(''.join(filter(str.isdigit, seek1_load)))
      int0 = int0 - 32

      int1 = int(''.join(filter(str.isdigit, data1_load)))
      int1 = int1 - 32

      int2 = int(''.join(filter(str.isdigit, seek2_load)))
      int2 = int2 - 32

      int3 = int(''.join(filter(str.isdigit, data2_load)))
      int3 = int3 - 32

      int4 = int(''.join(filter(str.isdigit, seek3_load)))
      int4 = int4 - 32

      int5 = int(''.join(filter(str.isdigit, data3_load)))
      int5 = int5 - 32
      print(f"Plugin Loaded: '{decent}'.")
      sleep(1)
      system(clear)
      print(f"Plugin Created By: {creator_final}.")
      
      if "." in notes_final:
        print(f"Plugin Note: {notes_final}")
      else:
        print(f"Plugin Note: {notes_final}.")

      print(" ")
      print(f"Plugin File Mode: {loader0}.")
      print(f"File Seeks Bytes: {int0}, {int2}, {int4}.")
      print(f"Bytes Changed To: {int1}. {int3}, {int5}.")
      print(" ")
      input("Press the 'Enter' Key To Continue.")
        
      if check0 == True:
        with open("Data0",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int3.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int2)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int5.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int4)
          binaryFile1.write(reversed_array)

      if check1 == True:
        with open("Data1",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int3.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int2)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int5.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int4)
          binaryFile1.write(reversed_array)

      if check2 == True:
        with open("Data2",'rb+') as binaryFile1:
          byte_array = bytearray(int1.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int0)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int3.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int2)
          binaryFile1.write(reversed_array)
          
          byte_array = bytearray(int5.to_bytes(4, byteorder='big'))
          reversed_array = byte_array[::-1]
          binaryFile1.seek(int4)
          binaryFile1.write(reversed_array)
          
    sleep(2)
    system(clear)
    print("Plugin Wrote Patch to File.")
    print("Continuing to NISZSE...")
    sleep(4)






slotsFind()
slotsID()
slotsEdit()
system(clear)

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
  print("This Program Only Accepts 4-Byte Integers (Or less).")
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
  print("This Program Only Accepts 4-Byte Integers (Or less).")
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
  print("This Program Only Accepts 4-Byte Integers (Or less).")
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
  print("This Program Only Accepts 4-Byte Integers (Or less).")
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


def Hack0():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  system(clear)
  if check0 == True:
    byt = b'\x0F\x00\x00\x00'
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    byt = b'\x0F\x00\x00\x00'
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
    

  if check2 == True:
    byt = b'\x0F\x00\x00\x00'
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  HackedClothes()













def Hack1():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  system(clear)
  if check0 == True:
    byt = b'\x01\x00\x00\x00'
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    byt = b'\x01\x00\x00\x00'
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
    

  if check2 == True:
    byt = b'\x01\x00\x00\x00'
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  HackedClothes()













def Hack2():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  system(clear)
  if check0 == True:
    byt = b'\x0A\x00\x00\x00'
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    byt = b'\x0A\x00\x00\x00'
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
    

  if check2 == True:
    byt = b'\x0A\x00\x00\x00'
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  HackedClothes()








def Hack3():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  system(clear)
  if check0 == True:
    byt = b'\x00\x00\x00\x00'
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    byt = b'\x00\x00\x00\x00'
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
    

  if check2 == True:
    byt = b'\x00\x00\x00\x00'
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  HackedClothes()










def Hack4():
  global clear
  system(clear)
  global check0
  global check1
  global check2
  system(clear)
  if check0 == True:
    byt = b'\x0B\x00\x00\x00'
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)

  if check1 == True:
    byt = b'\x0B\x00\x00\x00'
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
    

  if check2 == True:
    byt = b'\x0B\x00\x00\x00'
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(56)
      bin_file.write(byt)
      bin_file.seek(52)
      bin_file.write(byt)
      bin_file.seek(60)
      bin_file.write(byt)
  print("Wrote Clothing Data To File(s).")
  input("Press 'Enter' To Continue. ")
  HackedClothes()





















































def HackedClothes():  # THE HACKED CLOTHES ARE NOT FINISHED.
  global clear
  subsys = [1, 2, 3, 4, 5, 6]
  system(clear)
  print("Hacked Clothing/Apparel Menu (v1.0 - Hacked)")
  print(" ")
  print("1 = Orange Clothes")
  print("2 = Black CLothes")
  print("3 = Brown Clothes")
  print("4 = Red Clothes")
  print("5 = Grey Clothes")
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
  print("WARNING: Hacked Clothes Do 'NOT' Give Stats.")
  print("The Game 'WILL' Treat these Clothes as The 'Defualt Clothes'.")
  print(' ')
  input("Press The 'Enter' Key To Continue.")
  HackedClothes()



def plyrKill():
  global check0
  global check1
  global check2
  global clear
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Integers (Max Player Kills is 99).")
  print(" ")
  number = int(input("Enter An Integer for Player Kills: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(80)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(80)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(80)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  fitnessMenu()


def vhclDrv():
  global check0
  global check1
  global check2
  global clear
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Integers (Max Vehciles Driven is 99).")
  print(" ")
  number = int(input("Enter An Integer for Vehciles Driven: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(84)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(84)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(84)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  fitnessMenu()

def zmbiKill():
  global check0
  global check1
  global check2
  global clear
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Integers (Max Zombie Kills is 99).")
  print(" ")
  number = int(input("Enter An Integer for Zombie Kills: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(76)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(76)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(76)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  fitnessMenu()

def DaysSurv():
  global check0
  global check1
  global check2
  global clear
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Integers.")
  print(" ")
  number = int(input("Enter An Integer for Days Survived: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(68)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(68)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(68)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  fitnessMenu()

def DistTrvl():
  global check0
  global check1
  global check2
  global clear
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Integers.")
  print(" ")
  number = int(input("Enter An Integer for Distance Traveled: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(72)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(72)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(72)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  fitnessMenu()

def foodWater():
  global check0
  global check1
  global check2
  global clear
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Integers (Max Food/Water Consumed is 99).")
  print(" ")
  number = int(input("Enter An Integer for Food/Water Consumed: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(88)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(88)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(88)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  fitnessMenu()


def healthItm():
  global check0
  global check1
  global check2
  global clear
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Integers (Max Health Items Consumed is 99).")
  print(" ")
  number = int(input("Enter An Integer for Health Items Consumed: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(92)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(92)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(92)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  fitnessMenu()


def fishBirdCatch():
  global check0
  global check1
  global check2
  global clear
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Integers (Max Fish/Birds Caught is 99).")
  print(" ")
  number = int(input("Enter An Integer for Fish/Birds Caught: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if check0 == True:
    with open('Data0', 'rb+') as bin_file:
      bin_file.seek(96)
      bin_file.write(reversed_array)

  if check1 == True:
    with open('Data1', 'rb+') as bin_file:
      bin_file.seek(96)
      bin_file.write(reversed_array)

  if check2 == True:
    with open('Data2', 'rb+') as bin_file:
      bin_file.seek(96)
      bin_file.write(reversed_array)
  print("Wrote Data To File(s).")
  input("Press 'Enter' To Continue. ")
  fitnessMenu()













def fitnessMenu():
  global clear
  subsys = [1,2,3,4,5,6,7,8,0]

  system(clear)
  print("Fitness Menu (v1.1)")
  print(" ")
  print("1 = Player Kills") # Seek 80
  print("2 = Zombie Kills") # Seek 76
  print("3 = Days Survived") # Seek 68
  print("4 = Kilometers Traveled") # Seek 72
  print(" ")
  print("5 = Vehciles Driven") # Seek 84
  print("6 = Food/Water Consumed") # Seek 88
  print("7 = Health Items Consumed") # Seek 92
  print("8 = Birds/Fish Caught.") # Seek 96
  print("0 = Return To Menu")

  print(" ")
  useri = int(input("Select Choice: "))

  if useri not in subsys:
    fitnessMenu()

  if useri == 1: # 1st Half
    plyrKill()
  
  if useri == 2:
    zmbiKill()

  if useri == 3:
    DaysSurv()
  
  if useri == 4: 
    DistTrvl()

  if useri == 5: # 2nd Half
    vhclDrv()

  if useri == 6:
    foodWater()

  if useri == 7:
    healthItm()

  if useri == 8:
    fishBirdCatch()

  if useri == 0:
    Menu2()


























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
  spectrum0 = [1, 2, 3, 4, 5, 6, 0]
  system(clear)
  print("Ice Station Z Save Editor + Fixer (Console Window)")
  print("Press '1-6' (or) '0' To Select Your Options. (And Then Hit 'Enter')")
  print(" ")
  print("1 = Edit Health")
  print("2 = Edit Thirst")
  print("3 = Edit Hunger")
  print("4 = Edit Battery")
  print(" ")
  print("5 = Fitness Menu (v1.1)")
  print("6 = Active Slots Menu (v1.4)")
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

  if user_u == 5:
    fitnessMenu()

  if user_u == 6:
    system(clear)
    print("This Feature is Still in Development.")
    print("This Will Release Around 03/01/2023.")
    sleep(5)
    Menu2()














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
  print('Version 1.6')
  sleep(0.5)
  system(clear)
  print("Ice Station Z Save Editor + Fixer (Console Window)")
  print("Press '1-7' (or) '0' To Select Your Options. (And Then Hit 'Enter')")
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
    Menu2()


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