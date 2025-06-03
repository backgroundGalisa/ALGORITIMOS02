def selection_sort(lista):
    for i in range(len(lista)):
        indice_minimo = i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

num = [6,2,5,77,1,34,12]

print('lista desordenada:', num)

ordenada = selection_sort(num)

print('lista ordenada:', ordenada)




# Vantagens:
# - Fácil de implementar.
# - Não requer memória extra (in-place).
# - Faz poucas trocas, útil quando trocar é caro. 
# Desvantagens:
# - Muito lento para listas grandes (complexidade O(n²)).
# - Não é estável.
# Uso recomendado: Recomendado apenas para fins educacionais ou listas muito pequenas.