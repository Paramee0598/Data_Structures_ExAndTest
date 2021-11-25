print(" *** Summation of each digit ***")
#number = input("Enter a positive number : ")
sum_of_digits = sum(int(digit) for digit in str(input("Enter a positive number : ")))
"""""#sum_of_digits = 0
for digit in str(number): ####นำมาทีละ digit ของ string
  sum_of_digits += int(digit)#โดยแปลงstringเป็น int แล่วบวกทีละอัน"""
#t = int(number)
#sum = 0
#while int(t != 0):

#   remainder = int(t % 10)

#   sum = int(sum+remainder)

#   t = int(t / 10)

print("Summation of each digit =  " + str(sum_of_digits))
#print(sum_of_digits)