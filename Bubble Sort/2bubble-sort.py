def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

num = [3,4,2,1,5,6,7]

print('lista desordenada:', num)

ordenada = bubble_sort(num)

print('lista ordenada:', ordenada)



# Vantagens:
# - Muito simples de entender e implementar.
# - Estável.
# Desvantagens:
# - Um dos algoritmos mais lentos (O(n²)).
# Uso recomendado: Bom para fins didáticos, mas nunca usado em produção.