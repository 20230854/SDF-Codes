print("Welcome to Chineses Zodiac sign assign to animals\n")
#year_names=["Dragon","Snake","Horse","Sheep","Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Hare"]
zodiac_year = int(input("Please enter the year\n"))
#print(year_names[(zodiac_year - 2000) % 12])
if (zodiac_year - 2000) % 12 == 0:
 print ("You are a dragon")
elif (zodiac_year - 2000) % 12 == 1:
 print ("Snake") 
elif (zodiac_year - 2000) % 12 == 2:
 print ("Horse")
elif (zodiac_year - 2000) % 12 == 3:
 print ("Sheep")
elif (zodiac_year - 2000) % 12 == 4:
 print ("Monkey")
elif (zodiac_year - 2000) % 12 == 5:
 print ("Rooster")
elif (zodiac_year - 2000) % 12 == 6:
 print ("Dog")
elif (zodiac_year - 2000) % 12 == 7:
 print ("Pig")
elif (zodiac_year - 2000) % 12 == 8:
 print ("Rat")
elif (zodiac_year - 2000) % 12 == 9:
 print ("Ox")
elif (zodiac_year - 2000) % 12 == 10:
 print ("Tiger")
elif (zodiac_year - 2000) % 12 == 11:
 print ("Hare")

else:
 print ("value is not present here")
 