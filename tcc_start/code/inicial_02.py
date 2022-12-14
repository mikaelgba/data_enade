import pandas as pd
import inicial as base

# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2017_si.csv')
filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2021_si.csv')

# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2017_si_brasil.csv')
# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2021_si_brasil.csv')

# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2017_si_public.csv')
# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2021_si_public.csv')

# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2017_si_federal.csv')
# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2021_si_federal.csv')

# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2017_si_NE.csv')
# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2021_si_NE.csv')

# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2017_si_PB.csv')
# filtered_df_three_no_null = base.get_filtered_df_three_no_null('../datas/microdatas/microdados2021_si_PB.csv')

# result_final = 'result_si_2017.csv'
result_final = 'result_si_2021.csv'

# result_final = 'result_si_2017_brasil.csv'
# result_final = 'result_si_2021_brasil.csv'

# result_final = 'result_si_2017_public.csv'
# result_final = 'result_si_2021_public.csv'

# result_final = 'result_si_2017_federal.csv'
# result_final = 'result_si_2021_federal.csv'

# result_final = 'result_si_2017_NE.csv'
# result_final = 'result_si_2021_NE.csv'

# result_final = 'result_si_2017_PB.csv'
# result_final = 'result_si_2021_PB.csv'

# 2017
'''list_answer_gab = ["C","C","B","B","C","E","A","D",
                   "X","X","A","C","E","Z","A","D",
                   "B","B","B","E","B","D","D","B",
                   "X","E","A","E","X","C","B","D",
                   "C","C","C"]'''
# 2021
list_answer_gab = ["E","C","B","B","A","A","C","D","X","E",
                   "C","B","D","C","D","A","X","X","A","B",
                   "X","E","B","B","E","E","X","A","D","E",
                   "A","C","Z","D","D",]

list_g_q = ["Geral" for i in range(8)]
list_o_q = ["Espec??fico" for j in range(27)]
[list_g_q.append(i) for i in list_o_q]


def replace_string_answer(df_replace):
    list_out = []
    for line in df_replace:
        list_i = []
        [list_i.append(i) for i in line.replace('"', '')]
        list_out.append(list_i)
    return list_out


def cont_answers_by_number(list):
    dataframe = pd.DataFrame(list)
    dataframe1 = dataframe.transpose()
    list_out = []
    for i in [i for i in range(len(dataframe1))]:
        res = sum([eval(i) for i in dataframe[i].to_list()])
        list_out.append(res)
    return list_out


replace_by_filter_ACE_OFG = replace_string_answer(filtered_df_three_no_null['DS_VT_ACE_OFG'])
replace_by_filter_ACE_OCE = replace_string_answer(filtered_df_three_no_null['DS_VT_ACE_OCE'])

g_filter = cont_answers_by_number(replace_by_filter_ACE_OFG)
o_filter = cont_answers_by_number(replace_by_filter_ACE_OCE)

all_filter = g_filter
[all_filter.append(i) for i in o_filter]
all_p_filter = [i / len(filtered_df_three_no_null) for i in all_filter]
'''print(all_filter)
print(g_filter)
print(all_filter)
print([f'{i:,.2f}' for i in all_p_filter])'''

list_question_by_p = []
[list_question_by_p.append([list_answer_gab.__getitem__(i), all_p_filter[i]]) for i in range(all_filter.__len__())]

df = pd.DataFrame(list_question_by_p)
df.columns = ['Respostas certas','Porcetagem']
df['Numeros de acertos'] = all_filter

number_questions = []
[number_questions.append("Quest??o " + str(i + 1)) for i in range(35)]
df['Quest??es'] = number_questions
df['Componente'] = list_g_q
df_rename = pd.DataFrame(df)
df_rename = df_rename[['Quest??es','Respostas certas','Numeros de acertos','Porcetagem','Componente']]
df_rename.loc[df_rename['Numeros de acertos'] > len(filtered_df_three_no_null), 'Numeros de acertos'] = None
df_rename.loc[df_rename['Porcetagem'] >= 1, 'Porcetagem'] = None

'''print(len(filtered_df_three_no_null))'''
print(df_rename['Porcetagem'].mean())
print(df_rename)

df_rename.to_csv(f"../datas/results/{result_final}")


