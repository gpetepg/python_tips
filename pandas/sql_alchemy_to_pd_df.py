from sqlalchemy import (
    create_engine,
    MetaData,
    Table
)
import pandas as pd
import numpy as np

# https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
# https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)

def create_table_from_metadata(table_name, db_uri, echo=False):
    metadata = MetaData()
    engine = create_engine(
        db_uri,
        echo=echo,  # Set True to see raw SQL
    )

    connection = engine.connect()
    table = Table(table_name, metadata, autoload=True, autoload_with=engine)
    result = connection.execute(table.select())
    result_list = [row for row in result]
    df = pd.DataFrame(result_list, columns=table.columns.keys())
    return df


##### Add addtional columns #####

def add_addtional_columns(dataframe_needing_cols, list_of_cols):
    datafame_with_cols_added = pd.concat([
    dataframe_needing_cols,
    pd.DataFrame([
        [np.nan] * len(list_of_cols) for col_names in range(df.shape[0])],
        df.index,
        list_of_cols)],
        axis=1
    )
    return datafame_with_cols_added

#####