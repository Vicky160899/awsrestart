x =int(input('enter the no:-'))
if x > 1:
   for n in range(2, x):
      if (x % n) == 0:
         print(x, "is not prime")
         print(n, "times", x // n, "is", x)
         break
      print(x, "is a prime number")
   else:
      print(x, "is not prime number")