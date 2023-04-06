def multiply_numbers(list):
   mult = 1
   for i in list:
      mult = mult*i
   return mult
given_list = [6,2,7,8,4]
print('The list is:',given_list)
print("The multiplication is: ")
print(multiply_numbers(given_list))