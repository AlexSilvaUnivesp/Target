import json

dias_fat, valor_total = 0, 0

with open ('dados.json' , 'r') as lista_dados:
    dados = json.load(lista_dados)
    
    # Cria uma lista apenas com os valores para facilitar o cálculo do valor máximo
    valores = [x['valor'] for x in dados]
    maior_valor = max(valores)
    dia_maior = valores.index(maior_valor) + 1

    # Para calcular o menor valor, iniciamos com o maior valor e vamos comparando com os valores acima de 0
    # Aproveitamos para somar o valor total e calcular quantos dias houve faturamento
    menor_valor = maior_valor
    for i in dados:
        if i['valor'] > 0:
            dias_fat += 1
            valor_total += i['valor']
            if i['valor'] < menor_valor:
                menor_valor = i['valor']
                dia_menor = i['dia']

    media = valor_total / dias_fat    
    dias_acima = len([i for i in valores if i > media])

    print(f'Maior valor faturado: R$ {maior_valor:>8.2f} no dia {dia_maior}')
    print(f'Menor valor faturado: R$ {menor_valor:>8.2f} no dia {dia_menor}')
    print('Dias com faturamento acima da média: ', dias_acima, 'dias')