import math
import tkinter as tk

def getinput():
  try:
    jumpermass = float(massentry.get())
    jumperheight = float(heightentry.get())
    calculate(jumpermass, jumperheight)
  except:
    addstringlabel["text"] = "Invalid operation. Check if the inputs are numbers."


def calculate(jumpermass,jumperheight):
  etotal = totalenergy(grav,jumpermass,startheight)
  #print("\n")
  #fheight is finish height
  fheight = endheight(nogo,buffer)
  #print("\n")
  feenergy = elasticenergy(fheight,etotal,grav,jumpermass)
  #print("\n")
  stretch = stretchcalc(feenergy,spring)
  #print("\n\n-------------------------------------------------\n\n")
  adstring = additionalstring(startheight,fheight,stretch,jumperheight,unstretch)
  if adstring < 0:
    print('This is an unsafe situation. The customer should not jump, or they may be injured. DO NOT CONTINUE! Here be dragons')
    addstringlabel["text"] = "This is an unsafe situation. The customer should not jump, or they may be injured. DO NOT CONTINUE!"
  else:
    addstringlabel["text"] = f"{adstring}"
    print(f'You should add {adstring} meters of rope to the cord. This will ensure that the jumper gets to the target height.')

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

#tkinter initialize
window = tk.Tk()
mainframe = tk.Frame()
warning = tk.Label(master=mainframe, text="THIS SOFTWARE IS NOT LIABLE FOR ANY DECISIONS MADE BY THE JUMP TECHNICIAN. \nBUNGEE JUMPING IS A DANGEROUS SPORT. JUMPERS MAY BE INJURED!").grid(row="0", column="1")
mainframe.pack()

print('THIS SOFTWARE IS NOT LIABLE FOR ANY DECISIONS MADE BY THE JUMP TECHNICIAN. BUNGEE JUMPING IS A DANGEROUS SPORT. JUMPERS MAY BE INJURED!')
try:
  with open('jumpsetup.txt') as datafile:
    startheight = float(datafile.readline())
    buffer = float(datafile.readline())
    nogo = float(datafile.readline())
    unstretch = float(datafile.readline())
    grav = float(datafile.readline())
    spring = float(datafile.readline())
  setupdone = tk.Label(master=mainframe, text='Detected Setup data. Skipping initialization.').grid(row="1", column="1")
  print('Detected Setup data. Skipping initialization.')
  lastrow = 1
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
  setupcomplete = tk.Label(master=mainframe, text='Initial setup complete!').grid(row="1", column="1")
  lastrow = 1


# Used for square roots in stretchcalc function
masslabel = tk.Label(master=mainframe, text=' Input mass of jumper (kg): ').grid(row=str(lastrow + 1), column=0)
massentry = tk.Entry(master=mainframe)
massentry.grid(row=str(lastrow + 2), column = "0")

#print(massentry)

heightlabel = tk.Label(mainframe, text=' Input height of jumper (m): ').grid(row=str(lastrow + 1), column=1)
heightentry = tk.Entry(mainframe)
heightentry.grid(row=str(lastrow + 2), column = "1")

addlabel = tk.Label(mainframe, text=' Add this amount of string (m): ')
addlabel.grid(row=str(lastrow + 1), column=2)
addstringlabel = tk.Label(mainframe, text='')
addstringlabel.grid(row=str(lastrow + 2), column=2)

calcbtn = tk.Button(mainframe, text='Calculate', command = getinput)
calcbtn.grid(row=str(lastrow+3),column=2)

window.mainloop()



#startheight = float(input("\nInput starting height for the jump (m): "))

#buffer = float(input("\nInput buffer zone where jumper should not be, but can enter if neccessary (m): "))

#nogo = float(input("\nInput the area where the jumper cannot enter in a safe manner, for example where they might hit people (m): "))

#spring = float(input("\nInput the spring constant, or stretchiness of the spring (n/m): "))

#unstretch = float(input("\nInput length of cord (stretchy bit) when not being stretched at all (m): "))

#grav = 9.8
#if input("\nAre you on earth? Input y or n: ") == "n":
#  grav = float(input("Input gravitational constant (m/s^2): "))


#print("\n\n\n")
