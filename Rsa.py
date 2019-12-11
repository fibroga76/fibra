import math

print("Inserire p:")
p = int(input())
print("inserire q:")
q = int(input())

n = int(p * q)
m = 0
d = 0

print("n vale:", n)

if(p<q):
    maggiore = q
else:
    maggiore = p

while(m==0):
    if((maggiore % (q-1) == 0) and (maggiore % (p-1) == 0)):
        m = maggiore
        break
    maggiore = maggiore + 1

print("m vale:", m)

while(True):
    print("Inserire un numero 'c' che sia compreso tra 1 e m:")
    c = int(input())
    if(math.gcd(c, m)==1):
        break
    else:
        print("Il numero che è stato inserito deve essere compreso tra 1 e m:")

while(True):
    if((c*d)%m == 1):
        break
    else:
        d = d + 1

print("d vale:", d)