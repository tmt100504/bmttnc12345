def tao_tuple_tu_list(lst):
    return tuple(lst)

#Nhap ds tu nguoi dung va xu ly chuoi
input_list = input('Nhap ds cac so, cach nhau bang dau phay: ')
numbers = list(map(int,input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print('List: ', numbers)
print('Tuple tu List: ', my_tuple)
