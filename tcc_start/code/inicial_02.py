import pandas as pd
import inicial as base

filtered_df_three_no_null = base.get_filtered_df_three_no_null()
print(filtered_df_three_no_null['DS_VT_ACE_OFG'])


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
    for i in [i for i in range(0,len(dataframe1))]:
        res = sum([eval(i) for i in dataframe[i].to_list()])
        list_out.append(res)
    return list_out


replace_by_filter_ACE_OFG = replace_string_answer(filtered_df_three_no_null['DS_VT_ACE_OFG'])
replace_by_filter_ACE_OCE = replace_string_answer(filtered_df_three_no_null['DS_VT_ACE_OCE'])

print(cont_answers_by_number(replace_by_filter_ACE_OFG))
print(cont_answers_by_number(replace_by_filter_ACE_OCE))

