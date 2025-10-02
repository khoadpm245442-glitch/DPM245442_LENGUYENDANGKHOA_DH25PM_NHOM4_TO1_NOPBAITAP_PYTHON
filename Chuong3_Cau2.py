#Trả lời câu 2 chương 3
print("Chuong trinh tinh so ngay trong thang")
thang=int(input("Nhap thang can kiem tra: "))
if thang in (1,3,5,7,8,10,12):
    print("Thang", thang, "co 31 ngay")
elif thang in (4,6,9,11):
    print("Thang", thang, "co 30 ngay")
elif thang==2:
    year = int(input("Nhap nam can kiem tra: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Thang", thang, "co 29 ngay")
    else:
        print("Thang", thang, "co 28 ngay")
else:
    print("Thang", thang, "khong hop le")
    