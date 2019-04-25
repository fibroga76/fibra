
from turtle import *
fb1 =1
fb2 =1


print("inserisci il numero di bracci")
k=input()
k=int(k)
cont=0

while k>cont:
    forward(fb2)
    right(90)
    cont+=1
    fb2=fb1+fb2
    fb1=fb2
done()

