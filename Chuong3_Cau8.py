#Trả lời câu hỏi số 8 chương 3
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
pt=["+","-","*","/"]
pt=(input("Nhap phep tinh: "))
if pt == "+":
    print(a,"+",b)
elif pt == "-":
    print(a,"-",b)
elif pt == "*":
    print(a,"*",b)
elif pt == "/":
    if b!=0:
        print(a,"/",b)
    else:
        print("Khong the chia cho 0")
else:
    print("Phep tinh khong hop le!")
    