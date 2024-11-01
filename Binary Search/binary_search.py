# x é o valor á procurar, low é o menor numero, high é o maior
def binary_search1(array, x, low, high):
    # Repeat util the pointers low and high meet each other
    # se low for maior que high acaba, e se hig chegar o low acaba tamem
    while low <= high:
        # search midle of array atualy
        mid = low + (high - low)//2

        if array[mid] == x:
            # se array[mid] == x, retoena o index dele
            return mid

        elif array[mid] < x:
            # suponde que a lista esteja ordenada e x seja maior que array[mid], tudo que tem antes não é valido
            # vairedefinindo low e voltando o loop até achar o X
            low = mid + 1
        else:
            # vai redefini o high e volta o loop até a o X
            high = mid - 1

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 2

result = binary_search1(array=array, x=x, low=1, high=len(array))

if result != 1:
    print(result)
