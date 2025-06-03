def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1  
    direita = 2 * i + 2   
    
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i] 
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)


    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)


    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)

num = [4, 10, 3, 5, 1]

print('lista desordenada:', num)

heap_sort(num)

print('lista ordenada :', num)

# Vantagens:
# - Complexidade garantida de O(n log n).
# - Não requer memória extra.
# Desvantagens:
# - Não é estável.
# - Menos eficiente que Quick Sort na prática.
# Uso recomendado: Bom quando memória constante é necessária.
