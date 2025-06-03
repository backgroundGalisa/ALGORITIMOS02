def bucket_sort(lista):
    if not lista:
        return []

    minimo = min(lista)
    maximo = max(lista)
    intervalo = maximo - minimo

    n = len(lista)
    buckets = [[] for _ in range(n)]

    for num in lista:
        indice = int(((num - minimo) / intervalo) * (n - 1))
        buckets[indice].append(num)

    for i in range(n):
        buckets[i] = sorted(buckets[i])

    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado

num = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]

print('lista desordenada:', num)

ordenada = bucket_sort(num)

print('lista ordenada :', ordenada)


# Vantagens:
# - Muito rápido para valores uniformemente distribuídos.
# - Estável se o sort interno for estável.
# Desvantagens:
# - Desempenho depende da distribuição dos dados.
# - Pode desperdiçar memória.
# Uso recomendado: Indicado para números decimais uniformemente distribuídos