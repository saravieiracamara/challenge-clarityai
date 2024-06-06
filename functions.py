import pandas as pd

def question1(file,init_time,finish_time,host_name):
    df = pd.read_csv(file,sep='\s+',names=['TimeStamp','Host 1','Host 2'])
    df = df.sort_values(by = 'TimeStamp', ascending=True)

    df['TimeStamp'] = pd.to_datetime(df['TimeStamp'],origin='unix')
    df = df.set_index('TimeStamp')

    df = df[df['Host 1'] == host_name]
    df = df.loc[init_time:finish_time]
    data = df.groupby('Host 1')['Host 2'].apply(list)

    return data