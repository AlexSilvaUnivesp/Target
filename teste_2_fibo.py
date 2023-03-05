primeiro = 0
segundo = 1
atual = 0
fibo = False

num = int(input("Digite um número: "))

while atual <= num:
    if num == atual:
        fibo = True
        break
    else:
        atual = primeiro + segundo
        primeiro = segundo
        segundo = atual

if fibo:
    print("O número informado pertence à sequencia de Fibonacci.")
else:
    print("O número informado não pertence à sequencia de Fibonacci.")
