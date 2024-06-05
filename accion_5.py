class accion_5:
    #Constructor 
    def __init__(self):
        pass

    def dibujar (self,intervalos):
        lista_acomodar = [sublista[1] for sublista in intervalos]
        lista_con_intervalos= self.acomodar_lista(lista_acomodar)
        intervalo_mas_grande= max(lista_con_intervalos)
        espacio_inter=2
        espacio=5

        lista_para_bolitas = []
        if (len(str(intervalo_mas_grande))>1):
            espacio_inter= len(str(intervalo_mas_grande))

        for i in range (len(lista_con_intervalos)):
            contador=0         
            for j in range (len(intervalos)): 
                if (intervalos[j][1]==lista_con_intervalos[i]):
                     contador += 1 
            lista_para_bolitas.append(contador)

        max_valor = max(lista_para_bolitas)
        for i in range (max_valor):         
            mensaje= []
            
            for j in range (len(lista_con_intervalos)): 
                if (max_valor==lista_para_bolitas[j]):
                    forma_linea = "\u26AA".center(espacio," ") 
                    mensaje.append(forma_linea)
                elif (max_valor<lista_para_bolitas[j]):
                    forma_linea = "\u26AA".center(espacio," ") 
                    mensaje.append(forma_linea)
                elif (max_valor>lista_para_bolitas[j]):
                    forma_linea = "\u2800".center(espacio+1," ")
                    mensaje.append(forma_linea)
                else :
                    forma_linea = "\u2800".center(espacio," ")
                    mensaje.append(forma_linea)    
            max_valor-=1     
            linea_contructura= ("") .join (mensaje)
            print ("\033["+"7;30;45"+"m "+ " ".center(espacio_inter," ") +" "+linea_contructura+" ".center(espacio_inter,"\u2800")+"\033[0m")
        print ("\033["+"7;30;45"+"m "+" ".center(espacio_inter," ")+("\u2501")+(("\u2501")+('\u2501')+('\u2501')+('\u2501'))*(len(lista_acomodar))+" ".center(espacio_inter," ")+"\033[0m")
        for i in range (len(lista_con_intervalos)):
            lista_con_intervalos[i]=str(lista_con_intervalos[i]).center(espacio+1,"\u2800")
        linea_intervalos= ("") .join (lista_con_intervalos)

        print ("\033["+"7;30;45"+"m"+" ".center(espacio,"\u2800")+linea_intervalos+" ".center(espacio-4,"\u2800")+"\033[0m")

    def acomodar_lista(self, intervalos):
    # Eliminar duplicados convirtiendo la lista a un conjunto
        conjunto_intervalos = set(intervalos)
        lista_ordenada = list(conjunto_intervalos)
    
    # Implementar el algoritmo de ordenamiento burbuja para ordenar de mayor a menor
        n = len(lista_ordenada)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_ordenada[j] > lista_ordenada[j+1]:  
                    lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    
        return lista_ordenada 
ejecutar_5 = accion_5()
intervalos = [['1',7,1,3,4,5,14],['1',2,1,45,89,456,1234],['1',5,1,45,89,456,1234],['1',4,4,45,89,456,1234],['1',5,1,45,89,456,1234],['1',5,1,45,89,456,1234]]
ejecutar_5.dibujar(intervalos)
