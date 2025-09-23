import math

a, b, c = map(float, input("Nhập 3 cạnh tam giac:").split())

if ((a+b > c) and (b+c > a) and (c+a > b)):
    print("Đây là 3 cạnh tam giác")
    p = (a + b + c) / 2
    print("Chu vi là:", 2 * p)
    s = p * (p-a) * (p-b) * (p-c)
    print("Diện tích là:", math.sqrt(s))
else:
    print("Không phải 3 cạnh tam giác")

