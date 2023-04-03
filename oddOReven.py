def evenOdd(n):
    if(n % 2 == 0):
        return True
     
    elif(n %2 != 0):
        return False
        
    else:
        return evenOdd(n)
 
num =int(input('Enter the number:'))
if(evenOdd( num )):
    print(num ,":-Number is even")
else:
    print(num ,":-Number is odd")