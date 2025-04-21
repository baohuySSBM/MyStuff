import pandas as pd

path = "KonsolenTrend.csv"

daten = pd.read_csv(path, header=1)

daten.columns = daten.iloc[0]

daten= daten[1:]

daten.reset_index(drop=True, inplace=True)

daten.columns = ["Woche", "Playstation 5" , "Microsoft Xbox Series X" , "Nintendo Switch"]

print(daten.to_string(index=False))

daten.to_csv("konsolen_trends_bereinigt.csv", index=False)