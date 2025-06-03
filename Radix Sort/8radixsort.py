def counting_sort_por_digito(lista, digito):
    n = len(lista)
    output = [0] * n
    contagem = [0] * 10

    for numero in lista:
        indice = (numero // digito) % 10
        contagem[indice] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    for i in range(n - 1, -1, -1):
        indice = (lista[i] // digito) % 10
        output[contagem[indice] - 1] = lista[i]
        contagem[indice] -= 1

    for i in range(n):
        lista[i] = output[i]

def radix_sort(lista):
    if not lista:
        return

    maior = max(lista)

    digito = 1
    while maior // digito > 0:
        counting_sort_por_digito(lista, digito)
        digito *= 10

num = [170, 45, 75, 90, 802, 24, 2, 66]

print('lista desordenada:', num)

radix_sort(num)

print('lista ordenada :', num)



# Vantagens:
# - Ordenação linear para inteiros (O(nk), onde k é o número de dígitos).
# - Estável.
# Desvantagens:
# - Limitado a inteiros ou strings.
# - Requer memória extra.
# Uso recomendado: Útil para números inteiros ou dados estruturados com tamanho fixo.