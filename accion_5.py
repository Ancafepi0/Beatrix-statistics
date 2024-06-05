class accion_5:
    #Constructor 
    def __init__(self):
        pass

    def dibujar (self,intervalos):
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
            linea= "     ".join ([str(valor_intervalo),
                            str(valor_frecuencia),
                            str(valor_fr),
                            str(valor_fra),
                            str(valor_frp),
                            str(valor_frpa),
                            str(valor_fo)])
            print ("\033["+"7;30;45"+"m "+"|            |            |            |            |            |            |            |"+" \033[0m")
            print (linea)
            print ("\033["+"7;30;45"+"m "+" ------------------------------------------------------------------------------------------ "+" \033[0m")

ejecutar_5 = accion_5()
intervalos = [['1',2,1,3,4,5,14],['1',1,1,45,89,456,1234]]
ejecutar_5.dibujar(intervalos)
