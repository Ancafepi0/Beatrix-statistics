class accion_6:
    def __init__(self):
        pass
    def dibujar (self,intervalos):
        lista_odernar = []

        for mini_intervalo in intervalos:
            lista_odernar.extend(mini_intervalo)

        lista_odernar = self.redondear(lista_odernar) 
        limite_inferior_1= ("\033["+"7;30;45"+"m"+("\u2800")*(len(lista_odernar)*2)+"\u2503"+("\u2800")*((lista_odernar[1]-lista_odernar[0])+5)+"\033[0m")
        limite_inferior_2= ("\033["+"7;30;45"+"m"+("\u2800")*(len(lista_odernar)*2)+"\u2503"+("\u2800")*((lista_odernar[1]-lista_odernar[0])+5)+"\033[0m")
        limite_inferior_3= ("\033["+"7;30;45"+"m"+("\u2800")*(len(lista_odernar)*2)+"\u2503"+("\u2800")*((lista_odernar[1]-lista_odernar[0])+5)+"\033[0m")
        quartil_uno_1=  ("\033["+"7;30;44"+"m"+"\u250F"+"\033[0m")+("\033["+"7;30;44"+"m"+("\u2501")*((lista_odernar[2]-lista_odernar[1])+5)+"\033[0m")
        quartil_uno_2=  ("\033["+"7;30;44"+"m"+"\u2503"+"\033[0m")+("\033["+"7;34;46"+"m"+("\u2800")*((lista_odernar[2]-lista_odernar[1])+5)+"\033[0m")
        quartil_uno_3=  ("\033["+"7;30;44"+"m"+"\u2517"+"\033[0m")+("\033["+"7;30;44"+"m"+("\u2501")*((lista_odernar[2]-lista_odernar[1])+5)+"\033[0m")
        quartil_dos_1=  ("\033["+"7;30;44"+"m"+("\u2501")*((lista_odernar[3]-lista_odernar[2])+5)+"\033[0m")+("\033["+"7;30;47"+"m"+"\u2533"+"\033[0m")
        quartil_dos_2=  ("\033["+"7;34;46"+"m"+("\u2800")*((lista_odernar[3]-lista_odernar[2])+5)+"\033[0m")+("\033["+"7;30;47"+"m"+"\u2503"+"\033[0m")
        quartil_dos_3=  ("\033["+"7;30;44"+"m" +("\u2501")*((lista_odernar[3]-lista_odernar[2])+5)+"\033[0m")+("\033["+"7;30;47"+"m"+"\u253B"+"\033[0m")
        quartil_tres_1=  ("\033["+"7;30;47"+"m"+("\u2501")*((lista_odernar[4]-lista_odernar[3])+5)+"\033[0m")+("\033["+"7;30;47"+"m"+"\u2513"+"\033[0m")
        quartil_tres_2=  ("\033["+"7;37;46"+"m"+("\u2800")*((lista_odernar[4]-lista_odernar[3])+5)+"\033[0m")+("\033["+"7;30;47"+"m"+"\u2503"+"\033[0m")
        quartil_tres_3=  ("\033["+"7;30;47"+"m"+("\u2501")*((lista_odernar[4]-lista_odernar[3])+5)+"\033[0m")+("\033["+"7;30;47"+"m"+"\u251B"+"\033[0m")
        limite_superior_1= ("\033["+"7;30;45"+"m"+("\u2800")*((lista_odernar[1]-lista_odernar[0])+5)+"\u2503"+("\u2800")*(len(lista_odernar)*2)+"\033[0m")
        limite_superior_2= ("\033["+"7;30;45"+"m"+("\u2800")*((lista_odernar[1]-lista_odernar[0])+5)+"\u2503"+("\u2800")*(len(lista_odernar)*2)+"\033[0m")
        limite_superior_3= ("\033["+"7;30;45"+"m"+("\u2800")*((lista_odernar[1]-lista_odernar[0])+5)+"\u2503"+("\u2800")*(len(lista_odernar)*2)+"\033[0m")
        primera_linea= "" .join ([limite_inferior_1,
                                   quartil_uno_1,
                                   quartil_dos_1,
                                   quartil_tres_1,
                                   limite_superior_1])
        segunda_linea="" .join ([limite_inferior_2,
                                   quartil_uno_2,
                                   quartil_dos_2,
                                   quartil_tres_2,
                                   limite_superior_2])
        tercera_linea="" .join ([limite_inferior_3,
                                   quartil_uno_3,
                                   quartil_dos_3,
                                   quartil_tres_3,
                                   limite_superior_3])
        salto_linea= ("\033["+"7;30;45"+"m"+"\u2800"*(len(lista_odernar)*11-1)+"\033[0m")

        linea_horizontal_inicio= ("\033["+"7;30;45"+"m"+("\u2501")*(len(lista_odernar)*2)+"\u254B"+("\u2501")*((lista_odernar[1]-lista_odernar[0])+5)+"\033[0m")
        linea_horizontal_limite_menor=("\033["+"7;30;45"+"m"+"\u254B"+"\033[0m")+("\033["+"7;30;45"+"m"+("\u2501")*((lista_odernar[2]-lista_odernar[1])+5)+"\033[0m")
        linea_horizontal_quartil_1=("\033["+"7;30;45"+"m"+("\u2501")*((lista_odernar[3]-lista_odernar[2])+5)+"\033[0m")+("\033["+"7;30;45"+"m"+"\u254B"+"\033[0m")
        linea_horizontal_quartil_2=("\033["+"7;30;45"+"m"+("\u2501")*((lista_odernar[4]-lista_odernar[3])+5)+"\033[0m")+("\033["+"7;30;45"+"m"+"\u254B"+"\033[0m")
        linea_horizontal_quartil_3 = ("\033["+"7;30;45"+"m"+("\u2501")*((lista_odernar[1]-lista_odernar[0])+5)+"\u254B"+("\u2501")*(len(lista_odernar)*2)+"\033[0m")
        linea_horizontal= "" .join([linea_horizontal_inicio,
                                    linea_horizontal_limite_menor,
                                    linea_horizontal_quartil_1,
                                    linea_horizontal_quartil_2,
                                    linea_horizontal_quartil_3,
                                    
                                    ]
                                    )
        linea_horizontal_inicio= ("\033["+"7;30;45"+"m"+("\u2800")*(len(lista_odernar)*2)+"1"+("\u2800")*((lista_odernar[1]-lista_odernar[0])+5)+"\033[0m")
        linea_horizontal_limite_menor=("\033["+"7;30;45"+"m"+"2"+"\033[0m")+("\033["+"7;30;45"+"m"+("\u2800")*((lista_odernar[2]-lista_odernar[1])+5)+"\033[0m")
        linea_horizontal_quartil_1=("\033["+"7;30;45"+"m"+("\u2800")*((lista_odernar[3]-lista_odernar[2])+5)+"\033[0m")+("\033["+"7;30;45"+"m"+"3"+"\033[0m")
        linea_horizontal_quartil_2=("\033["+"7;30;45"+"m"+("\u2800")*((lista_odernar[4]-lista_odernar[3])+5)+"\033[0m")+("\033["+"7;30;45"+"m"+"4"+"\033[0m")
        linea_horizontal_quartil_3 = ("\033["+"7;30;45"+"m"+("\u2800")*((lista_odernar[1]-lista_odernar[0])+5)+"5"+("\u2800")*(len(lista_odernar)*2)+"\033[0m")
        linea_con_numeros= "" .join([linea_horizontal_inicio,
                                    linea_horizontal_limite_menor,
                                    linea_horizontal_quartil_1,
                                    linea_horizontal_quartil_2,
                                    linea_horizontal_quartil_3,
                                    
                                    ]
                                    )
        print (salto_linea+"\n"+primera_linea+"\n"+segunda_linea+"\n"+tercera_linea+"\n"+salto_linea+"\n"+salto_linea+"\n"+linea_horizontal+"\n"+linea_con_numeros)
        for i in range (5):
            if (i == 0):
                extra = "Limite inferior"
            elif (i==1):
                extra = "Quartil 1"
            elif (i==2):
                extra = "Quartil 2"
            elif (i==3):
                extra = "Quartil 3"
            elif (i==4):
                extra = "Limite superior"

            print ("\033["+"7;30;45"+"m"+str(i+1)+" = "+extra+" = "+str(intervalos[0][i])+"\033[0m")
    def redondear(self,lista_odernar):
        for i in range (len(lista_odernar)):
            lista_odernar[i]= self.redondear_al_entero_mas_cercana(lista_odernar[i])
        return (lista_odernar)
    def redondear_al_entero_mas_cercana(self,numero):
        return round(numero) 
nueva_accion = accion_6 ()
intervalos_prueba= [[23.8, 25.9, 27.5, 27.0, 26.1]]
nueva_accion.dibujar (intervalos_prueba)
