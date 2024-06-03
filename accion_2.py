class accion_1:
    def __init__(self):
        pass
    def dibujar (self,intervalos):
        lista_acomodar = [sublista[0] for sublista in intervalos]
        lista_con_intervalos= self.acomodar_lista(lista_acomodar)
        numero_de_intervalos=len(lista_con_intervalos)
        lista_con_nombre = [sublista[1] for sublista in intervalos]
        nombre_intervalo_grande= max(lista_con_nombre, key=len)
        espacio=5
        if (len(nombre_intervalo_grande)>5):
            espacio=len(nombre_intervalo_grande)
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
                    forma_linea = "     ".center(espacio," ")
                    mensaje.append (forma_linea)

            linea_contructura= ("") .join (mensaje)
            print ("\033["+"7;30;45"+"m "+ str(lista_con_intervalos[i]) +"\u2523"+" "+linea_contructura+" "+"\033[0m")
        print ("\033["+"7;30;45"+"m "+(" \u2517")+((("\u2501")+('\u253B')+('\u2501')+("\u2533")+('\u2501')+('\u253B')).center(espacio,"\u2501"))*(numero_de_intervalos+1)+" "+" \033[0m")
        for i in range (len(lista_con_nombre)):
            lista_con_nombre[i]=str(lista_con_nombre[i]).center(espacio," ")
        linea_intervalos= ("") .join (lista_con_nombre)

        print ("\033["+"7;30;45"+"m "+"  "+linea_intervalos+"\033[0m")

    def acomodar_lista(self, intervalos):
    # Eliminar duplicados convirtiendo la lista a un conjunto
        conjunto_intervalos = set(intervalos)
        lista_ordenada = list(conjunto_intervalos)
    
    # Implementar el algoritmo de ordenamiento burbuja para ordenar de mayor a menor
        n = len(lista_ordenada)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_ordenada[j] < lista_ordenada[j+1]:  # Cambiar '>' a '<'
                    lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    
        return lista_ordenada


nueva_accion = accion_1 ()
intervalos_prueba= [[1,"JAIME"],[4,"TULIO"],[3,"RODRIGO"],[9,"FABIAN"],[0,"norman"],[9,"luna"]]
nueva_accion.dibujar (intervalos_prueba)