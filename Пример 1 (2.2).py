import math

if __name__=="__main__":
    x=float(input("Введите значение x:"))
if x<=3.5:
    y=2*x**2 + math.cos(x)
elif 0<x<5:
    y=x+1
if x>=5:
    y=math.sin(2*x)-x**2
print(f"y={y}")




