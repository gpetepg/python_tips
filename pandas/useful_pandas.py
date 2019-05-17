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
    """
    
    :param table_name: str; Name of the table you want to copy into a DataFrame
    :param db_uri: str; Database connection string
    :param echo: bool; True if you want to see the sql, False if not
    :return: copied_dataframe; pd.DataFrame
    """
    metadata = MetaData()
    engine = create_engine(
        db_uri,
        echo=echo,  # Set True to see raw SQL
    )

    connection = engine.connect()
    table = Table(table_name, metadata, autoload=True, autoload_with=engine)
    result = connection.execute(table.select())
    result_list = [row for row in result]
    copied_dataframe = pd.DataFrame(result_list, columns=table.columns.keys())
    return copied_dataframe


def add_addtional_columns(dataframe_needing_cols, list_of_cols):
    """
    
    :param dataframe_needing_cols: pd.DataFrame; DataFrame needing columns added
    :param list_of_cols: list(); List of the columns to be added
    :return: datafame_with_cols_added; pd.DataFrame
    """
    datafame_with_cols_added = pd.concat([
        dataframe_needing_cols,
        pd.DataFrame([
            [np.nan] * len(list_of_cols) for col_names in range(dataframe_needing_cols.shape[0])],
            dataframe_needing_cols.index,
            list_of_cols)],
        axis=1
    )
    return datafame_with_cols_added

def subset_of_df(df, row_names=None, col_names=None):
    """
    
    :param df: pd.DataFrame; DataFrame to be subsetted
    :param row_names: list(); List of the rows to include in subset
    :param col_names: col_names; list(); List of the columns to include in subset
    :return: df; pd.DataFrame: Subset of original DataFrame
    """
    subset_df = df[col_names].loc[row_names]
    return subset_df


def apply_function(df, function, row_or_col=None, rows_or_cols=None):
    """
    
    :param df: pd.DataFrame; DataFrame to perform function on
    :param function: function(); The function to be applied
    :param row_or_col: str; Choose if row or col is to be performed on
    :param rows_or_cols: list(); List of the rows or columns to apply the function to
    :return: df; pd.DataFrame: DataFrame with the function applied to the desired rows or columns
    """
    if row_or_col == "col".lower():
        df[rows_or_cols] = df[rows_or_cols].apply(function)
        return df
    elif row_or_col == "row".lower():
        df.loc[rows_or_cols] = df.loc[rows_or_cols].apply(function)
        return df
    else:
        return "Invalid: Select row or col"

#####

"""
df = pd.read_csv("grades.csv")

aggregation = {
    "grades" : {. # Which column to work on
        "highest gread" : "max" # We give a name to the aggregate column and what function we want applied there
    }
}

# Add our where, groupby and aggregation
newdf = df[df["last_name"] == "Guo"].groupby("month").agg(aggregation)

# We ravel() to join the newly named column with the aggregation function for readability
newdf.columns = ["_".join(col) for col in newdf.columns.ravel()]

# We reset it to make it look pretty like Manda
newdf.reset_index()


Find column and row and assign it
t.loc[(t["ID"] == 1938), "BATCHID"] = [1,2,3,4]
"""
