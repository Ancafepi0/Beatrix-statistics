class accion_9:
    #Constructor 
    def __init__(self):
        pass
    def dibujar (self,lista_datos):
        for dato in (lista_datos):
            limite_inferior= dato[0]
            limite_inferior=self.modificador_dibujar_primario (limite_inferior)
            q1=dato[1]
            q1=self.modificador_dibujar_general (q1)
            q2=dato [2]
            q2=self.modificador_dibujar_general (q2)
            q3= dato[3]
            q3=self.modificador_dibujar_general (q3)
            limite_superior= dato[4]
            limite_superior=self.modificador_dibujar_ultimo (limite_superior)
            linea= "".join ([str(limite_inferior),
                            str(q1),
                            str(q2),
                            str(q3),
                            str(limite_superior),])
        print ("\033["+"7;30;45"+"m "+"  ________________________________________________________ "+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                                                        |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                                                        |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |    |             _________ _________             |     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |    |            |         |         |            |     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |    |            |         |         |            |     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |    |            |         |         |            |     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |    |            |         |         |            |     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |    |             ¯¯¯¯¯¯¯¯¯ ¯¯¯¯¯¯¯¯¯             |     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                 |         |         |                  |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                 |         |         |                  |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |  _______________|_________|_________|_________________ |"+" \033[0m")
        print ("\033["+"7;30;45"+"m " , linea ," \033[0m")
        print ("\033["+"7;30;45"+"m "+" |  LIMITE        Q1        Q2        Q3        LIMITE    |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" | INFERIOR                                    SUPERIOR   |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |________________________________________________________|"+" \033[0m")

    
                     
    
    def modificador_dibujar_general (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"    "+" \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m "+"  "+dato_acomodar+"     "+" \033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m "+"   "+dato_acomodar+"  "+" \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m "+"   "+dato_acomodar+"   "+" \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"  "+dato_acomodar+"   "+" \033[0m"
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL PRIMER DATO
    def modificador_dibujar_primario (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+"|    "+ dato_acomodar +"    "+"    \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m"+"|   "+dato_acomodar+"    "+"   \033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m"+"|   "+dato_acomodar+"  "+"    \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"   \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"    "+dato_acomodar+"  \033[0m"
 
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL ULTIMO DAÑO
    def modificador_dibujar_ultimo (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+"       "+dato_acomodar+ "    "+" |"+" \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m"+"     "+dato_acomodar+"    "+"| "+"\033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m"+"       "+dato_acomodar+"   "+" |"+" \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"   \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"   "+dato_acomodar+"   \033[0m"


        return (mensaje)
ejecutar_9 = accion_9()
lista_datos = [[111,112,113,114,115]]
ejecutar_9.dibujar(lista_datos)