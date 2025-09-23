a, b, c = map(float, input("Nhập 3 cạnh tam giac:").split())

if ((a+b > c) and (b+c > a) and (c+a > b)):
    print("Đây là 3 cạnh tam giác")
else:
    print("Không phải 3 cạnh tam giác")