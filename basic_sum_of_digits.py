### Take an integer input from the user
### Add the sume of digits
### Eg: 123 -> 1+2+3 = 6

print("I will find  the sum of digits of the number you give me")
number=input("Enter the number:")

## List comprehension
print("##### List comprehension #####")
sumofdigit=sum([int(num) for num in str(number)])
print("Sum of {} using list comprehension is {}".format(number,sumofdigit))

print("\n")

## Iterative method
print("##### Iterative method #####")
sumIt=0
for num in str(number):
   sumIt=sumIt+int(num)
print("Sum of {} using iterative method is {}".format(number,sumIt))
