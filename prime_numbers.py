# take input from the user
lowernumber = int(input("Enter lower range: "))
uppernumber = int(input("Enter upper range: "))
def prime(small,large):
    prime_nos=[]
    for x in range(small,large + 1):
       # prime numbers are greater than 1
       
       isPrime=True

       if x > 1:
           for i in range(2,x):
               if (x % i) == 0:
                    isPrime=False
                    break

           if isPrime:
                prime_nos.append(x)

    return prime_nos

                

       
print(prime(lowernumber,uppernumber))