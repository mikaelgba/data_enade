import pandas as pd

def split_comp(csv_input, type, type_output):
    df = pd.read_csv(csv_input)
    list_comp, list_comp_final = [], []
    [list_comp.append(str(i[0]).split(";")) for i in df[[type]].values]
    if type_output == 0:
        return list_comp
    else:
        for i in list_comp:
            if len(i) > 1:
                [list_comp_final.append(int(comp)) for comp in i]
            else:
                list_comp_final.append(int(i[0]))
    return list_comp_final

def group_comp(list_input):
    list_out = []
    for i in range(1,23):
        list_i = i
        cont = 0
        for j in list_input:
            if j == i: cont += 1
        list_out.append([list_i, cont])
    return list_out

def convert_dataframe(list, str1, str2, type_out):
    if type_out == 0: return pd.DataFrame(list, columns=[str1, str2])
    return pd.DataFrame(group_comp(list), columns=[str1, str2])

csv_2017 = "../datas/join_2017.csv"
csv_2021 = "../datas/join_2021.csv"

'''list_obj_conh_final_2017 = split_comp(csv_2017, "objeto_de_conhecimento_numero",1)
list_obj_conh_final_2021 = split_comp(csv_2021, "objeto_de_conhecimento_numero",1)
list_obj_conh_final_2017_2021 = list_obj_conh_final_2017 + list_obj_conh_final_2021

print(list_obj_conh_final_2017)
print(list_obj_conh_final_2021)
print(list_obj_conh_final_2017_2021)

print(group_comp(list_obj_conh_final_2017))
print(group_comp(list_obj_conh_final_2021))
print(group_comp(list_obj_conh_final_2017_2021))

df_2017 = convert_dataframe(list_obj_conh_final_2017,'number_comp', 'quant_by_comp', 1)
df_2021 = convert_dataframe(list_obj_conh_final_2021,'number_comp', 'quant_by_comp', 1)
df_2017_2021 = convert_dataframe(list_obj_conh_final_2017_2021,'number_comp', 'quant_by_comp', 1)

print(df_2017.sort_values(['quant_by_comp']))
print(df_2021.sort_values(['quant_by_comp']))
print(df_2017_2021.sort_values(['quant_by_comp']))'''
