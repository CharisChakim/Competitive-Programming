#Fungsi Mencari irisan
def compare(a, b):
    len1 = len(a)
    len2 = len(b)
    txt1 = a
    txt2 = b
    if len1 >= len2:
        st_idx = txt1.index(txt2)
        en_idx = st_idx + len2
        return txt2[st_idx:en_idx]
    elif len1 < len2:
        st_idx = txt2.index(txt1)
        en_idx = st_idx + len1
        return txt1[st_idx:en_idx]

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA
    
#lite version based on testcase
# if len1 > len2:
#         return b
#     else:
#         return a