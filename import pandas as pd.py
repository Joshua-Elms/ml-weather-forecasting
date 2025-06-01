import pandas as pd
import datetime 
data = "kbmg.csv"
df = pd.read_csv(data, quotechar='"', skipinitialspace=True, header=0, delimiter=',', engine='python')
df = df[df["CALL_SIGN"].str.strip() == "KBMG"]
#Above already done
df = df[["DATE", "TMP"]]
df["DATE"] = pd.to_datetime(df["DATE"]).dt.round("h")
print(df[df["DATE"] == datetime.datetime(2021,6,19,23,0,0)].iat[0,1])