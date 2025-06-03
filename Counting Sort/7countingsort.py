def counting_sort(lista):
    if not lista:
        return []

    maior = max(lista)

    contagem = [0] * (maior + 1)

    for numero in lista:
        contagem[numero] += 1

    resultado = []
    for numero, qtd in enumerate(contagem):
        resultado.extend([numero] * qtd)

    return resultado

num = [4, 2, 2, 8, 3, 3, 1]

print('lista desordenada:', num)

ordenada = counting_sort(num)

print('lista ordanada :', ordenada)



# Vantagens:
# - Muito rápido para inteiros em um intervalo pequeno (O(n)).
# - Estável.
# Desvantagens:
# - Requer memória proporcional ao maior valor.
# - Só funciona com inteiros não-negativos.
# Uso recomendado: Ideal para contagens e dados discretos em intervalos curtos.