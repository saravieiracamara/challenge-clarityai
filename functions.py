import pandas as pd
from datetime import datetime, timedelta
import contants

def convert_to_datetime(time):
    try: 
        if time.isnumeric():
            time = pd.to_datetime(time, unit='ms')
        return time
    except Exception as e:
        return e

def question1(file,init_time,finish_time,host_name):
    df = pd.read_csv(file,sep='\s+',names=['TimeStamp','Host 1','Host 2'] )
    df = df.sort_values(by = 'TimeStamp', ascending=True)

    df['TimeStamp'] = pd.to_datetime(df['TimeStamp'],origin='unix',unit='ms')
    df = df.set_index('TimeStamp')

    df = df[df['Host 1'] == host_name]
    df = df.loc[init_time:finish_time]
    data = df.groupby('Host 1')['Host 2'].apply(list)
    data = data.get(host_name, [])
    print('Host: ', host_name)
    print('Connection to Host {0}: '.format(host_name),data)
    return data

def question2(file,init_time,finish_time,host_name,connection):
    df = pd.read_csv(file,sep='\s+',names=['TimeStamp','Host 1','Host 2'] )
    df = df.sort_values(by = 'TimeStamp', ascending=True)

    df['TimeStamp'] = pd.to_datetime(df['TimeStamp'],origin='unix',unit='ms')
    df = df.set_index('TimeStamp')

    df = df[df['Host 1'] == host_name]
    df = df.loc[init_time:finish_time]
    data1 = df.groupby('Host 1')['Host 2'].apply(list)
    data1 = data1.get(host_name, [])
    print('Host: ', host_name)
    print('Connections to Host {0}: '.format(host_name),data1)
    print()


    df2 = df[df['Host 2'] == connection]
    df2 = df2.loc[init_time:finish_time]
    data2 = df2.groupby('Host 2')['Host 1'].apply(list)
    data2 = data2.get(connection, [])
    print('Connection: ', host_name)
    print('Hosts for the Connection {0}: '.format(host_name),data2)
    print()

    data3 = df.groupby('Host 1').count().sort_values(by = 'Host 2', ascending=False).index[0]
    print('Host with the most connections: ',data3)

    return data1,data2,data3


def select_time_frame(useCurrentTime_flag):
    if useCurrentTime_flag == True: 
        init_time = str(datetime.today())
        finish_time = str(datetime.today() - timedelta(hours=1))
    else:
        init_time = contants.StartTime2
        finish_time = contants.FinishTime2

    return init_time,finish_time
        



