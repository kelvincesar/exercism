def quicksort(arr, left, right):
    if left < right:
        print(arr[left:right+1])
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot-1)
        quicksort(arr, pivot+1, right)

def partition(arr, left, right):
    # escolha ultima posição como pivot
    # atinge sempre o worst case caso o array
    # já esteja ordenado
    pivot = arr[right]

    # index do menor elemento e indica a posição a direita do pivot 
    i = left-1

    # percorre o array e move todos os menores valores
    # para o lado da esquerda. elemento de left até i, são menores após
    # cada iteração
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # move o pivot para depois dos menores lementos
    # e retorna a sua posição
    arr[i+1], arr[right] = arr[right], arr[i+1]
    
    return i+1

arr = [0,3,6,7,8,4,2,1,5]
quicksort(arr, 0, len(arr)-1)