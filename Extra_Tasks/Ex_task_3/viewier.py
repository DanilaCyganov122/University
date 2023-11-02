import dcalc
def create_list(*a, **b):
    convert = dict()
    for i in range(0, len(a)):
        convert["Point_"+str(i)] = a[i]
    convert.update(b)
    lst = []
    for i,j in convert.items():
        lst.append(f"{i} = {dcalc.deg_to_gms(j)}")
    return lst
print(create_list(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))





