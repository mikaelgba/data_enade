import csv
import pandas as pd

# read_file = pd.read_csv('microdados2017_arq3.txt')
# read_file.to_csv('New_microdados2017_arq3.csv', index=None)
# read_2017 = pd.read_csv('New_microdados2017_arq3.csv', header=None)
# print(read_2017.head())

tags = ['NU_ANO', 'CO_CURSO', 'NU_ITEM_OFG', 'NU_ITEM_OFG_Z', 'NU_ITEM_OFG_X', 'NU_ITEM_OFG_N',
        'NU_ITEM_OCE', 'NU_ITEM_OCE_Z', 'NU_ITEM_OCE_X', 'NU_ITEM_OCE_N', 'DS_VT_GAB_OFG_FIN', 'DS_VT_GAB_OCE_FIN',
        'DS_VT_ESC_OFG', 'DS_VT_ACE_OFG', 'DS_VT_ESC_OCE', 'DS_VT_ACE_OCE', 'TP_PRES', 'TP_PR_GER',
        'TP_PR_OB_FG', 'TP_PR_DI_FG', 'TP_PR_OB_CE', 'TP_PR_DI_CE', 'TP_SFG_D1', 'TP_SFG_D2',
        'TP_SCE_D1', 'TP_SCE_D2', 'TP_SCE_D3', 'NT_GER', 'NT_FG', 'NT_OBJ_FG',
        'NT_DIS_FG', 'NT_FG_D1', 'NT_FG_D1_PT', 'NT_FG_D1_CT', 'NT_FG_D2', 'NT_FG_D2_PT',
        'NT_FG_D2_CT', 'NT_CE', 'NT_OBJ_CE', 'NT_DIS_CE', 'NT_CE_D1', 'NT_CE_D2',
        'NT_CE_D3', 'CO_RS_I1', 'CO_RS_I2', 'CO_RS_I3', 'CO_RS_I4', 'CO_RS_I5',
        'CO_RS_I6', 'CO_RS_I7', 'CO_RS_I8', 'CO_RS_I9']

# print(len(tags))

with open('New_microdados2017_arq3.csv', encoding='utf-8') as arquivo_referencia:

  table = csv.reader(arquivo_referencia, delimiter=';')
  table_two = []

  for l in table:
      table_two.append(l[0].__str__().split(";"))

  df = pd.DataFrame.from_records(table_two, columns=tags)

  filtered_df = df[df['CO_CURSO'] == '107360']

  print(filtered_df)
  filtered_df.to_csv("microdados2017_si.csv")






