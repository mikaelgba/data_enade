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

all_by_comp_2017 = all_2017_join[['competencia', 'numero_questao']].groupby('competencia')['numero_questao'].count().sort_values()
all_by_comp_2021 = all_2021_join[['competencia', 'numero_questao']].groupby('competencia')['numero_questao'].count().sort_values()
all_by_comp = all_2017_2021_join[['competencia', 'numero_questao']].groupby('competencia')['numero_questao'].count().sort_values()

print("2017 \n", all_by_comp_2017)
print("2021 \n", all_by_comp_2021)
print("2017 e 2021 \n", all_by_comp)

all_by_2017 = all_2017_join[['numero_questao', 'Numeros de acertos', 'Porcetagem', 'competencia']].groupby('competencia')['Porcetagem'].sum()
all_by_2021 = all_2021_join[['numero_questao', 'Numeros de acertos', 'Porcetagem', 'competencia']].groupby('competencia')['Porcetagem'].sum()
all_by_2017_2021 = all_2017_2021_join[['numero_questao', 'Numeros de acertos', 'Porcetagem', 'competencia']].groupby('competencia')['Porcetagem'].sum()

print("2017 \n", all_by_2017)
print("2021 \n", all_by_2021)
print("2017 e 2021 \n", all_by_2017_2021)

porc_by_comp = join_data(all_by_comp, all_by_2017_2021)
porc_by_comp = porc_by_comp.eval('media_competencia = (Porcetagem / numero_questao) * 100')
print(porc_by_comp)


