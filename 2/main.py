#Funciones
def imprimir():
    print("Hola Mundo")
imprimir()

def imprimirRetornar():
    return "Hola Mundo"
print(imprimirRetornar())

def imprmirParametros(nombre):
    print(f"Hola {nombre}")
    
def retornarVariosParametros():
    return "Juan","Herrera"

a,b = retornarVariosParametros()
print(f"Mi nombre {a} {b}")

def imprimirJAJA():
    def impirmirImprimir():
        print("Función interna: Hola, Python !")
    impirmirImprimir()

imprimirJAJA()


#Funciones del Sistema
#Len
print(len("JuanJose"))
#Type
print(type(36))
#Upper
print("JuanJose".upper())
#Str
print(type(str(36)))

#
def colombiaMeHizoPerder20k(james, quintero):
    goles = 0
    for arquero in range(1, 101):
        if arquero % 3 == 0 and arquero % 5 == 0:
            print(f"{arquero} : {james} {quintero}")
        elif arquero % 3 == 0:
            print (f"{arquero} :{james}")  
        elif arquero % 5 == 0: 
            print (f"{arquero} : {quintero}")
        else:
            print(arquero)
            goles += 1
    return goles

print(colombiaMeHizoPerder20k("Cheque","Kiki"))          