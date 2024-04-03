class accion_1:

    #Constructor 
    def __init__(self):
        pass
    #METODO PARA DIBUJAR LA TABLA DE FRECUENCIA
    def dibujar (self,intervalos):
        print ("\033["+"7;30;45"+"m "+" __________________________________________________________________________________________ "+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"|            |            |            |            |            |            |            |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"|  INTERVALO | FRECUENCIA |     FR     |     FRA    |     FRP    |     FRPA   |      F°    |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" ------------------------------------------------------------------------------------------ "+" \033[0m")
        #CILO UTILIZADO PARA ASIGNARLE LOS VALORES A VARIABLES LAS CUALES SRAN LAS QUE SE VAN A IMPRIMIR
        for intervalo in (intervalos):
            valor_intervalo= intervalo [0]
            valor_intervalo= self.modificador_dibujar_primario (valor_intervalo)
            valor_frecuencia=  intervalo [1]
            valor_frecuencia= self.modificador_dibujar_general (valor_frecuencia)
            valor_fr= intervalo [2]
            valor_fr= self.modificador_dibujar_general (valor_fr)
            valor_fra= intervalo [3]
            valor_fra= self.modificador_dibujar_general (valor_fra)
            valor_frp= intervalo [4]
            valor_frp= self.modificador_dibujar_general (valor_frp)
            valor_frpa= intervalo [5]
            valor_frpa= self.modificador_dibujar_general (valor_frpa)
            valor_fo= intervalo [6]
            valor_fo= self.modificador_dibujar_ultimo(valor_fo)
        #JOIN UTILIZADO PARA GUARDAR EL MENSAJE CON CADA UNO DE LOS DATOS SEPARADOS POR UN |
            linea= "".join ([str(valor_intervalo),
                            str(valor_frecuencia),
                            str(valor_fr),
                            str(valor_fra),
                            str(valor_frp),
                            str(valor_frpa),
                            str(valor_fo)]) 
            print ("\033["+"7;30;45"+"m "+"|            |            |            |            |            |            |            |"+" \033[0m")
            print (linea)
            print ("\033["+"7;30;45"+"m "+" ------------------------------------------------------------------------------------------ "+" \033[0m")


    #SIRVE PARA ACOMODAR EL TAMAÑO DEL DATO A AGREGAR EN VALORES DIFERENTES AL PRIMERO Y AL ULTIMO
    def modificador_dibujar_general (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+"     "+dato_acomodar+"     "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m "+"   "+dato_acomodar+"     "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m "+"    "+dato_acomodar+"   "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m "+"   "+dato_acomodar+"   "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"  "+dato_acomodar+"   "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 6):
            mensaje="\033["+"7;30;45"+"m "+"  "+dato_acomodar+"  "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 7):
            mensaje="\033["+"7;30;45"+"m "+"  "+dato_acomodar+" "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 8):
            mensaje="\033["+"7;30;45"+"m "+" "+dato_acomodar+" "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 9):
            mensaje="\033["+"7;30;45"+"m "+""+dato_acomodar+" "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 10):
            mensaje="\033["+"7;30;45"+"m "+""+dato_acomodar+""+"|"+" \033[0m"


        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL PRIMER DATO
    def modificador_dibujar_primario (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+" |"+"      "+dato_acomodar+"     "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m"+" |"+"     "+dato_acomodar+"     "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m"+" |"+"     "+dato_acomodar+"    "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m"+" |"+"    "+dato_acomodar+"    "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"|"+"    "+dato_acomodar+"   "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 6):
            mensaje="\033["+"7;30;45"+"m"+" |"+"   "+dato_acomodar+"   "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 7):
            mensaje="\033["+"7;30;45"+"m"+" |"+"  "+dato_acomodar+"   "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 8):
            mensaje="\033["+"7;30;45"+"m"+" |"+"  "+dato_acomodar+"  "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 9):
            mensaje="\033["+"7;30;45"+"m"+" |"+"  "+dato_acomodar+" "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 10):
            mensaje="\033["+"7;30;45"+"m"+" |"+" "+dato_acomodar+" "+"|"+" \033[0m"

 
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL ULTIMO DAÑO
    def modificador_dibujar_ultimo (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje="\033["+"7;30;45"+"m"+"      "+dato_acomodar+"     "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 2):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"     "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 3):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"    "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 4):
            mensaje="\033["+"7;30;45"+"m"+"    "+dato_acomodar+"   "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 5):
            mensaje="\033["+"7;30;45"+"m "+"   "+dato_acomodar+"  "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 6):
            mensaje="\033["+"7;30;45"+"m"+"  "+dato_acomodar+"   "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 7):
            mensaje="\033["+"7;30;45"+"m"+"  "+dato_acomodar+"  "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 8):
            mensaje="\033["+"7;30;45"+"m"+" "+dato_acomodar+"  "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 9):
            mensaje="\033["+"7;30;45"+"m"+" "+dato_acomodar+" "+"|"+" \033[0m"
        elif(len (dato_acomodar) == 10):
            mensaje="\033["+"7;30;45"+"m"+""+dato_acomodar+" "+"|"+" \033[0m"


        return (mensaje)
"""
#INSTACIA DE LA CLASE ACCION_1
creacion_accion_1 = accion_1()
intervalos = [[4,5,6,7,8,9,10],[10,11,12,13,14,15,16],[101,102,103,104,105,106,107],[1001,1002,1003,1004,1005,1006,1007],[10001,10002,10003,10004,10005,10006,10007],
              [100001,100002,100003,100004,100005,100006,100007],[1000001,1000002,1000003,1000004,1000005,1000006,1000007],
              [10000001,10000002,10000003,10000004,10000005,145450006,100000407]]
creacion_accion_1.dibujar(intervalos)"""
