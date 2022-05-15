def unique_counts(data):
    shape = data.shape
    null = data.isnull().sum()
    print("shape : ", shape)
    print("Null : ", null)
    cols_data = data.select_dtypes(['object'])
    for i in cols_data.columns:
        print("Unique values in", i, 'are : ')
        print(cols_data[i].value_counts())
        print('*'*50)
    return
  
