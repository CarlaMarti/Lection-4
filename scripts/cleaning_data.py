def clean_dataframe(df):
    
    print("\n\n\nI AM CLEANING!")
            
    df_cleaned = df.dropna()

    df_cleaned = df_cleaned.drop_duplicates()

    df = df_cleaned

    print("\n\n\nNew number of rows: ", len(df))
    
    return df
