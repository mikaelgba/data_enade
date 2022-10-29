import csv
import pandas as pd

# read_file = 'microdados2017_arq1.txt'
read_file = 'microdados2021_arq1.txt'

# read_file_03 = 'New_microdados2017_arq3.csv'
read_file_03 = 'New_microdados2021_arq3.csv'

# read_file_01 = 'New_microdados2017_arq1.csv'
read_file_01 = 'New_microdados2021_arq1.csv'

# filter_year_csv = 'filter2017.csv'
filter_year_csv = 'filter2021.csv'

tags = ["NU_ANO","CO_CURSO","CO_IES","CO_CATEGAD","CO_ORGACAD","CO_GRUPO","CO_MODALIDADE","CO_MUNIC_CURSO","CO_UF_CURSO","CO_REGIAO_CURSO"]

def filter(ent_01, ent_02):
    read_file = pd.read_csv(ent_01)
    read_file.to_csv(ent_02, index=None)
    read_year = pd.read_csv(ent_02, header=None)
    print(read_year.head())

def csv_filter(entr):
    with open(entr, encoding='utf-8') as arquivo_referencia:
        table = csv.reader(arquivo_referencia, delimiter=';')
        table_two = []

        for l in table:
            print(l)
            table_two.append(l)
            # table_two.append(l[0].__str__().split(";"))

        df = pd.DataFrame.from_records(table_two, columns=tags)
        filtered_df = df[df['CO_GRUPO'] == '4006']
        filtered_df.to_csv(filter_year_csv)
        print(filtered_df)


'''def filter_brasil(entr, df_g):
    with open(entr, encoding='utf-8') as arquivo_referencia:
        table = csv.reader(arquivo_referencia, delimiter=';')
        table_two = []

        for l in table:
            table_two.append(l[0].__str__().split(";"))

        print(table_two)
        df = pd.DataFrame.from_records(table_two, columns=tags)

       filtered_df = df[df['CO_CURSO'] == df_g[df_g['CO_CURSO']]]

        print(filtered_df)

        #filtered_df.to_csv("microdados2021_si.csv")'''

filter(read_file, read_file_01)
filter_year = csv_filter(read_file_01)
#brasil = filter_brasil(read_file_03, filter_year)

