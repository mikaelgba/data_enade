import pandas as pd
import matplotlib.pyplot as plt

def get_filtered_df_three_no_null(file: str):
    df = pd.read_csv(file)
    filtered_df = df[['NU_ITEM_OFG', 'NU_ITEM_OFG_Z', 'NU_ITEM_OFG_X', 'NU_ITEM_OFG_N']]
    filtered_df_two = df[['NU_ITEM_OCE', 'NU_ITEM_OCE_Z', 'NU_ITEM_OCE_X', 'NU_ITEM_OCE_N']]
    filtered_df_three = df[['DS_VT_ACE_OFG', 'DS_VT_ACE_OCE']]
    # filtered_df_three_no_null = filtered_df_three.dropna(thresh=2)
    return filtered_df_three.dropna(thresh=2)
    pass

#filtered_df_three_no_null = get_filtered_df_three_no_null('../datas/microdados2017_si.csv')
fil = pd.read_csv('../datas/microdados2017_si_brasil.csv')
filtered_df_three_no_null = get_filtered_df_three_no_null('../datas/microdados2017_si_brasil.csv')
list_right_ACE_OFG = []
list_all_ACE_OFG = []
list_right_ACE_OCE = []
list_all_ACE_OCE = []


def search_answer(list_input):
    value = 0
    total_answers = len(list_input)
    for line in list_input.replace('"', ''):
        if line == "1":
            value += 1
    return value, total_answers


for i in filtered_df_three_no_null.values:
    DS_VT_ACE_OFG, DS_VT_ACE_OFG_len = search_answer(i[0])
    DS_VT_ACE_OCE, DS_VT_ACE_OCE_len = search_answer(i[1])

    list_right_ACE_OFG.append(DS_VT_ACE_OFG)
    list_all_ACE_OFG.append(DS_VT_ACE_OFG_len - 2) # -2 para remover os caracteres de aspas
    list_right_ACE_OCE.append(DS_VT_ACE_OCE)
    list_all_ACE_OCE.append(DS_VT_ACE_OCE_len - 2) # -7 (-8 quando for 2021) pelas aspas e tambem excluindo as 4 questoes que foram anuladas

filtered_df_all = filtered_df_three_no_null.assign(right_ace_ofg = list_right_ACE_OFG,
                                      all_ace_ofg = list_all_ACE_OFG,
                                      right_ace_oce = list_right_ACE_OCE,
                                      all_ace_oce = list_all_ACE_OCE)

filtered_df_all['percent_ace_ofc'] = (filtered_df_all['right_ace_ofg'] / filtered_df_all['all_ace_ofg']) * 100
filtered_df_all['percent_ace_oce'] = (filtered_df_all['right_ace_oce'] / filtered_df_all['all_ace_oce']) * 100
filtered_df_all['total_all_ace'] = (filtered_df_all['all_ace_ofg'] + filtered_df_all['all_ace_oce'])
filtered_df_all['total_right_ace'] = (filtered_df_all['right_ace_ofg'] + filtered_df_all['right_ace_oce'])
filtered_df_all['percent_ace_final'] = (filtered_df_all['total_right_ace'] / filtered_df_all['total_all_ace']) * 100
filtered_df_all_ord = filtered_df_all.sort_values(['percent_ace_final'])
total_answer_right = filtered_df_all_ord[['total_right_ace']].mean()
total_answer = filtered_df_all_ord[['total_all_ace']].mean()

'''print("Respostas certas ofg, Percentual de certas ofc, Respostas certas oce e Percentual de certas oce \n",
      filtered_df_all_ord[['right_ace_ofg', 'percent_ace_ofc', 'right_ace_oce', 'percent_ace_oce']], "\n"
      "------------------------------------------------------------")

print("Total de respostas, Total certas, Respostas certas oce e Percentual total de certas \n",
      filtered_df_all_ord[['total_all_ace', 'total_right_ace', 'percent_ace_final']], "\n"
      "------------------------------------------------------------")

print("GroupBy por certas ofg \n", filtered_df_all_ord.groupby(['right_ace_ofg']).count(), "\n"
      "------------------------------------------------------------")

print("Percentual de certas ofg \n", filtered_df_all_ord.groupby(['percent_ace_ofc']).count(), "\n"
      "------------------------------------------------------------")

print("GroupBy por certas oce \n", filtered_df_all_ord.groupby(['right_ace_oce']).count(), "\n"
      "------------------------------------------------------------")

print("Percentual de certas oce \n", filtered_df_all_ord.groupby(['percent_ace_oce']).count(), "\n"
      "------------------------------------------------------------")

print("Media geral de acertos \n", total_answer_right, "\n"
      "------------------------------------------------------------")

print("Percetual geral de acertos \n", filtered_df_all_ord[['percent_ace_final']].sum() / 46, "\n"
      "------------------------------------------------------------")

print("Percetual geral de acertos \n", filtered_df_all_ord[['percent_ace_final']], "\n"
                                                                                              
      "------------------------------------------------------------")
print("Percetual geral de acertos \n", filtered_df_all_ord[['percent_ace_final']].mean(), "\n"
      "------------------------------------------------------------")

print("Percetual geral de acertos \n", filtered_df_all_ord[['total_right_ace']].std(), "\n"
      "------------------------------------------------------------")

print("Percetual geral de acertos \n", filtered_df_all_ord.mean(), "\n"
      "------------------------------------------------------------")

print("Percetual geral de acertos \n", filtered_df_all_ord.var(), "\n"
      "------------------------------------------------------------")


print(filtered_df_three_no_null, "OK")
print(fil, "OK 2")'''