def get_multiplied_digits(number):
   str_number = str(number)
   if len(str_number) > 1:
       first = int(str_number[0])
       return first * get_multiplied_digits(int(str_number[1:]))
   if number == 0:
       return 1
   else:
       return str (str_number)

result = get_multiplied_digits(4020300)
print(result)