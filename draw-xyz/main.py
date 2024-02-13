#Membuat fungsi
def draw_xyz(N):
#Membuat variable awal yang bernilai kosong dan empty string
    counter = 0
    pattern = ''
#Membuat looping agar membentuk patterm N x N
    for i in range (1,N+1):
#Menambah variable empty string untuk mencatat tiap pertambahan nilai dari looping        
        row = '' 
        for j in range (1,N+1):
            counter += 1 
#Membuat fungsi konversi            
            if counter % 3 == 0:
                row += 'X '
            elif counter % 2 == 1:
                row += 'Y '
            else:
                row += 'Z '
#Memasukkan nilai tiap row ke dalam pattern                  
        pattern += row + '\n'  
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """