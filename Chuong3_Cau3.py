#Trả lời câu hỏi số 3 chương 3
from math import sqrt
print("Chuong trinh giai phuong trinh bac 2")
a=float(input("Nhap he so a: "))
b=float(input("Nhap he so b: "))
c=float(input("Nhap he so c: "))
if a==0:
    if b==0 and c==0:
        print("Phuong trinh vo so nghiem")
    elif b==0 and c!=0:
        print("Phuong trinh vo nghiem")
    else:
        x=-c/b
        print("Khong nghiem X= ", x)
else:
    delta= b**2 - 4*a*c
    if delta<0:
        print("Phuong trinh vo nghiem")
    elif delta==0:
        x=-b/(2*a)
        print("Phuong trinh co nghiem kep X1=X2= ", x)
    else:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem phan biet X1= ", x1, "va X2= ", x2)
        
        