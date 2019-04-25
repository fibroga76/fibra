import turtle as t         #alias

while True:
    
    lettera = input("Inserisci lettera(a,g,h,d): ")

    if(lettera == "a"):
        t.forward(50)
    elif (lettera == "g"):
        t.left(90)
    elif (lettera == "h"):
        t.right(90)
    elif (lettera == "d"):
        t.back(50)
t.done()