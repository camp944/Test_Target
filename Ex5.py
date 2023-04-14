texto = str(input("Insira o texto que deseja inverter: "))

lista = list(texto)
lista_Inv = ""
cont = len(lista)-1


while cont >= 0 :

    lista_Inv+=lista[cont]
    cont -= 1

print(lista_Inv)



