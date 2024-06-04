class accion_1:
    def __init__(self):
        pass
    def dibujar (self,intervalos):
        lista_acomodar = [sublista[0] for sublista in intervalos]
        lista_con_intervalos= self.acomodar_lista(lista_acomodar)
        numero_de_intervalos=len(lista_con_intervalos)
        lista_con_nombre = [sublista[1] for sublista in intervalos]
        nombre_intervalo_grande= max(lista_con_nombre, key=len)
        intervalo_mas_grande= max(lista_con_intervalos)
        espacio_inter=2
        espacio=6
        if (len(nombre_intervalo_grande)>6):
            espacio=len(nombre_intervalo_grande)
        if (len(str(intervalo_mas_grande))>1):
            espacio_inter= len(str(intervalo_mas_grande))
        for i in range (numero_de_intervalos):         
            mensaje= []
            for j in  intervalos:
                if (j[0]==lista_con_intervalos[i]):
                    forma_linea= "\u250F\u2501\u2501\u2501\u2513".center(espacio," ")
                    mensaje.append (forma_linea)
                elif (j[0]>  lista_con_intervalos[i]):
                    forma_linea = "\u2503   \u2503".center(espacio," ")
                    mensaje.append (forma_linea)
                else:
                    forma_linea = "\u2800".center(espacio," ")
                    mensaje.append (forma_linea)

            linea_contructura= ("") .join (mensaje)
            print ("\033["+"7;30;45"+"m "+ str(lista_con_intervalos[i]).center(espacio_inter," ") +"\u2523"+" "+linea_contructura+" ".center(espacio_inter,"\u2800")+"\033[0m")
        print ("\033["+"7;30;45"+"m "+" ".center(espacio_inter," ")+("\u2517")+((("\u2501")+('\u253B')+('\u2501')+("\u2533")+('\u2501')+('\u253B')).center(espacio,"\u2501"))*(len(lista_acomodar))+" ".center(espacio_inter+1," ")+"\033[0m")
        for i in range (len(lista_con_nombre)):
            lista_con_nombre[i]=str(lista_con_nombre[i]).center(espacio,"\u2800")
        linea_intervalos= ("") .join (lista_con_nombre)

        print ("\033["+"7;30;45"+"m"+" ".center(espacio_inter+2,"\u2800")+linea_intervalos+" ".center(espacio_inter+1,"\u2800")+"\033[0m")

    def acomodar_lista(self, intervalos):
    # Eliminar duplicados convirtiendo la lista a un conjunto
        conjunto_intervalos = set(intervalos)
        lista_ordenada = list(conjunto_intervalos)
    
    # Implementar el algoritmo de ordenamiento burbuja para ordenar de mayor a menor
        n = len(lista_ordenada)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_ordenada[j] < lista_ordenada[j+1]:  
                    lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    
        return lista_ordenada


nueva_accion = accion_1 ()
intervalos_prueba= [[11234,"J"],[42,"T"],[3,"R"],[2,"F"],[1,"N"],[9,"L"]]
nueva_accion.dibujar (intervalos_prueba)
