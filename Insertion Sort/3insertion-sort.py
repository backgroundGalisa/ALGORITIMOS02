def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j>=0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

num = [3,4,2,1,5,6,7]

print('lista desordenada:', num)

ordenada = insertion_sort(num)

print('lista ordenada:', ordenada)




# Vantagens:
# - Simples e eficiente para listas pequenas ou quase ordenadas.
# - Estável e in-place.
# Desvantagens:
# - Ineficiente para listas grandes (O(n²)).
# Uso recomendado: Útil para pequenas quantidades de dados, ou como parte de algoritmos híbridos.
