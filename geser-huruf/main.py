#Membuat fungsi geser huruf
def ubah_huruf(sentence):
    pattern = "" 
    offset = 10 #nilai geser huruf
#Membuat Looping untuk mengecek tiap huruf
    for huruf in sentence:
        if huruf.isalpha(): #mengecek apakah huruf2 tersebut masuk ke alphabet
            huruf = huruf.upper()
#Membuat algoritma pergeseran
            kode_huruf = ord(huruf) - 65
            kode_huruf = (kode_huruf + offset) % 26
            huruf = chr(kode_huruf + 65)
        pattern += huruf
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB