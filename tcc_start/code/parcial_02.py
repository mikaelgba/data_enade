import pandas as pd
import parcial_01

def div_ocn(list_input):
    list_ocn = []
    for line in list_input:
        if len(line) == 2:
            list_ocn.append([line[0], line[1]])
        else:
            list_ocn.append([line[0], 0])
    return list_ocn

def join_data(file_one, file_two):
    return pd.concat([file_one, file_two], axis=1, join='inner')

def gen_group_comp(dataframe):
    grouped_df = dataframe.groupby(["competencia"]).sum()
    df = dataframe.groupby('competencia')['Numeros de acertos'].apply(list)
    df_c = dataframe.groupby('competencia')['Porcetagem'].apply(list)
    return grouped_df, df, df_c

def count_list(list, number):
    list_out =[]
    size = len(list)
    count = 0
    for i in list:
        count += i
    med = count / size
    list_out.append([number, size, count, med])
    return [number, size, count, med]
def list_calc(list_one, list_two, list_number):
    list_out = []
    list_out_alt = []
    number = 0
    for i in list_one:
        list_out.append(count_list(i, list_number[number]))
        number += 1
    number = 0
    for j in list_two:
        list_out_alt.append(count_list(j, list_number[number]))
        number += 1
    return list_out, list_out_alt

csv_2017 = "../datas/join_2017.csv"
csv_2021 = "../datas/join_2021.csv"

list_obj_conh_final_2017 = parcial_01.split_comp(csv_2017, "objeto_de_conhecimento_numero", 0)
list_obj_conh_final_2021 = parcial_01.split_comp(csv_2021, "objeto_de_conhecimento_numero", 0)
# list_obj_conh_final_2017_2021 = list_obj_conh_final_2017 + list_obj_conh_final_2021

ocn_2017 = parcial_01.convert_dataframe(div_ocn(list_obj_conh_final_2017), 'ocn_1', "ocn_2", 0)
ocn_2021 = parcial_01.convert_dataframe(div_ocn(list_obj_conh_final_2021), 'ocn_1', "ocn_2", 0)
# ocn_2017_2021 = parcial_01.convert_dataframe(div_ocn(list_obj_conh_final_2017_2021), 'ocn_1', "ocn_2", 0)

all_2017 = pd.DataFrame(pd.read_csv(csv_2017))
all_2021 = pd.DataFrame(pd.read_csv(csv_2021))

all_2017_join = join_data(all_2017, ocn_2017)
all_2021_join = join_data(all_2021, ocn_2021)
all_2017_2021_join = pd.concat([all_2017_join, all_2021_join])

all_by_2017 = all_2017_join[['numero_questao', 'Numeros de acertos', 'Porcetagem', 'competencia']]
all_by_2021 = all_2021_join[['numero_questao', 'Numeros de acertos', 'Porcetagem', 'competencia']]
all_by_2017_2021 = all_2017_2021_join[['numero_questao', 'Numeros de acertos', 'Porcetagem', 'competencia']]
base_all_comp = all_by_2017_2021[['numero_questao', 'Porcetagem', 'competencia']]

grouped_df = base_all_comp.groupby(["competencia"]).count()
print(grouped_df.sort_values(["numero_questao"]))

all_by_2017 = all_by_2017.dropna(subset=["Porcetagem"])
all_by_2021 = all_by_2021.dropna(subset=["Porcetagem"])
all_by_2017_2021 = all_by_2017_2021.dropna(subset=["Porcetagem"])

'''print("2017 \n", all_by_2017)
print("2021 \n", all_by_2021)
print("2017 e 2021 \n", all_by_2017_2021)'''

grouped_df, df, df_c = gen_group_comp(all_by_2017)
grouped_df_2021, df_2021, df_c_2021 = gen_group_comp(all_by_2021)
grouped_df_2017_2021, df_2017_2021, df_c_2017_2021 = gen_group_comp(all_by_2017_2021)

list_number_2017 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
list_number_2021 = [1,2,3,4,5,7,8,9,10,11,12,14]
list_number_2017_2021 = [i + 1 for i in range(15)]

a, a2 = list_calc(df, df_c, list_number_2017)
b, b2 = list_calc(df_2021, df_c_2021, list_number_2021)
c, c2 = list_calc(df_2017_2021, df_c_2017_2021, list_number_2017_2021)

by_comp_2017 = pd.DataFrame(a, columns=["competencia", "Quantidade", "soma_acertos", "media_acertos_competencia"])
by_comp_2021 = pd.DataFrame(b, columns=["competencia", "Quantidade", "soma_acertos", "media_acertos_competencia"])

media_comp_2017 = pd.DataFrame(a2, columns=["competencia", "Quantidade", "soma_media", "media_por_competencia"])
media_comp_2021 = pd.DataFrame(b2, columns=["competencia", "Quantidade", "soma_media", "media_por_competencia"])
media_comp_2017_2021 = pd.DataFrame(c2, columns=["competencia", "Quantidade", "soma_media", "media_por_competencia"])

print(by_comp_2017.sort_values(['Quantidade']))
print(by_comp_2021.sort_values(['Quantidade']))

print(media_comp_2017.sort_values(['media_por_competencia']))
print(media_comp_2021.sort_values(['media_por_competencia']))
print(media_comp_2017_2021.sort_values(['Quantidade']))
