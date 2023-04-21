def common_elements(list1, list2):

    for x in list1:
      if x in list2:
         return True

    return False

def main():
   list1 = [1,2,3,4,5]
   list2 = [2,7,8,7,9]

   print(common_elements(list1, list2))
main()