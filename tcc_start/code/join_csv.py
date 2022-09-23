import pandas as pd


def join_csv(file_one, file_two, output):
    df1 = pd.DataFrame(file_one)
    df3 = pd.DataFrame(file_two)
    result = pd.concat([df1, df3], axis=1, join='inner')
    result.to_csv(output)


csv_2017 = "../datas/relação termas por disciplinas - 2017.csv"
csv_2021 = "../datas/relação termas por disciplinas - 2021.csv"

csv_2017_prov = "../datas/result_si_2017.csv"
csv_2021_prov = "../datas/result_si_2021.csv"

join_2017 = "../datas/join_2017.csv"
join_2021 = "../datas/join_2021.csv"

df_csv_2017 = pd.read_csv(csv_2017)
df_csv_2021 = pd.read_csv(csv_2021)

df_csv_2017_prov = pd.read_csv(csv_2017_prov)
df_csv_2021_prov = pd.read_csv(csv_2021_prov)

join_csv(df_csv_2017_prov, df_csv_2017, join_2017)
join_csv(df_csv_2021_prov, df_csv_2021, join_2021)

