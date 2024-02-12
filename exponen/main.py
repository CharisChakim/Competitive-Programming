#Fungsi exponen
def pangkat(base, pangkat):
    # your code here
    result = 1
    for i in range (pangkat):
        result *= base
    return result
        


if __name__ == '__main__':
    print(pangkat(2, 3)) # 8
    print(pangkat(5, 3)) # 125
    print(pangkat(10, 2)) # 100
    print(pangkat(2, 5)) # 32
    print(pangkat(7, 3)) # 343
    
#LITE VERSION    
#ver basic
# def pangkat(base, pangkat):
#     base**pangkat

# other version
# def pangkat(base, pangkat):  
#     pow(base,pangkat)