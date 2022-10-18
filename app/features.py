import featuretools as ft
import pandas as pd
import json
from woodwork.logical_types import Categorical

def feature_extraction(data):
    
    ''' Creating a pandas DataFrame '''

    df = pd.DataFrame.from_dict(data, orient="columns")
    df1 = pd.json_normalize(df['data'])
    df2 = pd.json_normalize(df1['loans'])

    final_df = pd.DataFrame()

    for i in range(len(df2)):
        temp_df = pd.DataFrame.from_dict(list(df2.iloc[i].dropna()), orient = 'columns')
        final_df = pd.concat([final_df, temp_df], ignore_index = True, axis = 0)



    final_df.insert(0, "transaction_ID", range(0, 151), True)


    final_df['transaction_ID'] = final_df['transaction_ID'].astype('int64')
    final_df['customer_ID'] = final_df['customer_ID'].astype('int64')
    final_df['loan_date'] = final_df['loan_date'].astype('datetime64[ns]')
    final_df['amount'] = final_df['amount'].astype('int64')
    final_df['fee'] = final_df['fee'].astype('int64')
    final_df['loan_status'] = final_df['loan_status'].astype('int64')
    final_df['term'] = final_df['term'].astype('category')
    final_df['annual_income'] = final_df['annual_income'].astype('int64')
    
    
    ''' Using the feature tools library to extract features '''
    es = ft.EntitySet(id="customer_data")

    

    es = es.add_dataframe(
        dataframe_name="transactions",
        dataframe=final_df,
        index="transaction_ID",
        logical_types={
            "term": Categorical,
        },
    )

    es.normalize_dataframe(base_dataframe_name ='transactions', new_dataframe_name ='customers', index = 'customer_ID')

    feature_matrix, feature_defs = ft.dfs(entityset=es, target_dataframe_name="customers", max_depth = 1)
    
    result = feature_matrix.to_json(orient="index")

    parsed = json.loads(result)
    json.dumps(parsed, indent=4)
    
    
    return parsed
