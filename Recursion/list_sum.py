def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0] 
    else:
        return list_sum(num_list[:len(num_list)//2]) + list_sum(num_list[len(num_list)//2:])

print(list_sum([1, 3, 5, 7, 9]))