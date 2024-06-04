class accion_1:

    #Constructor 
    def __init__(self):
        pass
    #METODO PARA DIBUJAR LA TABLA DE FRECUENCIA
    def dibujar (self,intervalos):
        #CILO UTILIZADO PARA ASIGNARLE LOS VALORES A VARIABLES LAS CUALES SRAN LAS QUE SE VAN A IMPRIMIR
        tamano= self.saber_mayor (intervalos) +1
        self.dibujar_indice (tamano)
        for intervalo in (intervalos):          
            valor_intervalo= intervalo [0]
            valor_intervalo= self.modificador_dibujar_primario (valor_intervalo,tamano)
            valor_frecuencia=  intervalo [1]
            valor_frecuencia= self.modificador_dibujar_general (valor_frecuencia,tamano)
            valor_fr= intervalo [2]
            valor_fr= self.modificador_dibujar_general (valor_fr,tamano)
            valor_fra= intervalo [3]
            valor_fra= self.modificador_dibujar_general (valor_fra,tamano)
            valor_frp= intervalo [4]
            valor_frp= self.modificador_dibujar_general (valor_frp,tamano)
            valor_frpa= intervalo [5]
            valor_frpa= self.modificador_dibujar_general (valor_frpa,tamano)
            valor_fo= intervalo [6]
            valor_fo= self.modificador_dibujar_ultimo(valor_fo,tamano)
        #JOIN UTILIZADO PARA GUARDAR EL MENSAJE CON CADA UNO DE LOS DATOS SEPARADOS POR UN |
            linea= "".join ([str(valor_intervalo),
                            str(valor_frecuencia),
                            str(valor_fr),
                            str(valor_fra),
                            str(valor_frp),
                            str(valor_frpa),
                            str(valor_fo)]) 
            print ("\033["+"7;30;45"+"m "+"\u2503"+" ".center(tamano," ") +"\u2503"+" ".center(tamano," ")+"\u2503"+" ".center(tamano," ")+"\u2503"+" ".center(tamano," ")+"\u2503"+" ".center(tamano," ")+"\u2503"+" ".center(tamano," ")+"\u2503"+" ".center(tamano," ")+"\u2503"+" \033[0m")
            print (linea)
            print ("\033["+"7;30;45"+"m "+"\u2523"+("\u2501"* (tamano)+"\u254B")*6+("\u2501"*tamano)+"\u252B"+" \033[0m")

    def saber_mayor (self, intervalos):
        tamaño_mayor = 14
        for intervalo in intervalos:
            valor_1 = len(str(intervalo [0]))
            valor_2 = len(str(intervalo [1]))
            valor_3 = len(str(intervalo [2]))
            valor_4 = len(str(intervalo [3]))
            valor_5 = len(str(intervalo [4]))
            valor_6 = len(str(intervalo [5]))
            valor_7 = len(str(intervalo [6]))
            lista_valores = [valor_1,valor_2,valor_3,valor_4,valor_5,valor_6,valor_7]
            nuermo_selecto= max(lista_valores)
            if (nuermo_selecto > tamaño_mayor):
                tamaño_mayor = nuermo_selecto
        return (tamaño_mayor)
    def dibujar_indice (self, tamaño_mayor):
        if (tamaño_mayor < 12):
            tamaño_mayor = 12

        indice= "".join ([str("\u2503 "+"INTERVALO".center(tamaño_mayor-2," ")+" \u2503"),
                            str(" "+"FRECUENCIA".center(tamaño_mayor-2," ")+" \u2503 "),
                            str(" "+"FR".center(tamaño_mayor-2," ")+"\u2503 "),
                            str(" "+"FRA".center(tamaño_mayor-2," ")+"\u2503 "),
                            str(" "+"FRP".center(tamaño_mayor-2," ")+"\u2503 "),
                            str(" "+"FRPA".center(tamaño_mayor-2," ")+"\u2503 "),
                            str(" "+"F°".center(tamaño_mayor-2," ")+"\u2503")])
        linea_superior = "\u2503"+" "*(tamaño_mayor)+"\u2503"+" "*(tamaño_mayor)+"\u2503"+" "*(tamaño_mayor)+"\u2503"+" "*(tamaño_mayor)+"\u2503"+" "*(tamaño_mayor)+"\u2503"+" "*(tamaño_mayor)+"\u2503"+" "*(tamaño_mayor)+"\u2503"
        print ("\033["+"7;30;45"+"m "+"\u250F"+("\u2501"*(tamaño_mayor)+"\u2533")*6+"\u2501"*tamaño_mayor+"\u2513"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+linea_superior+" \033[0m")
        print ("\033["+"7;30;45"+"m "+indice+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2523"+("\u2501"*(tamaño_mayor)+"\u254B")*6+("\u2501")*tamaño_mayor+"\u252B"+" \033[0m")       
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL DATO A AGREGAR EN VALORES DIFERENTES AL PRIMERO Y AL ULTIMO
    def modificador_dibujar_general (self,dato_acomodar,tamano):
        dato_acomodar = str(dato_acomodar)
        if (tamano < 12):
            tamano = 12
        mensaje="\033["+"7;30;45"+"m"+dato_acomodar.center(tamano-1," ")+"\u2503"+" \033[0m"
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL PRIMER DATO
    def modificador_dibujar_primario (self,dato_acomodar,tamano):
        dato_acomodar = str(dato_acomodar)
        if (tamano < 12):
            tamano = 12
        mensaje="\033["+"7;30;45"+"m"+" \u2503"+dato_acomodar.center(tamano," ")+"\u2503"+" \033[0m"
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL ULTIMO DAÑO
    def modificador_dibujar_ultimo (self,dato_acomodar,tamano):
        dato_acomodar = str(dato_acomodar)
        if (tamano < 12):
            tamano = 12
        mensaje="\033["+"7;30;45"+"m"+dato_acomodar.center(tamano-1," ")+"\u2503"+" \033[0m"
        return (mensaje)

#INSTACIA DE LA CLASE ACCION_1
creacion_accion_1 = accion_1()
intervalos = [['1',2,1,3,4,5,14],['1',1,1,45,89,456,1234]]
creacion_accion_1.dibujar(intervalos)
