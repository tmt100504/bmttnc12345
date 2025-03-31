def xoa_ptu(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

#Su dung ham va in kq
my_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
key_to_delete = 'b'
result = xoa_ptu(my_dict, key_to_delete)
if result:
    print('Phan tu da duoc xoa tu Dictionary: ',my_dict)
else:
    print('Khong tim thay ptu can xoa trong Dictionary.')