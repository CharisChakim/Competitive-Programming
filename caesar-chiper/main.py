#Fungsi Caesar chiper/geser angka/enkripsi
def caesar(offset, input_str):
    result =  ''
    for char in input_str:
        if char.islower():
            new_char = chr(((ord(char) - 97 + offset) % 26) + 97)
            result += new_char
        else:
            result += char
    return result

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl