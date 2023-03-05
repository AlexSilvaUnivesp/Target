import json
#inicializar variáveis
maior_valor, dias_acima, dias_fat, valor_total = 0, 0, 0, 0
valores = []

with open ('dados.json' , 'r') as lista_dados:
    dados = json.load(lista_dados)
    valores = [x['valor'] for x in dados]
    maior_valor = max(valores)
    menor_valor = maior_valor
    for i in dados:
        if i['valor'] > 0:
            dias_fat += 1
            valor_total += i['valor']
            if i['valor'] < menor_valor:
                menor_valor = i["valor"]
    media = valor_total / dias_fat    
    
    dias_acima = 
    print(f'O maior valor faturado foi R$ {maior_valor:>8.2f}')
    print(f'O menor valor faturado foi R$ {menor_valor:>8.2f}')
    print(valor_total)
