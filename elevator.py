print("Door is opening ...Welcome!")
current_floor = 1
while True:
    print("current_floor=" , current_floor)
    floor=int(input("Enter your designated floor :"))
    if floor != current_floor :
     print("Door is closing .....")
    if floor > current_floor:
     print("Lift is going UP .....")
    elif floor < current_floor :
        print("Lift is going DOWN ....")
    else :
      print("You are already on this floor ....")
    current_floor = floor 
    if (floor==1):
     print("you are on ground floor")
    elif(floor==2):
      print("welcome to  second floor")
    elif(floor==3):
      print("welcome to the third floor ") 
    elif(floor==4):
      print("welcome to the fourth floor")
    elif(floor==5):
      print("welcome to the fifth floor")
    elif(floor==6):
     print("welcome to the six floor")
    elif(floor==7):
     print("welcome to the seventh floor")
    elif(floor==8):
      print("welcome to the eigth  floor")
    elif(floor==9):
      print("welcome to the nineth floor")
    elif(floor==10):
     print("welcome to the tenth floor")
    elif(floor==11):
     print("welcome to the eleventh floor")
    elif(floor==12):
     print("welcome to the twelveth floor")
    elif(floor==13):
      print("welcome to the thirteenth  floor")
    elif(floor==14):
      print("welcome to the fourteenth floor")
    elif(floor==15):
     print("welcome to the fifteenth floor")
    elif(floor==16):
     print("welcome to the sixteenth floor")
    else:
     print("you are on the top of the Arfa Tower")
