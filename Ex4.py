import json

valores = '{"SP":67836.43,"RJ":36678.66,"MG":29229.88,"ES":27165.48,"OUTROS":19849.53}'
dados = json.loads(valores)

valorTotal = 0

for d in dados:
    valorTotal += float(dados[d])

print(("\n\tParicipação de SP -> {SP:.1f}%\n\tParicipação de RJ -> {RJ:.1f}%\n\tParicipação de MG -> {MG:.1f}%\n\tParicipação de ES -> {ES:.1f}%\n\tParicipação de OUTROS -> {OUTROS:.1f}%\n\t")
      .format(SP=float(dados['SP'])/valorTotal*100,RJ=float(dados['RJ'])/valorTotal*100,MG=float(dados['MG'])/valorTotal*100,ES=float(dados['ES'])/valorTotal*100,OUTROS=float(dados['OUTROS'])/valorTotal*100,))