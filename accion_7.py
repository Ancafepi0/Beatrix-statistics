class accion_7:
    def __init__(self):
        pass
    def dibujar (self,intervalos):
        lista_acomodar = [sublista[0] for sublista in intervalos]
        lista_con_intervalos= self.acomodar_lista(lista_acomodar)
        numero_de_intervalos=len(lista_con_intervalos)
        lista_con_nombre = [sublista[1] for sublista in intervalos]
        nombre_intervalo_grande= "landa1"
        intervalo_mas_grande= max(lista_con_intervalos)
        espacio_inter=2
        espacio=5
        if (len(nombre_intervalo_grande)>6):
            espacio=len(nombre_intervalo_grande)
        if (len(str(intervalo_mas_grande))>1):
            espacio_inter= len(str(intervalo_mas_grande))
        
        for i in range (numero_de_intervalos):         
            mensaje= []
            contador=numero_de_intervalos
            for j in  range(len(intervalos)):
                #PARA ESPACIO NORMAL
                if (intervalos[j][0]==lista_con_intervalos[i]):
                    forma_linea= "\u2500\u2500\u252C\u2500\u2500".center(espacio," ")
                    mensaje.append (forma_linea)
                elif (intervalos[j][0]>  lista_con_intervalos[i]):
                    forma_linea = "\u2502".center(espacio," ")
                    mensaje.append (forma_linea)
                else:
                    forma_linea = "\u2800".center(espacio," ")
                    mensaje.append (forma_linea)
                #PARA ESPACIO INTERMEDIO
                if (contador >= 0):
                    try:
                        forma_linea = self.determinar_espacio_intermedio(lista_con_intervalos[i],intervalos[j][0],intervalos[j+1][0])
                    except (IndexError):
                        forma_linea = self.determinar_espacio_intermedio(lista_con_intervalos[i],intervalos[j][0],intervalos[j][0])
                        
                    mensaje.append (forma_linea)
                    contador-=1

            linea_contructura= ("") .join (mensaje)
            print ("\033["+"7;30;45"+"m "+ (" ").center(espacio_inter+1," ") +" "+" "+linea_contructura+" ".center(espacio_inter,"\u2800")+"\033[0m")
        print ("\033["+"7;30;45"+"m "+" ".center(espacio_inter," ")+("\u2501")+"\u2501"+((("\u2501")+('\u2501')+('\u2501')+("\u2533")+('\u2501')+('\u2501')).center(espacio+1,"\u2501"))*(len(lista_acomodar))+" ".center(espacio_inter+1," ")+"\033[0m")
        contador=[]
        num_contador=0
        for i in range (len(lista_con_nombre)):
            lista_con_nombre[i]=str(lista_con_nombre[i]).center(espacio,"\u2800")
            
            if (num_contador == 0):
                extra=("\u03BC"+"-"+"3\u03C3").center(espacio,"\u2800")
                contador.append((extra))
            elif (num_contador == 1):
                extra=("\u03BC"+"-"+"2\u03C3").center(espacio,"\u2800")
                contador.append((extra))
            elif (num_contador == 2):
                extra=("\u03BC"+"-"+"1\u03C3").center(espacio,"\u2800")
                contador.append((extra))
            elif (num_contador == 3):
                extra="\u03C3".center(espacio,"\u2800")
                contador.append((extra))
            elif (num_contador == 4):
                extra=("\u03BC"+"+"+"1\u03C3").center(espacio,"\u2800")
                contador.append((extra))
            elif (num_contador == 5):
                extra=("\u03BC"+"+"+"2\u03C3").center(espacio,"\u2800")
                contador.append((extra))
            elif (num_contador == 6):
                extra=("\u03BC"+"+"+"3\u03C3").center(espacio,"\u2800")
                contador.append((extra))

            num_contador +=1
        linea_intervalos= ((" "))  .join (contador)

        print ("\033["+"7;30;45"+"m"+" ".center(espacio+2,"\u2800")+linea_intervalos+" ".center(espacio-3,"\u2800")+"\033[0m")
        for i in  range (len(lista_con_nombre)):
            if(i== 0):
                extra = contador[i]
            elif (i==1):
                extra = contador[i]
            elif (i==2):
                extra = contador[i]
            elif (i==3):
                extra = contador[i]
            elif (i==4):
                extra = contador[i]
            elif (i==5):
                extra = contador[i]
            elif (i==6):
                extra = contador[i]

            print ("\033["+"7;30;45"+"m "+ extra +" = "+lista_con_nombre[i] +"\u2800"+"\033[0m") 

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
    def determinar_espacio_intermedio (self,fr,fri,frd):
        if (fr >=fri):
            izquierda = True
        else:
            izquierda = False
        if (fr >= frd):
            derecha = True
        else:
            derecha = False
        if (izquierda== True and derecha ==False):
            if (fri==fr):
                return("\u256F") #UNICODE DE FORMA ╯
            elif (frd==fr):
                return("b\u2517")
            else:
                return("\u2502") #UNICODE DE FORMA ┃
        if (izquierda== False and derecha ==True):
            if (fri==fr):
                return("d\u251B")
            elif (frd==fr):
                return("\u2570") #UNICODE DE FORMA ╰
            else:
                return("\u2502") #UNICODE DE FORMA ┃
        if (izquierda== False and derecha ==False):
            return("\u2800") #UNICODE DE FORMA ┃ 
        if (izquierda== True and derecha ==True) :
            if (fri > fr and frd >fr):
                return("\u2800") #UNICODE DE FORMA VACIA
            if (fri == fr and frd ==fr):
                return("\u2500") #UNICODE DE FORMA ━
            if (fri > frd):
                if (fri==fr):
                    return("\u256E") #UNICODE DE FORMA ╮
                elif (frd==fr):
                    return("\u2517")
                else:
                    return("\u2800") #UNICODE DE FORMA VACIA
            if (frd>fri):
                if (fri==fr):
                    return("\u251B")
                elif (frd==fr):
                    return("\u256D") #UNICODE DE FORMA ╭
                else:
                    return("\u2800") #UNICODE DE FORMA VACIA
        return("\u2800")

nueva_accion = accion_7 ()
intervalos_prueba= [[19,22.8], [20,23.9], [22,24.5], [21,25.0], [19,26.1],[17,27],[15,28]]
nueva_accion.dibujar (intervalos_prueba)
