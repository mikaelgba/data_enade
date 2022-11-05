import csv
import pandas as pd

read_file = 'txt/microdados2017_arq1.txt'
# read_file = 'txt/microdados2021_arq1.txt'

read_file_01 = 'new/New_microdados2017_arq1.csv'
# read_file_01 = 'new/New_microdados2021_arq1.csv'

filter_year_csv = 'filters/filter2017.csv'
# filter_year_csv = 'filters/filter2021.csv'

# filter_year_csv = 'filters/filter2017_public.csv'
# filter_year_csv = 'filters/filter2021_public.csv'

# filter_year_csv = 'filters/filter2017_federal.csv'
# filter_year_csv = 'filters/filter2021_federal.csv'

# filter_year_csv = 'filters/filter2017_NE.csv'
# filter_year_csv = 'filters/filter2021_NE.csv'

# filter_year_csv = 'filters/filter2017_PB.csv'
# filter_year_csv = 'filters/filter2021_PB.csv'

CO_GRUPO = '4006'
co_category_public = ['1', '2', '3']
co_category_federal = '1'
co_region = '2'
co_uf = '25'

tags = ["NU_ANO","CO_CURSO","CO_IES","CO_CATEGAD","CO_ORGACAD","CO_GRUPO","CO_MODALIDADE","CO_MUNIC_CURSO","CO_UF_CURSO","CO_REGIAO_CURSO"]

def filter(ent_01, ent_02):
    read_file = pd.read_csv(ent_01)
    read_file.to_csv(ent_02, index=None)
    read_year = pd.read_csv(ent_02, header=None)
    print(read_year.head())

def csv_filter(entr, co_grupo, area):
    with open(entr, encoding='utf-8') as arquivo_referencia:
        table = csv.reader(arquivo_referencia, delimiter=';')
        table_two = []

        for l in table:
            # print(l)
            table_two.append(l)
            # table_two.append(l[0].__str__().split(";"))

        df = pd.DataFrame.from_records(table_two, columns=tags)
        print(len(df))

        filtered_df = df[df['CO_GRUPO'] == co_grupo]
        print(len(filtered_df))
        if area == 'public':
            filtered_df = filtered_df[filtered_df['CO_CATEGAD'].isin(co_category_public)]
        if area == 'federal':
            filtered_df = filtered_df[filtered_df['CO_CATEGAD'] == co_category_federal]
        if area == 'ne':
            filtered_df = filtered_df[filtered_df['CO_REGIAO_CURSO'] == co_region]
        if area == 'pb':
            filtered_df = filtered_df[filtered_df['CO_UF_CURSO'] == co_uf]
        print(filtered_df)
        filtered_df.to_csv(filter_year_csv)

filter(read_file, read_file_01)
csv_filter(read_file_01, CO_GRUPO, '')

