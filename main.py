#from tkinter import *
#from tkinter import ttk
import math
#rootwin = Tk()
#basefrm = ttk.Frame(rootwin, padding = 10)
#basefrm.grid()
#tkinter initialize
print('THIS SOFTWARE IS NOT LIABLE FOR ANY DECISIONS MADE BY THE JUMP TECHNICIAN. BUNGEE JUMPING IS A DANGEROUS SPORT. JUMPERS MAY BE INJURED!')
try:
  with open('jumpsetup.txt') as datafile:
    startheight = float(datafile.readline())
    buffer = float(datafile.readline())
    nogo = float(datafile.readline())
    unstretch = float(datafile.readline())
    grav = float(datafile.readline())
    spring = float(datafile.readline())
  print('Detected Setup data. Skipping initialization.')
except FileNotFoundError: #if no existing file for initialization is found, set one up
  print('There is no existing setup data for this jump. Creating data now.')
  startheight = float(input("\nInput starting height for the jump (m): "))
  buffer = float(input("\nInput buffer zone where jumper should not be, but can enter if neccessary (m): "))
  nogo = float(input("\nInput the area where the jumper cannot enter in a safe manner, for example where they might hit people (m): "))
  if nogo + buffer > startheight:
    print('The total nogo/buffer height cannot be greater than the starting height. Please try again.')
    buffer = float(input("\nInput buffer zone where jumper should not be, but can enter if neccessary (m): "))
    nogo = float(input("\nInput the area where the jumper cannot enter in a safe manner, for example where they might hit people (m): "))
  unstretch = float(input("\nInput length of cord (stretchy bit) when not being stretched at all (m): "))
  grav = 9.8
  if input("\nAre you on earth? Input y or n: ") == "n":
    grav = float(input("Input gravitational constant (m/s^2): "))
  spring = float(input("\nInput the spring constant, or stretchiness of the spring (n/m): "))
  with open('jumpsetup.txt', 'w') as datafile:
    datafile.write(f"{startheight}\n{buffer}\n{nogo}\n{unstretch}\n{grav}\n{spring}")
  print("Initial setup complete!")


# Used for square roots in stretchcalc function
jumpermass = float(input("Input mass of jumper (kg): "))

jumperheight = float(input("\nInput height of jumper (m): "))

#startheight = float(input("\nInput starting height for the jump (m): "))

#buffer = float(input("\nInput buffer zone where jumper should not be, but can enter if neccessary (m): "))

#nogo = float(input("\nInput the area where the jumper cannot enter in a safe manner, for example where they might hit people (m): "))

#spring = float(input("\nInput the spring constant, or stretchiness of the spring (n/m): "))

#unstretch = float(input("\nInput length of cord (stretchy bit) when not being stretched at all (m): "))

#grav = 9.8
#if input("\nAre you on earth? Input y or n: ") == "n":
#  grav = float(input("Input gravitational constant (m/s^2): "))

def endheight(nogo,buffer):
  heightval = nogo + buffer
#  ttk.Label(basefrm, text=f"The height that the jumper should (hopefully) end up at is {heightval} meters").grid(column=0, row=0)
  print('The height that the jumper should (hopefully) end up at is',heightval,"meters.")
  return heightval

def totalenergy(gravconstant,massjumper,stheight):
  etotal = gravconstant * massjumper * stheight
#  ttk.Label(basefrm, text=f"The total energy in this system is {etotal} joules.").grid(column=0, row=2)
  print("The total energy in this system is",etotal,"joules.")
  return etotal

def elasticenergy(fheight,etotal,grav,massjumper):
  fgenergy = grav * fheight * massjumper
  feenergy = etotal - fgenergy
  print("The elastic energy that the jumper should end up with is",feenergy,"joules.")
  return feenergy

def stretchcalc(feenergy,spring):
  stretch = math.sqrt(2 * feenergy / spring)
  print("The distance that the cord/spring will stretch is",stretch,"meters.")
  return stretch

def additionalstring(startheight,fheight,stretch,jumperheight,unstretch):
  adstring = startheight - unstretch - stretch - jumperheight - fheight
  return adstring

print("\n\n\n")
etotal = totalenergy(grav,jumpermass,startheight)
print("\n")
#fheight is finish height
fheight = endheight(nogo,buffer)
print("\n")
feenergy = elasticenergy(fheight,etotal,grav,jumpermass)
print("\n")
stretch = stretchcalc(feenergy,spring)
print("\n\n-------------------------------------------------\n\n")
adstring = additionalstring(startheight,fheight,stretch,jumperheight,unstretch)
if adstring < 0:
  print('This is an unsafe situation. The customer should not jump, or they may be injured. DO NOT CONTINUE!')
else:
  print(f'You should add {adstring} meters of rope to the cord. This will ensure that the jumper gets to the target height.')