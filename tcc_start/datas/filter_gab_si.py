import csv
import pandas as pd

# data_entr = 'txt/microdados2017_arq3.txt'
data_entr = 'txt/microdados2021_arq3.txt'

# new_date_entr = 'new/New_microdados2017_arq3.csv'
new_date_entr = 'new/New_microdados2021_arq3.csv'

# new_date_entr = 'new/New_microdados2017_arq3_brasil.csv'
# new_date_entr = 'new/New_microdados2021_arq3_brasil.csv'

# date_out = 'microdatas/microdados2017_si.csv'
# date_out = 'microdatas/microdados2021_si.csv'

# date_out = 'microdatas/microdados2017_si_brasil.csv'
# date_out = 'microdatas/microdados2021_si_brasil.csv'

# date_out = 'microdatas/microdados2017_si_public.csv'
# date_out = 'microdatas/microdados2021_si_public.csv'

# date_out = 'microdatas/microdados2017_si_federal.csv'
# date_out = 'microdatas/microdados2021_si_federal.csv'

# date_out = 'microdatas/microdados2017_si_NE.csv'
# date_out = 'microdatas/microdados2021_si_NE.csv'

# date_out = 'microdatas/microdados2017_si_PB.csv'
date_out = 'microdatas/microdados2021_si_PB.csv'

# filter_year_csv = 'filters/filter2017.csv'
# filter_year_csv = 'filters/filter2021.csv'

# filter_year_csv = 'filters/filter2017_public.csv'
# filter_year_csv = 'filters/filter2021_public.csv'

# filter_year_csv = 'filters/filter2017_federal.csv'
# filter_year_csv = 'filters/filter2021_federal.csv'

# filter_year_csv = 'filters/filter2017_NE.csv'
# filter_year_csv = 'filters/filter2021_NE.csv'

# filter_year_csv = 'filters/filter2017_PB.csv'
filter_year_csv = 'filters/filter2021_PB.csv'

co_curso_rio_tinto = '107360'
id_curso = 'rio tinto'

read_file = pd.read_csv(data_entr)
read_file.to_csv(new_date_entr, index=None)
read_2017 = pd.read_csv(new_date_entr, header=None)
print(read_2017.head())

tags = ['NU_ANO', 'CO_CURSO', 'NU_ITEM_OFG', 'NU_ITEM_OFG_Z', 'NU_ITEM_OFG_X', 'NU_ITEM_OFG_N',
        'NU_ITEM_OCE', 'NU_ITEM_OCE_Z', 'NU_ITEM_OCE_X', 'NU_ITEM_OCE_N', 'DS_VT_GAB_OFG_FIN', 'DS_VT_GAB_OCE_FIN',
        'DS_VT_ESC_OFG', 'DS_VT_ACE_OFG', 'DS_VT_ESC_OCE', 'DS_VT_ACE_OCE', 'TP_PRES', 'TP_PR_GER',
        'TP_PR_OB_FG', 'TP_PR_DI_FG', 'TP_PR_OB_CE', 'TP_PR_DI_CE', 'TP_SFG_D1', 'TP_SFG_D2',
        'TP_SCE_D1', 'TP_SCE_D2', 'TP_SCE_D3', 'NT_GER', 'NT_FG', 'NT_OBJ_FG',
        'NT_DIS_FG', 'NT_FG_D1', 'NT_FG_D1_PT', 'NT_FG_D1_CT', 'NT_FG_D2', 'NT_FG_D2_PT',
        'NT_FG_D2_CT', 'NT_CE', 'NT_OBJ_CE', 'NT_DIS_CE', 'NT_CE_D1', 'NT_CE_D2',
        'NT_CE_D3', 'CO_RS_I1', 'CO_RS_I2', 'CO_RS_I3', 'CO_RS_I4', 'CO_RS_I5',
        'CO_RS_I6', 'CO_RS_I7', 'CO_RS_I8', 'CO_RS_I9']
tags2 = ["NU_ANO","CO_CURSO","CO_IES","CO_CATEGAD","CO_ORGACAD","CO_GRUPO","CO_MODALIDADE","CO_MUNIC_CURSO","CO_UF_CURSO","CO_REGIAO_CURSO"]

print(len(tags))


def date_out_csv(area):
    with open(new_date_entr, encoding='utf-8') as arquivo_referencia:

        table = csv.reader(arquivo_referencia, delimiter=';')
        table_two = []

        for l in table:
            table_two.append(l[0].__str__().split(";"))

        df = pd.DataFrame.from_records(table_two, columns=tags)

        if area == id_curso:
            filtered_df = df[df['CO_CURSO'] == co_curso_rio_tinto]

        else:
            # ---------------------------------------------
            df2 = pd.read_csv(filter_year_csv, header=None)
            print(df2)
            list_of_single_column = df2[2].to_list()
            print(list_of_single_column)
            filtered_df = df[df['CO_CURSO'].isin(list_of_single_column)]
            # ----------------------------------------------

        print(filtered_df)
        filtered_df.to_csv(date_out)


date_out_csv('')
