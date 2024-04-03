class accion_1:

    #Constructor 
    def __init__(self):
        pass
    #
    def dibujar (self,lista_intervalor):
        print ("\033["+"7;30;45"+"m "+" __________________________________________________________________________________________ "+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"|            |            |            |            |            |            |            |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"|  INTERVALO | FRECUENCIA |     FR     |     FRA    |     FRP    |     FRPA   |      F°    |"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ "+" \033[0m")
        for intervalo in range (lista_intervalor):
            valor_intervalo= intervalo [0]
            valor_frecuencia=  intervalo [1]
            valor_fr= intervalo [2]
            valor_fra= intervalo [3]
            valor_frp= intervalo [4]
            valor_frpa= intervalo [5]
            valor_fo= intervalo [6]
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL DATO A PARQUEAR
    def modificador_dibujar (self,dato_acomodar):

#INSTACIA DE LA CLASE ACCION_1
creacion_accion_1 = accion_1()
creacion_accion_1.dibujar()
