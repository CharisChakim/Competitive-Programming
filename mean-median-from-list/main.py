#Fungsi mencari mean dan median dari list array
def mean_median(array_input):
#Initial variable
    mean = None
    median = None
    total = sum(array_input) #total nilai dalam array
    length = len(array_input)#panjang array
#Command jika array kosong   
    if not array_input:
        return None
#Membuat rumus untuk mean dan median 
    if length % 2 == 0:
        median = (array_input[length // 2 - 1] + array_input[length// 2])/2
        mean = total / length
        return mean,median
    else:
        median = array_input[len(array_input)//2]
        mean = total / length
        return mean,median


if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)
    print(mean_median([]))