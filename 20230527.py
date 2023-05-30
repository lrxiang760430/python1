import pandas as pd
df4g=pd.read_csv(r'C:\tools\sd\2023年5月份\4g_sd.csv',sep='^')
print(df4g)
df4g.to_csv(r'C:\tools\sd\2023年5月份\4g_sd_fl1.csv')