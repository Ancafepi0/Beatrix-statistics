class accion_4:
    #Constructor 
    def __init__(self):
        pass
    def dibujar (self,intervalos):
        valores_en_gragos=[]
        for i in intervalos:
            valores_en_gragos.append(i[1])
        self.insertador_de_colores(intervalos)
        intervalos = self.acomodador_grados(intervalos)
        W =  "\033[30m" + "W"
        a=  color=self.encontrar_color(intervalos)+";"
        b=  color=self.encontrar_color(intervalos)+";"
        c= color=self.encontrar_color(intervalos)+";"
        d=  color=self.encontrar_color(intervalos)+";"
        e= color=self.encontrar_color(intervalos)+";"
        f=  color=self.encontrar_color(intervalos)+";"
        g=  color=self.encontrar_color(intervalos)+";"
        h=  color=self.encontrar_color(intervalos)+";"
        a11= color=self.encontrar_color(intervalos)+";"
        a7= color=self.encontrar_color(intervalos)+";"
        i=  color=self.encontrar_color(intervalos)+";"
        j=  color=self.encontrar_color(intervalos)+";"
        k=  color=self.encontrar_color(intervalos)+";"
        l=  color=self.encontrar_color(intervalos)+";"
        m= color=self.encontrar_color(intervalos)+";"
        n= color=self.encontrar_color(intervalos)+";"
        o= color=self.encontrar_color(intervalos)+";"
        p= color=self.encontrar_color(intervalos)+";"
        a9= color=self.encontrar_color(intervalos)+";"
        q= color=self.encontrar_color(intervalos)+";"
        r= color=self.encontrar_color(intervalos)+";"
        s= color=self.encontrar_color(intervalos)+";"
        t= color=self.encontrar_color(intervalos)+";"
        u= color=self.encontrar_color(intervalos)+";"
        v= color=self.encontrar_color(intervalos)+";"
        w= color=self.encontrar_color(intervalos)+";"
        x= color=self.encontrar_color(intervalos)+";"
        a8= color=self.encontrar_color(intervalos)+";"
        y= color=self.encontrar_color(intervalos)+";"
        z= color=self.encontrar_color(intervalos)+";"
        a1= color=self.encontrar_color(intervalos)+";"
        a2= color=self.encontrar_color(intervalos)+";"
        a3= color=self.encontrar_color(intervalos)+";"
        a4= color=self.encontrar_color(intervalos)+";"
        a10=color=self.encontrar_color(intervalos)+";"
        a5= color=self.encontrar_color(intervalos)+";"
        a6= color=self.encontrar_color(intervalos)+";"

        print(W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W)
        print(W+W+W+W+W+W+W+W+W+W+W+W+a4+a10+a10+a10+a5+a5+a5+a6+a6+a6+a6+a6+a+a+a+a+a+a+b+b+b+b+b+b+b+c+W+W+W+W+W+W+W+W+W+W+W+W)
        print(W+W+W+W+W+W+W+W+W+W+a4+a4+a4+a4+a4+a10+a10+a5+a5+a5+a6+a6+a6+a6+a+a+a+a+a+b+b+b+b+b+c+c+c+c+c+W+W+W+W+W+W+W+W+W+W+W)            
        print(W+W+W+W+W+W+W+W+a3+a3+a3+a3+a4+a4+a4+a10+a10+a10+a5+a5+a6+a6+a6+a6+a+a+a+a+a+b+b+b+b+b+c+c+c+d+d+d+d+d+W+W+W+W+W+W+W+W)
        print(W+W+W+W+W+W+a2+a2+a2+a2+a3+a3+a3+a4+a4+a4+a4+a10+a10+a5+a5+a6+a6+a6+a+a+a+a+b+b+b+b+c+c+c+c+d+d+d+d+e+e+e+e+W+W+W+W+W+W)
        print(W+W+W+W+a1+a1+a2+a2+a2+a2+a2+a3+a3+a3+a3+a4+a4+a4+a10+a10+a5+a6+a6+a6+a+a+a+a+b+b+b+c+c+c+d+d+d+d+e+e+e+e+e+f+f+W+W+W+W+W)
        print(W+W+W+a1+a1+a1+a1+a1+a1+a2+a2+a2+a3+a3+a3+a3+a4+a4+a4+a10+a5+a5+a6+a6+a+a+a+b+b+b+c+c+c+d+d+d+d+e+e+e+f+f+f+f+f+h+h+W+W+W)
        print(W+W+z+z+z+z+a1+a1+a1+a1+a1+a2+a2+a2+a2+a3+a3+a3+a3+a4+a4+a5+a5+a6+a+a+b+b+c+c+d+d+d+d+e+e+e+e+f+f+f+f+f+g+g+g+g+W+W+W)
        print(W+W+y+y+y+z+z+z+z+z+a1+a1+a1+a2+a2+a2+a2+a2+a3+a3+a3+a4+a5+a6+a+a+b+c+d+d+d+e+e+e+e+e+f+f+f+g+g+g+g+g+g+h+h+h+W+W)
        print(W+y+y+y+y+z+z+z+z+z+z+z+a1+a1+a1+a1+a2+a2+a2+a2+a3+a4+a5+a6+a+a+b+c+d+e+e+e+f+f+f+f+g+g+g+g+g+g+g+g+h+h+h+h+h+W)
        print(W+y+y+y+y+y+y+y+z+z+z+z+z+z+a1+a1+a1+a1+a1+a2+a3+a4+a5+a6+a+a+b+c+d+e+f+f+f+f+g+g+g+g+g+g+h+h+h+h+h+h+a11+a11+a11+W)
        print(W+a8+a8+a8+a8+y+y+y+y+y+y+y+z+z+z+z+z+a1+a1+a2+a3+a4+a5+a6+a+a+b+c+d+e+f+f+g+g+g+g+g+h+h+h+h+h+a11+a11+a11+a11+a11+a11+a11+W)
        print(W+a8+a8+a8+a8+a8+a8+a8+a8+y+y+y+z+z+z+z+z+a1+a1+a2+a3+a4+a5+a6+a+a+b+c+d+e+f+f+g+g+g+g+g+a11+a11+a11+a11+a11+a11+a11+a11+a11+a11+a11+a11+W)
        print(W+x+x+x+x+x+x+x+x+x+x+x+v+v+v+v+v+u+u+t+s+r+q+p+o+o+n+m+l+k+j+j+i+i+i+i+i+a7+a7+a7+a7+a7+a7+a7+a7+a7+a7+a7+a7+W)
        print(W+x+x+x+x+x+x+x+v+v+v+v+v+v+u+u+u+u+u+t+s+r+q+p+o+o+n+m+l+k+j+j+j+j+j+i+i+i+i+i+a7+a7+a7+a7+a7+a7+a7+a7+a7+W)
        print(W+x+x+x+x+v+v+v+v+v+v+v+u+u+u+u+t+t+t+t+s+r+q+p+o+o+n+m+l+k+k+k+k+j+j+j+j+i+i+i+i+i+i+i+i+a7+a7+a7+a7+W)
        print(W+W+x+x+x+v+v+v+v+v+u+u+u+t+t+t+t+t+s+s+s+r+q+p+o+o+n+m+l+l+l+k+k+k+k+k+j+j+j+i+i+i+i+i+i+a7+a7+a7+W+W)
        print(W+W+v+v+v+v+u+u+u+u+u+t+t+t+t+s+s+s+s+r+r+q+q+p+o+o+n+n+m+m+l+l+l+l+k+k+k+k+j+j+j+j+j+i+i+i+i+W+W+W)
        print(W+W+W+u+u+u+u+u+u+t+t+t+s+s+s+s+r+r+r+q+q+q+p+p+o+o+o+n+n+n+m+m+m+l+l+l+l+k+k+k+j+j+j+j+j+i+W+W+W+W)
        print(W+W+W+W+u+u+t+t+t+t+t+s+s+s+s+r+r+r+q+q+q+a9+p+p+o+o+o+o+n+n+n+m+m+m+l+l+l+l+k+k+k+k+k+j+j+W+W+W+W+W)
        print(W+W+W+W+W+W+t+t+t+t+s+s+s+r+r+r+r+q+q+a9+a9+p+p+p+o+o+o+o+n+n+n+n+m+m+m+m+l+l+l+l+k+k+k+k+W+W+W+W+W+W)
        print(W+W+W+W+W+W+W+W+s+s+s+s+r+r+r+q+q+q+a9+a9+a9+p+p+p+o+o+o+o+o+n+n+n+n+n+m+m+m+l+l+l+l+l+W+W+W+W+W+W+W+W)
        print(W+W+W+W+W+W+W+W+W+W+r+r+r+r+r+q+q+a9+a9+a9+p+p+p+p+o+o+o+o+o+o+n+n+n+n+n+m+m+m+m+m+W+W+W+W+W+W+W+W+W+W)
        print(W+W+W+W+W+W+W+W+W+W+W+W+W+W+r+q+q+a9+a9+p+p+p+p+p+o+o+o+o+o+n+n+n+n+n+m+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W)
        print(W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W)


        # Código para reiniciar el color
        reset = "\033[0m"

        # Reiniciar el estilo para no afectar el resto de la salida del terminal
        print(reset)
        l=0
        for i in intervalos:
            print (i[2]+" COLOR \u2588 "+"NOMBRE = "+i[0]+" "+"VALOR EN GRADOS =  "+str(valores_en_gragos[l])+"°"+"\n")
            l +=1
        print(reset)
    def insertador_de_colores (self,intervalos):
        colores = [
            "\033[30m",  # Negro
            "\033[31m",  # Rojo
            "\033[32m",  # Verde
            "\033[33m",  # Amarillo
            "\033[34m",  # Azul
            "\033[35m",  # Magenta
            "\033[36m",  # Cian
            "\033[37m",  # Blanco
            "\033[90m",  # Gris oscuro
            "\033[91m",  # Rojo claro
            "\033[92m",  # Verde claro
            "\033[93m",  # Amarillo claro
            "\033[94m",  # Azul claro
            "\033[95m",  # Magenta claro
            "\033[96m",  # Cian claro
            "\033[97m",  # Blanco brillante
        ]
        for i in range (len(intervalos)):
            color = colores[i % len(colores)]
            intervalos[i].append (str(color))
    def redondear_a_decena_mas_cercana(numero):
        return round(numero / 10) * 10
    def acomodador_grados (self,intervalos):
        for sublista in intervalos:
            if (sublista[1] % 10 != 0): 
                sublista[1] = self.redondear_a_decena_mas_cercana(sublista[1])

        suma_total = sum(sublista[1] for sublista in intervalos)
        while suma_total > 360:
        # Encontrar el valor más grande
            max_sublista = max(intervalos, key=lambda x: x[1])
            # Restar 10 del valor más grande
            max_sublista[1] -= 10
            # Recalcular la suma total
            suma_total = sum(sublista[1] for sublista in intervalos)
        return intervalos
    def encontrar_color (self,intervalos):
        for i in intervalos:
            if (i[1]==0):
                continue
            elif(i[1]>0):
                i[1] -= 10
                return (i[2])
        return (intervalos[len(intervalos)-1][2])
                
        
ejecutar_4 = accion_4()
lista_intervalos = [["Lupe",60],["Lupe",60],["Lupe",60],["Lupe",60],["Lupe",60],["Lupe",60]]
ejecutar_4.dibujar(lista_intervalos)