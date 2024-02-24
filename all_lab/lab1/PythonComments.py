def myfunction(x):
    a=1
    if(x<0):
        return 0
    elif(x==1):
        return 1
    else:
        while(x>0):
            a=a*x
            x=x-1
        return a
x=int(input())
print(myfunction(x))
