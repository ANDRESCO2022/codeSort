
def shell_sort(list_to_order):
    # calcula  la  cantidad  de  elementos  de lista
    length = len(list_to_order)
    # referencia  de   intervalo => resultado de  cantidad  de  elementos  entre  2 dividion  entera
    reference = length//2
    print(f'referencia de  invalo:{reference}')
    while reference > 0:
        # iteracion  en razon de   el intervalo de  referencia  y la cantidad  de  elementos  en lista
        for i in range(reference, length):
            insert = list_to_order[i]
            index = i
            print(
                f'bloque a comparar: { insert} menor que  {list_to_order[index-reference] }  ')
            # bucle  en razon al indice  donde  se  compara  el valor del indice  en   la  lista y se inserta  el mismo
            while index >= reference and insert < list_to_order[index-reference]:
                list_to_order[index] = list_to_order[index-reference]
                index -= reference
            # insersion de  index  en el intervalo comparado
            list_to_order[index] = insert
            print(list_to_order)
        reference //= 2  # actualizacion  y division de  referencia de  intervalo
    return list_to_order


if __name__ == "__main__":
    unordened_list = [8, 12, 1, 3, 5]
print(f'lista desordenada:{unordened_list}')
print(f'lista ordenada:{shell_sort(unordened_list)}')
