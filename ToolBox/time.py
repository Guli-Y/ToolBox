import pandas as pd
import numpy as np

def get_time_features(df, column):
        # extract time features
        df.index = pd.to_datetime(df[column].str.replace(' UTC', ''), format='%Y-%m-%d %H:%M:%S')
        df.index = df.index.tz_localize('UTC').tz_convert('America/New_York')
        # year
        year = df.index.year
        df['scaled_year'] = (year-2011.5)/3.5 # data are from 2008-2015, scale the year to be in range(-1,1)
        # day of year
        day = df.index.dayofyear-1
        df['dayofyear_cos'] = np.cos(np.pi*day/365)
        df['dayofyear_sin'] = np.sin(np.pi*day/365)
        # day of week
        weekday = df.index.weekday
        df['weekday_cos'] = np.cos(np.pi*weekday/6)
        df['weekday_sin'] = np.sin(np.pi*weekday/6)
        # hour
        hour = df.index.hour
        minute = df.index.minute
        minutes = 60*hour+minute
        df['hour_cos'] = np.cos(np.pi*minutes/1440)
        df['hour_sin'] = np.sin(np.pi*minutes/1440)
        # reset index
        df = df.reset_index(drop=True)
        # select columns
        df = df[['scaled_year', 'dayofyear_cos', 'dayofyear_sin',
                        'weekday_cos', 'weekday_sin', 'hour_cos','hour_sin']]
        return df
