#ex1
import math 
def ConToRad(angle):
    return (angle*math.pi)/180
inner=int(input("Input degree: "))
print("Output radian: ",ConToRad(inner))
#ex2
def AreaofTpz(Height,BaseDown,BaseUp):
    return Height*(BaseDown+BaseUp)/2
height = int(input("Height: "))
baseFirst = int(input("Base, first value: "))
baseSecond = int(input("Base, second value: ")) 
print("Area is :",AreaofTpz(height,baseFirst,baseSecond))
#ex3
from math import tan, pi
def CalcAreaPolygon(n,length):
    return  n * (length ** 2) / (4 * tan(pi / n))
#magic
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
print("The area of the polygon is: ",CalcAreaPolygon(n,s))
#ex4
def AreaofP(height,length):
    return height*length
l = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
print("Area is: ",AreaofP(h,l))