print("Welcome to view earthquake magnitude range below\n")

range_value = float(input("Please enter the range\n"))

if (range_value < 2.0):
 print("It is Micro")
elif (range_value >= 2.0 and range_value <3.0):
 print ("It is Very Minor")
elif (range_value >= 3.0 and range_value <4.0):
 print ("It is Minor")
elif (range_value >= 4.0 and range_value <5.0):
 print ("It is Light")
elif (range_value >= 5.0 and range_value <6.0):
 print ("It is Moderate")
elif (range_value >= 6.0 and range_value <7.0):
 print ("It is Strong")
elif (range_value >= 7.0 and range_value <8.0):
 print ("It is Major")
elif (range_value >= 8.0 and range_value <10.0):
 print ("It is Great")

else:
 print ("It is meteoric")
 

