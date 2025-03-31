def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

#Nhap ds tu nguoi dung
input_string = input('Nhap ds cac tu, cach nhau bang dau cach ')
word_list = input_string.split()

#Su dung ham va in kq
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print('So lan xuat hien cua cac ptu: ', so_lan_xuat_hien)