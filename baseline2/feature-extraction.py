import time
import pickle
import pandas as pd
from datetime import datetime
from scipy.stats import entropy

def get_features(df, time_str):
    """
    Params
    -------------
    df: dataframe to extract features
    time_str: end datetime to extract period 
    i1: # of total edits
    i2: avg. # of edits per item
    i3: # of items edited
    i4: # of seconds between first/last edits
    i5: diversity of types of edits
    
    Return
    -------------
    extracted feature df for ML
    """

    end_time_str = time_str
    #periods = [1.,2.,3.,4.,5.,6.,7.,8.,9.,10.]
    feature_df_list = list()
    for p in range(10):
        temp_df_list = list()
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
        start_time = (end_time - pd.Timedelta(30., unit='D')).strftime('%Y-%m-%d %H:%M:%S')
        
        # get subdf of the period p and stats
        stime = time.time()
        groupby = df[(df['time']>=start_time) & (df['time']<end_time_str)].groupby('user')
        num_edits = groupby['edittype'].agg(['count'])
        temp_df_list.append(num_edits)
        
        num_items = groupby['target'].agg(['nunique'])
        temp_df_list.append(num_items)
        
        min_max_edittime = groupby['time'].agg(['min','max'])
        min_max_edittime['min'] = pd.to_datetime(min_max_edittime['min'], format='%Y-%m-%d %H:%M:%S')
        min_max_edittime['max'] = pd.to_datetime(min_max_edittime['max'], format='%Y-%m-%d %H:%M:%S')
        min_max_edittime['daydiff'] = (min_max_edittime['max'] - min_max_edittime['min']).dt.seconds 
        temp_df_list.append(min_max_edittime)
    
        edittypes = groupby['edittype'].value_counts().to_frame()
        edittypes.columns = ['edittypecount']
        edittypes.reset_index(inplace=True)
        # print(edittypes)
        edittypes = edittypes.groupby('user')['edittypecount'].apply(entropy).to_frame()
        edittypes.columns = ['entropy']
        temp_df_list.append(edittypes)
        
        stats_df = pd.concat(temp_df_list, axis=1)
        #print(stats_df)
        
        print(start_time, end_time, '{}s to process...'.format(time.time()-stime))
        
        feature_df_list.append(stats_df)
        
        end_time_str = start_time # move to previous one month range
        
    return feature_df_list


mydateparser = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
df = pd.read_csv(
    '../data/filtered_data.csv', 
    delimiter='\t', 
    header=None, 
    names=['target','time','user','edittype'],
#     parse_dates=['time'], 
#     date_parser=mydateparser
)

# load train users
with open('../data/a_users_s2.data', 'rb') as filehandle:
    # store the data as binary data stream
    train_users = pickle.load(filehandle)
print(len(train_users))

# test
with open('../data/a_users_s3.data', 'rb') as filehandle:
    # store the data as binary data stream
    test_users = pickle.load(filehandle)
print(len(test_users))

# get sub df
sub_df = df[(df['user'].isin(train_users)) & (df['time']<'2020-02-07 15:48:42')] # 15min

# dump train feature dfs
feature_df_list = get_features(sub_df, '2020-02-07 15:48:42')

with open('../data/baseline2_testdf_list.pkl', 'wb') as f:
    pickle.dump(feature_df_list, f)
