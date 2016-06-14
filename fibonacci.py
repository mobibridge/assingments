def fib(x):
    myfib = [0,1];
    for i in range(2,x):
        myfib.append(myfib[i-1] + myfib[i-2]);
        
    print(myfib)
    
x=int(input("enter any number"))
fib(x)