#---->Operadores Aritmeticos
a,b = 3,5
#Suma
print(a + b)
#Resta
print(a - b)
#Division
print(a / b)
#Multiplicacion
print(a * b)
#Division Entera
print(a // b)
#Potencia
print(a ** b)
#Modulo
print(a % b)

#---->Operadores Relacionales
#Mayor que
print(a > b)
#Menor que
print(a < b)
#Igualdad
print(a == b)
#Menor igual que
print( a <= b)
#Mayor igual que
print(a >= b)
#Diferencia
print( a != b)

#---->Operadores Asignacion
#Asignacion
a = 10
print(a)
#Asignar suma
a += 10
print(a)
#Asignar resta
a-= 10
print(a)
#Asignar potencia
a**= 10
print(a)
#Asignar modulo
a %= 10
print(a)
#Asignar Division
a /= 10
print(a)
#Asignar Multiplicacion
a *= 10
print(a)
#Asignar division Entera
a //= 10
print(a)

#---->Operadores Logicos
a,b = False, True
#And (Y)
print(a and b)
#Or (O)
print(a or b)
#Not 
print(not b)

#---->Operadores Pertenencia
a = [1,2,3,4,5]
#In
print(1 in a)
#Not in
print(1 not in a)

#---->Operadores Identidad
a,b = 5,5
#Is
print(a is b)
#Not is
print(a is not b)

#---->Dificultad Extra
for x in range(10, 56, +2):
    if (x % 3 != 0 or x !=16):
        print(x)