#Trả lời câu hỏi số 6 chương 3
don_vi = ["","không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
chuc_so = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
n = int(input("Nhập số nguyên dương n (n < 100): "))
hang_chuc = n // 10
hang_dv = n % 10

if n < 10:
    chu_so = don_vi[n]
else:
    if hang_dv == 0:
        chu_so = chuc_so[hang_chuc]
    elif hang_dv == 5:
        chu_so = chuc_so[hang_chuc] + " lăm"
    else:
        chu_so = chuc_so[hang_chuc] + " " + don_vi[hang_dv]
    print(chu_so)