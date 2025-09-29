def check (i):
    if (len(i) != 1): return False
    if (("a" <= i <= "z") or ("A" <= i <= "Z")):
        return True
    return False

def ans (i):
    k = ord(i)
    if ((k >= 65) and (k <= 90)): return chr(k + 32)
    else: return chr(k - 32)


i = input("Nhập kí tự: ")

while (check(i) == False):
    i = input("Vui long nhap lai: ")
    
print(ans(i))


