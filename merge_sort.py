def merge_sort(order_List):
    if len(order_List) > 1:  # caso de  uso
        mid = len(order_List) // 2
        left = order_List[:mid]
        right = order_List[mid:]
        print(f'division de lista:izquierda-->{left}, derecha-->{ right}')
        # llamada  recursiva
        merge_sort(left)
        merge_sort(right)
        # iteradores que  recorren  la division
        i = 0
        j = 0
        # iterador de  la  lista =>order_List
        k = 0

        # bucle  principal  comparativo division derecha e izquierda
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:

                order_List[k] = left[i]

                i += 1
            else:
                order_List[k] = right[j]
                j += 1

            k += 1

        if i < len(left):
            order_List[k] = left[i]
            i += 1
            k += 1

        if j < len(right):
            order_List[k] = right[j]
            j += 1
            k += 1
        return order_List


if __name__ == "__main__":
    unordened_list = [8, 12, 1, 3, 5]
print(f'lista desordenada:{unordened_list}')
print(f'lista ordenada:{merge_sort(unordened_list)}')
