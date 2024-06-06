import contants
import pandas as pd

file = contants.File
init_time = contants.StartTime
finish_time = contants.FinishTime


df = pd.read_csv(file,sep='\s+',names=['TimeStamp','Host 1','Host 2'])
df = df.sort_values(by = 'TimeStamp', ascending=True)

df['TimeStamp'] = pd.to_datetime(df['TimeStamp'],origin='unix')
df = df.set_index('TimeStamp')

df_date = df.loc[init_time:finish_time]
data = df_date.groupby('Host 1')['Host 2'].apply(list)

print(data)
