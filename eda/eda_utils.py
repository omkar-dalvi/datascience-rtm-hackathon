def get_null_percentage(df):
    return df.isnull().sum()/len(df) * 100