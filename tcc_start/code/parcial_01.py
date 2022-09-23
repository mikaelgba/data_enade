
import pandas as pd

csv_2017 = "../datas/relação termas por disciplinas - 2017.csv"
csv_2021 = "../datas/relação termas por disciplinas - 2021.csv"

df = pd.read_csv(csv_2017)

list_comp = []

for i in df["objeto_de_conhecimento_numero"]:

    #if i.find(";"):
    print(i)

print(df)