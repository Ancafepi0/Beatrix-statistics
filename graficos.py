#Cuadrado relleno
"""size = 5
for i in range (0,size):
    for j in range(0,size):
        print ("* ", end = "")
    print ()"""

#Cuadrado hueco
"""size = 5
for i in range (0,size):
    for j in range (0,size):
        if (i== 0 or i == size-1 or j == 0 or j == size-1):
            print ("-", end = " ")
        else:
            print (" ", end= " ")
    print ()"""

#Triangulo a la izquierda 
"""n= 5
for i in range (1, n+1):
    for j in range (1, i +1):
        print ("* ", end= "")
    print ()"""

#Triangulo a la derecha
"""n= 5
for i in range (n):
    for j in range (1,n-i):
        print (" ", end = " ")
    for k in range (n-i,n+1):
        print ("*", end = " ")
    print ()"""

#Triangulo hueco a la izquierda
n = 5
for i in range (1, n+1):
    for j in range (i):
        if j == 0 or j == i-1:
            print ("*", end = " ")
        else:
            if i!=n:
                print (" ", end = " ")
            else:
                print ("*", end= " ")
    print ()