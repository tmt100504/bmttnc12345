def truy_cap_ptu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element,last_element

#Nhap tuple tu nguoi dung
input_tuple = eval(input('Nhap tuple, vi du (1,2,3): '))
first,last = truy_cap_ptu(input_tuple)

#In kq
print('Phan tu dau tien: ', first)
print('Phan tu cuoi cung: ',last)
