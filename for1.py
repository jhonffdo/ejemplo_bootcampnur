'''for i in range(5): #arranca desde cero
    print(i**2)
print("fin del programa")  


#for i in range(2,20,2) #muestra los numero pares de 2 en 2
for i in range(1,11):#es 11 porque es un dato menosal imprimir
    print(i,'*5',5*i)
print("fin")    

for i in range(100,4,-5):#es descendente, loq le quito es negativo
    print(i)
print("fin")    

lista_verduras=["cebolla","papa","tomate"]
for x in range(len(lista_verduras)):
    print(lista_verduras[x]) #imprime en cada posicion de la lista
print("fin")

#escribir un prog q pregunte al usuario su edad
#y muestre por pantalla todos los años que ha cumplido
#desde 1 hasta su edad
edad=int (input("ingresa tu edad :"))
for i in range(1,edad+1):
    print(i)
    '''
#ejer 4
#cuantos años cumpli por cada año
cont=0
sum=0
nac=0
nac=int(input("digite su año de nacimiento:"))
edad=int (input("ingresa tu edad :"))
for i in range(1,edad):
    cont=cont+edad
    sum=cont+nac
    nac=nac+1
    print( "en el año",nac,"cumpliste",i)