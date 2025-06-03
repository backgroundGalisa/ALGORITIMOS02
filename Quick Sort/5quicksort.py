def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]

    menores = [x for x in lista[1:] if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)


num = [5,22,1,66,5,4,6]

print('lista desordenada :', num)

ordenada = quick_sort(num)

print('lista ordenada :', ordenada)


# Vantagens:
# - Muito rápido na prática (média O(n log n)).
# - In-place.
# Desvantagens:
# - Pior caso é O(n²), embora raro.
# - Não é estável.
# Uso recomendado: Um dos mais usados na prática por sua performance.