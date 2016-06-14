# take input from the user
lowernumber = int(input("Enter lower range: "))
uppernumber = int(input("Enter upper range: "))
def prime(small,large):
    for x in range(small,large + 1):
       # prime numbers are greater than 1
       if x > 1:
           for i in range(2,x):
               if (x % i) == 0:
                   break
           else:
               print(x)
      
prime(lowernumber,uppernumber)