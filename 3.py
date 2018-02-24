std_list = input('Student Code : ')
fac_list = []
for std in std_list:
    if(std%100 not in fac_list):
        fac_list.append(std%100)

print(len(fac_list))
