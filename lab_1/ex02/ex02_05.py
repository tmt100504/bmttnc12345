sohlam = float(input('Nhap so gio lam moi tuan: '))

luong_gio = float(input('Nhap thu lao tren moi gio lam tieu chuan: '))

giotieuchuan = 44 #So gio lam tieu chuan moi tuan

giovuotchuan = max(0, sohlam - giotieuchuan) #So gio lam vuot chuan moi tuan

thuclinh = giotieuchuan * luong_gio + giovuotchuan * luong_gio * 1.5 #Tinh tong thu nhap

print(f'So tien thuc linh cua nhan vien: {thuclinh}')