def check (i):
    if (len(i) != 1): return False
    if (("a" <= i <= "z") or ("A" <= i <= "Z")):
        return True
    return False

def ans (i):
    k = ord(i)
    if ((k >= 65) and (k < 90)): return chr(k + 33)
    elif ((k >= 97) and (k < 122)): return chr(k - 31)
    elif (k == 90): return chr(97)
    return chr(97)

i = input("Nhập kí tự: ")

while (check(i) == False):
    i = input("Vui long nhap lai: ")
    
print(ans(i))

