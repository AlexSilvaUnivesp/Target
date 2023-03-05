# O programa deve calcular o percentual de representação que cada estado teve dentro do valor total.

fat_mensal = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

total = sum(fat_mensal.values())

print('Porcentagem de representação por estado:')

for estado, valor in fat_mensal.items():
    rep = (valor / total) * 100
    print(f'{estado:<7}: {rep:>5.2f}%', sep="")