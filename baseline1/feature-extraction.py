import time
import pickle
import pandas as pd
from datetime import datetime


def get_features(df, time_str):
    """
    Params
    -------------
    df: dataframe to extract features
    time_str: end datetime to extract period 
    
    Return
    -------------
    extracted feature df for ML
    """
    end_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    periods = [1./16, 1./8, 1./4, 1./2, 1., 2., 4., 12., 36., 108.]
    feature_df_list = list()
    for p in periods:
        start_time = (end_time - pd.Timedelta(30.*p, unit='D')).strftime('%Y-%m-%d %H:%M:%S')
        # get subdf of the period p and stats
        stime = time.time()
        if p != 108.:
            stats_df = df[df['time']>=start_time].groupby('user').agg(['min','max','count','nunique'])
        else:
            stats_df = df.groupby('user').agg(['min','max','count','nunique'])
        print(start_time, end_time, '{}s to process...'.format(time.time()-stime))
        feature_df_list.append(stats_df)
        
    return feature_df_list


mydateparser = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
df = pd.read_csv(
    'data/filtered_data.csv', 
    delimiter='\t', 
    header=None, 
    names=['target','time','user','edittype'],
#     parse_dates=['time'], 
#     date_parser=mydateparser
)

# load train users
with open('data/a_users_s2.data', 'rb') as filehandle:
    # store the data as binary data stream
    train_users = pickle.load(filehandle)
print(len(train_users))

# test
with open('data/a_users_s3.data', 'rb') as filehandle:
    # store the data as binary data stream
    test_users = pickle.load(filehandle)
print(len(test_users))

# get sub df
sub_df = df[(df['user'].isin(train_users)) & (df['time']<'2019-04-14 15:48:42')] # 15min

# dump train feature dfs
feature_df_list = get_features(sub_df, '2019-04-14 15:48:42')

with open('data/baseline1_traindf_list.pkl', 'wb') as f:
    pickle.dump(feature_df_list, f)
