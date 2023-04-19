print("Welcome to Check the sound level\n")

level_value=int(input("Please enter the level value\n"))

if (level_value >= 130):
 print("It is Jackhammer")
elif (level_value >= 106 and level_value <130):
 print ("It is Gas lawnmower")
elif (level_value >= 70 and level_value <106):
 print ("It is Alarm Clock")
elif (level_value >= 40 and level_value <70):
 print ("It is Quiet Room")

else:
 print ("There is no sound")
 

