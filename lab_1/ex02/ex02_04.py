#Tao mot danh sach rong de luu kq
j=[]

#Duyet qua tat ca cac so trong doan tu 2000 den 3000, ktra xem so i co chia het cho 7 va khong phai la boi so cua 5 khong
for i in range(2000,3201):
    if (i%7 == 0) and (i %5 !=0):
        j.append(str(i))
print(','.join(j))
