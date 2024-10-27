#def f(binary_number):
  #  for char in binary_number:
   #     if all(char == '1' or char == '0'):
  #          return True
   #     else:
 #           return False
        
def f(binary_number):
    return all(char in '01' for char in binary_number) and binary_number != ''
