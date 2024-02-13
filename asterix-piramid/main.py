# Fungsi Piramida asterix
def play_with_asterisk(n):
    pattern = ""
    for i in range(1, n+1):
        # Tambahkan leading spaces (spasi di depan)
        pattern += " " * (n - i)

        # Tambahkan bintang sesuai dengan nilai i
        pattern += "* " * i

        # Tambahkan newline untuk baris berikutnya
        pattern += "\n"

    return pattern

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """

#Versi 2
#Algoritma Looping Untuk Menggambarkan Piramida
# for i in range(n):
#     # Mencetak spasi untuk meratakan
#     for j in range(n - i - 1):
#         print(" ", end="")
    
#     # Mencetak bintang sesuai dengan nomor baris
#     for k in range( i + 1):
#         print("*", end=" ")
    
#     # Pindah ke baris berikutnya
#     print()
