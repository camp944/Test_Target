#Calcula os valores solictados com base no arquivo json

import json

file = open('dados.json')
dados  = json.load(file)



def calculos(dados:any):
    mediaMensal = 0
    DaysCount = 0

    min_Val = float(dados[0]['valor'])
    max_Val = min_Val

    for n in dados:
        DaysCount+=1
        mediaMensal += float(float(n['valor']))

        if float(n['valor']) < min_Val:
            min_Val = float(n['valor'])
        if float(n['valor']) > max_Val:
            max_Val = float(n['valor'])



    mediaMensal /= DaysCount

    DaysCount = 0
    for n in dados:
        if float(n['valor']) > mediaMensal:
            DaysCount+=1

    print(("\n\tMenor valor de faturamento mensal -> R${min_Val:.2f}\n\tMaior valor de faturamento mensal -> R${max_Val:.2f}\n\tNúmero de dias em que o faturamento superou o a média mensal -> {DaysCount}\n").format(min_Val=min_Val,max_Val=max_Val,DaysCount=DaysCount))
    

calculos(dados)

