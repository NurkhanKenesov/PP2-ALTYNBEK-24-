#ex1
def Squares(N):
    a = 1
    while a < N:
        yield a**2
        a+=1 

lim = int(input())

for i in Squares(lim):
    print(i)
#ex2
def PrintDef(N):
    for i in range(N):
        if i%2 == 0:
            yield i

List = [x for x in range(1,9)]
print(List)

# generator expression 
PrintDefver2 = (i for i in range(4) if i%2==0)

for i in PrintDef(4):
    print(i,end=",")

print()

for i in PrintDefver2:
    print(i,end=",")
#ex3
def Divby4and3(n):
    for i in range(12,n):
        if i % 12 == 0:
            yield i 



DivBy3and4 = (i for i in range(12,100) if i % 12==0)
#ex4
def Squares(a,b):
    for i in range(a,b):
        yield i*i

for i in Squares(10,20):
    print(i)
#ex5
def generator(n):
    iterator = n
    while(iterator):
        yield iterator
        iterator -= 1
    yield 0
for i in generator(7):
    print(i)