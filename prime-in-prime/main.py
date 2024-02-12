#Fungsi Menentukan Bilangan Prima
def prime_number(num):
    if num == 1:
        return False
    elif num > 1 :
        for i in range(2,num):
            if (num % i) == 0 :
                return False
        else :
            return True
    else :
        return False
#Fungsi untuk menentukan apakah tiap digitnya juga Prima
def full_prima(num):
    return prime_number(num) and all(prime_number(int(num)) for num in str(num)) 

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True