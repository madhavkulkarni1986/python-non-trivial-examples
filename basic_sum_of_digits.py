### Take an integer input from the user
### Add the sume of digits
### Eg: 123 -> 1+2+3 = 6

print("**************************************************************")
print("** I will find  the sum of digits of the number you give me **")
print("**************************************************************\n")
number=input("Enter the number:")

## List comprehension
try:
   sumofdigit=sum([int(num) for num in str(number)])
   print("\n##### List comprehension #####")
   print("Sum of {} using list comprehension is {}".format(number,sumofdigit))

## Iterative method
   print("\n##### Iterative method #####")
   sumIt=0
   for num in str(number):
      sumIt=sumIt+int(num)
   print("Sum of {} using iterative method is {}".format(number,sumIt))
except ValueError:
   print("[Error]: You have not provided a interger")
