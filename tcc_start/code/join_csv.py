import pandas as pd

def join_csv(file_one, file_two, output):
    df1 = pd.DataFrame(file_one)
    df3 = pd.DataFrame(file_two)
    result = pd.concat([df1, df3], axis=1, join='inner')
    result.to_csv(output)


csv_2017 = "../datas/relationship/relação termas por disciplinas - 2017.csv"
csv_2021 = "../datas/relationship/relação termas por disciplinas - 2021.csv"

# -------------------------
csv_2017_prov = "../datas/results/result_si_2017.csv"
csv_2021_prov = "../datas/results/result_si_2021.csv"

csv_2017_prov_brasil = "../datas/results/result_si_2017_brasil.csv"
csv_2021_prov_brasil = "../datas/results/result_si_2021_brasil.csv"

csv_2017_prov_public = "../datas/results/result_si_2017_public.csv"
csv_2021_prov_public = "../datas/results/result_si_2021_public.csv"

csv_2017_prov_federal = "../datas/results/result_si_2017_federal.csv"
csv_2021_prov_federal = "../datas/results/result_si_2021_federal.csv"

csv_2017_prov_NE = "../datas/results/result_si_2017_NE.csv"
csv_2021_prov_NE = "../datas/results/result_si_2021_NE.csv"

csv_2017_prov_PB = "../datas/results/result_si_2017_PB.csv"
csv_2021_prov_PB = "../datas/results/result_si_2021_PB.csv"

# ------------------------
join_2017 = "../datas/join/join_2017.csv"
join_2021 = "../datas/join/join_2021.csv"

join_2017_brasil = "../datas/join/join_2017_brasil.csv"
join_2021_brasil = "../datas/join/join_2021_brasil.csv"

join_2017_public = "../datas/join/join_2017_public.csv"
join_2021_public = "../datas/join/join_2021_public.csv"

join_2017_federal = "../datas/join/join_2017_federal.csv"
join_2021_federal = "../datas/join/join_2021_federal.csv"

join_2017_NE = "../datas/join/join_2017_NE.csv"
join_2021_NE = "../datas/join/join_2021_NE.csv"

join_2017_PB = "../datas/join/join_2017_PB.csv"
join_2021_PB = "../datas/join/join_2021_PB.csv"

# ------------------------
df_csv_2017 = pd.read_csv(csv_2017)
df_csv_2021 = pd.read_csv(csv_2021)

# Rio Tinto
df_csv_2017_prov = pd.read_csv(csv_2017_prov)
df_csv_2021_prov = pd.read_csv(csv_2021_prov)

join_csv(df_csv_2017_prov, df_csv_2017, join_2017)
join_csv(df_csv_2021_prov, df_csv_2021, join_2021)

# Brasil
df_csv_2017_prov_brasil = pd.read_csv(csv_2017_prov_brasil)
df_csv_2021_prov_brasil = pd.read_csv(csv_2021_prov_brasil)

join_csv(df_csv_2017_prov_brasil, df_csv_2017, join_2017_brasil)
join_csv(df_csv_2021_prov_brasil, df_csv_2021, join_2021_brasil)

# Public
df_csv_2017_prov_public = pd.read_csv(csv_2017_prov_public)
df_csv_2021_prov_public = pd.read_csv(csv_2021_prov_public)

join_csv(df_csv_2017_prov_public, df_csv_2017, join_2017_public)
join_csv(df_csv_2021_prov_public, df_csv_2021, join_2021_public)

# Federal
df_csv_2017_prov_federal = pd.read_csv(csv_2017_prov_federal)
df_csv_2021_prov_federal = pd.read_csv(csv_2021_prov_federal)

join_csv(df_csv_2017_prov_federal, df_csv_2017, join_2017_federal)
join_csv(df_csv_2021_prov_federal, df_csv_2021, join_2021_federal)

# NE
df_csv_2017_prov_ne = pd.read_csv(csv_2017_prov_NE)
df_csv_2021_prov_ne = pd.read_csv(csv_2021_prov_NE)

join_csv(df_csv_2017_prov_ne, df_csv_2017, join_2017_NE)
join_csv(df_csv_2021_prov_ne, df_csv_2021, join_2021_NE)

# PB
df_csv_2017_prov_PB = pd.read_csv(csv_2017_prov_PB)
df_csv_2021_prov_PB = pd.read_csv(csv_2021_prov_PB)

join_csv(df_csv_2017_prov_PB, df_csv_2017, join_2017_PB)
join_csv(df_csv_2021_prov_PB, df_csv_2021, join_2021_PB)