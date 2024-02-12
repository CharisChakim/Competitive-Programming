# input
student_score = 80

# Process: Your Solution Code Here
#Fungsi Konversi angka menjadi nilai berupa string
def convert(student_score):
    if 80 <= student_score <= 100:
        return "A"
    elif 65<= student_score <= 79:
        return "B+"
    elif 50 <= student_score <= 64:
        return "B" 
    elif 35 <= student_score <= 49:
        return "C"
    else:
        return "D" 

# Output "Nilai A"
konversi =convert(student_score)
print("Nilai", konversi)