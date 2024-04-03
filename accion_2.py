class accion_2:
    #Constructor 
    def __init__(self):
        pass
    #METODO PARA DIBUJAR EL DIAGRAMA DE BARRAS
    def dibujar(self,lista_intervalo):
        zona_inferior= self.modificador_intervalo(lista_intervalo)
        print ("\033["+"7;30;45"+"m "+" ______________________________________________________ "+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"|                                                      |"+" \033[0m")        
        zona_vertical= self.modiciador_vertical(lista_intervalo)
        zona_horizontal= self.modificador_horizontal(lista_intervalo)
        print ("\033["+"7;30;45"+"m "+"|  "+ zona_inferior +" \033[0m")
        print ("\033["+"7;30;45"+"m "+"|                                                      |"+" \033[0m")                
        print ("\033["+"7;30;45"+"m "+" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ "+" \033[0m")
    #METODO PARA DIBUJAR LA LINEA DONDE VAN LOS INTERVALOS
    def modificador_intervalo (self,lista_intervalo):
        #CRAR TABLA CON LOS INTERVALOS UTILIZANDO 0 COMO INICIAL
        linea_horizontal= ["0"]
        #CICLO PARA SABER EL VALOR DE CADA INTERVALO
        for intervalo in (lista_intervalo):
            dato= str(intervalo[0])
            linea_horizontal.append (dato)
        #ORGANIZA LA LISTA DE MENO A MAYOR
        linea_horizontal.sort()
        #CONVIERTE LA LISTA EN UNA LINEA HORIZONTAL
        linea_horizontal= "        ".join (linea_horizontal)     
        return (linea_horizontal)
    #METODO PARA DIBUJAR EL EJE Y
    def modiciador_vertical(self,lista_intervalo):
        #CREACION DE LISTA CON LA CUAL SE ALMACENA LA CANTIDAD LOS DATOS DE LA FRECUENCIA
        linea_vertical = []
        for intervalo in (lista_intervalo):
            dato= int(intervalo[1])
            linea_vertical.append (dato)
        #VARIABLE CON EL NUMERO MAS GRANDE DE LA LISTA
        numero_tope = int(max(linea_vertical)) 
        #IMPRIME LA LINEA VERTICAL CON CIERTOS VALORES
        contador= len(lista_intervalo)
        base =  len(lista_intervalo)
        for i in range (numero_tope,0,-1):
            
            for candidato in lista_intervalo:
                if (candidato [1]== i):
                    ubicacion = int(candidato [0])
                    if(contador > base):
                        diferencia= contador - base
                        mensaje = " |     |  " * diferencia
                        print ("\033["+"7;30;45"+"m "+"|",i, "|  "+"     " * ubicacion + "|¯¯¯¯¯| ", mensaje," \033[0m")
                        print ("\033["+"7;30;45"+"m "+"|"+ "     |  "+"     " * ubicacion+"|     | ", mensaje, " \033[0m")
                    else:
                        print ("\033["+"7;30;45"+"m "+"|",i, "|  "+"      "* ubicacion+"|¯¯¯¯¯|" +" \033[0m")
                        print ("\033["+"7;30;45"+"m "+"| "+ "    |  "+"      "* ubicacion+"|     |"+" \033[0m")
                    contador= contador + 1 

    def modificador_horizontal(self,lista_intervalo):
        lista_horizontal = []
        for cantidad in lista_intervalo:
            dato= str(cantidad[0])
            lista_horizontal.append (dato)
        dato_tope= int(len (lista_horizontal))
        mensaje= ("¯"*10)* dato_tope
        print ("\033["+"7;30;45"+"m"+" |    |"+mensaje+" \033[0m")

ejecutar_2 = accion_2()
lista=[[0,235],[2,435],[4,520],[5,598]]
ejecutar_2.dibujar(lista)
