#Fungsi Menghilangkan duplikat output len after duplikat
def remove_duplicates(array):
    if not array:
        return 0
    else:
        remove = set(array)
        makelist = list(remove)
        result = len(makelist)
    return result

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4