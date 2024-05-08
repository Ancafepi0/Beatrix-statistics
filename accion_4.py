class accion_4:
    #Constructor 
    def __init__(self):
        pass
    def dibujar (self,intervalos):


        print ("\033["+"7;30;45"+"m "+" |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |      ___________________________________________________________________________________________________              |"+" \033[0m")
        self.modificador_dibujar(intervalos)
        print ("\033["+"7;30;45"+"m "+" |      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯              |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                                                                                                                       |"+" \033[0m")
        self.modificador_nombre(intervalos)
        print ("\033["+"7;30;45"+"m "+"  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ "+" \033[0m")
    
    
    def modificador_dibujar(self,intervalos):
        contador= 0
        for intervalos in (lista_intervalos):
            if  (len(lista_intervalos) == 5):
                dato = int (intervalos [1])
                dato = dato // 5
                if (contador == 0):
                  for i in range (dato): 
                       #blanco 
                       print ("\033["+"7;37;45"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 1):
                    for i in range (dato): 
                        #rojo 
                        print ("\033["+"7;31;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 2):
                    for i in range (dato): 
                        #verde 
                        print ("\033["+"7;32;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 3):
                    for i in range (dato):
                        #amarillo  
                        print ("\033["+"7;33;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 4):
                    for i in range (dato):
                        #morado  
                        print ("\033["+"7;35;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
            elif (len(lista_intervalos) == 6):
                dato = int (intervalos [1])
                dato = dato // 5
                if (contador == 0):
                  for i in range (dato):  
                       print ("\033["+"7;37;45"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 1):
                    for i in range (dato):  
                        print ("\033["+"7;31;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 2):
                    for i in range (dato):  
                        print ("\033["+"7;32;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 3):
                    for i in range (dato):  
                        print ("\033["+"7;33;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 4):
                    for i in range (dato):  
                        print ("\033["+"7;35;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 5):
                    for i in range (dato):  
                        print ("\033["+"7;34;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")

            elif (len(lista_intervalos) == 7):
                dato = int (intervalos [1])
                dato = dato // 5
                if (contador == 0):
                  for i in range (dato):  
                       print ("\033["+"7;37;45"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 1):
                    for i in range (dato):  
                        print ("\033["+"7;31;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 2):
                    for i in range (dato):  
                        print ("\033["+"7;32;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 3):
                    for i in range (dato):  
                        print ("\033["+"7;33;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 4):
                    for i in range (dato):  
                        print ("\033["+"7;35;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 5):
                    for i in range (dato):  
                        print ("\033["+"7;36;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 6):
                    for i in range (dato):  
                        print ("\033["+"7;30;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                
            elif (len(lista_intervalos) == 8):
                dato = int (intervalos [1])
                dato = dato // 5
                if (contador == 0):
                  for i in range (dato):  
                       print ("\033["+"7;37;45"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 1):
                    for i in range (dato):  
                        print ("\033["+"7;31;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 2):
                    for i in range (dato):  
                        print ("\033["+"7;32;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 3):
                    for i in range (dato):  
                        print ("\033["+"7;33;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 4):
                    for i in range (dato):  
                        print ("\033["+"7;35;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 5):
                    for i in range (dato):  
                        print ("\033["+"7;36;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 6):
                    for i in range (dato):  
                        print ("\033["+"7;30;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 7):
                    for i in range (dato):  
                        print ("\033["+"7;36;47 "+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")

            elif (len(lista_intervalos) == 9):
                dato = int (intervalos [1])
                dato = dato // 5
                if (contador == 0):
                  for i in range (dato):  
                       print ("\033["+"7;37;45"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 1):
                    for i in range (dato):  
                        print ("\033["+"7;31;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 2):
                    for i in range (dato):  
                        print ("\033["+"7;32;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 3):
                    for i in range (dato):  
                        print ("\033["+"7;33;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 4):
                    for i in range (dato):  
                        print ("\033["+"7;35;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 5):
                    for i in range (dato):  
                        print ("\033["+"7;36;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 6):
                    for i in range (dato):  
                        print ("\033["+"7;30;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 7):
                    for i in range (dato):  
                        print ("\033["+"7;36;47 "+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 8):
                    for i in range (dato):  
                        print ("\033["+"4;34;45 "+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")

            elif (len(lista_intervalos) == 10):
                dato = int (intervalos [1])
                dato = dato // 5
                if (contador == 0):
                  for i in range (dato):  
                       print ("\033["+"7;37;45"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 1):
                    for i in range (dato):  
                        print ("\033["+"7;31;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 2):
                    for i in range (dato):  
                        print ("\033["+"7;32;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 3):
                    for i in range (dato):  
                        print ("\033["+"7;33;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 4):
                    for i in range (dato):  
                        print ("\033["+"7;35;46"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 5):
                    for i in range (dato):  
                        print ("\033["+"7;36;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 6):
                    for i in range (dato):  
                        print ("\033["+"7;30;47"+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 7):
                    for i in range (dato):  
                        print ("\033["+"7;36;47 "+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 8):
                    for i in range (dato):  
                        print ("\033["+"4;34;45 "+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")
                elif (contador == 9):
                    for i in range (dato):  
                        print ("\033["+"4;34;44 "+"m "+" |     |                                                                                                   |"+"             |"+" \033[0m")

    
            contador += 1
    def modificador_nombre (self,intervalos):
        lista_nombres = []
        for intervalo in (intervalos):
            nombre= str(intervalo[0])
            lista_nombres.append(nombre)
        """if (len(intervalos)== 5):
            lista_colores = ["blanco","rojo","verde","amarillo","morado"]
            linea_colores = "    color=".join (lista_colores)
        if (len(intervalos)== 5):
            lista_porcentaje = []
            for i in intervalos:
                porcentaje= str(i [1])
                lista_porcentaje.append(porcentaje)
            linea_porcentaje = "  porcentaje=".join (lista_porcentaje)"""
        linea_nombres= "  nombre = ".join (lista_nombres) 
        print ("\033["+"7;30;45"+"m "+" | nombre=",linea_nombres,"                                    |"+" \033[0m")
        #print ("\033["+"7;30;45"+"m "+" | color =",linea_colores,"                                        |"+" \033[0m")
        #print ("\033["+"7;30;45"+"m "+" | porcentaje =",linea_porcentaje,"                                          |"+" \033[0m")

ejecutar_4 = accion_4()
lista_intervalos = [[0,10],[5,20],[3,20],[1,10],[4,20],[5,10],[6,10]]
ejecutar_4.dibujar(lista_intervalos)