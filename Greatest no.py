num1=int(input('Enter first no:'))
num2=int(input('Enter second no:'))
num3=int(input('Enter first no:'))
if (num1 >= num2) and (num1 >= num3):
   greatest = num1
elif (num2 >= num1) and (num2 >= num3):
   greatest = num2
else:
   greatest = num3

print("The Greatest number is", greatest)