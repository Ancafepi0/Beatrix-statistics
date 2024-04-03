class accion_8:
    #Constructor 
    def __init__(self):
        pass
    def dibujar (self,lista_datos):
        for dato in (lista_datos):
            x_3s= dato[0]
            x_3s=self.modificador_dibujar_primario (x_3s)
            x_2s=dato[1]
            x_2s=self.modificador_dibujar_general (x_2s)
            x_1s=dato [2]
            x_1s=self.modificador_dibujar_general (x_1s)
            x= dato[3]
            x=self.modificador_dibujar_general (x)
            x__s= dato[4]
            x__s=self.modificador_dibujar_general (x__s)
            x__2s= dato[5]
            x__2s=self.modificador_dibujar_general (x__2s)
            x__3s = dato [6]
            x__3s=self.modificador_dibujar_ultimo (x__3s)
            linea= "".join ([str(x_3s),
                            str(x_2s),
                            str(x_1s),
                            str(x),
                            str(x__s),
                            str(x__2s),
                            str(x__3s)])
        print ("\033["+"7;30;45"+"m "+"  ____________________________________________________ "+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                                                    |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                                                    |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                      _______                       |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                     /   |   \                      |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                ____/    |    \____                 |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |               / |       |       | \                |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |              /  |       |       |  \               |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |         ____/   | 34%   |  34%  |   \____          |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |        /|       |       |       |       |\         |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |  _____/ | 13.5% |       |       | 13.5% | \_____   |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" | / | 24% |       |       |       |       | 24% | \  |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ "+" \033[0m")
        print ("\033["+"7;30;45"+"m ",linea," \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                  <------ ------>                   |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                    EL 68% DENTRO                   |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                     1 DESVIACION                   |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                      ESTANDAR                      |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                                                    |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |           <-------------  ------------->           |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                    EL 95% DENTRO                   |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                      2 DESVICIONES                 |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                       ESTANDAR                     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |    <--------------------    ----------------->     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                    EL 97% DE TODOS                 |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                    LOS DATOS ESTAN                 |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                DENTRO DE 3 DESVIACIONES            |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                       ESTANDAR                     |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" |                                                    |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ "+" \033[0m")
    
                     
    
    def modificador_dibujar_general (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+"  "+dato_acomodar+"   "+" \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m "+" "+dato_acomodar+"  "+" \033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m "+" "+dato_acomodar+" "+" \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m "+"   "+dato_acomodar+"   "+" \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"  "+dato_acomodar+"   "+" \033[0m"
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL PRIMER DATO
    def modificador_dibujar_primario (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+"|   "+ dato_acomodar +"    \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m"+"|  "+dato_acomodar+"    \033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m"+"| "+dato_acomodar+"    \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"   \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"    "+dato_acomodar+"  \033[0m"
 
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL ULTIMO DAÑO
    def modificador_dibujar_ultimo (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+ "   "+" |"+" \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"  "+" | "+"\033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+" "+" |"+" \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"   \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"   "+dato_acomodar+"   \033[0m"


        return (mensaje)
ejecutar_8 = accion_8()
lista_datos = [[111,112,113,114,115,116,117]]
ejecutar_8.dibujar(lista_datos)