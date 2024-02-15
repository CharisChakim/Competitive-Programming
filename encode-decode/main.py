def encode_decode(word):
    #your code here
    shift = 2 if word.startswith('<encode>') else -2 
    result = ''

    for char in word[8:]:
        if char.islower():  # Hanya melakukan enkripsi/dekripsi pada huruf kecil
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)  # Menambah/dikurangi dua huruf sesuai pergeseran
            result += new_char
        # else:
        #     result += char  # Jika bukan huruf kecil, biarkan karakter aslinya
            
    return result
    
    # pass

#encode
print(encode_decode('<encode>abcd')) #cdef
print(encode_decode('<encode>xyz'))  #zab

#decode
print(encode_decode('<decode>cdef')) #abcd
print(encode_decode('<decode>zab'))  #xyz