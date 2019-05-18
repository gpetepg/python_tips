from sqlalchemy import (
    create_engine,
    MetaData,
    Table
)
import pandas as pd
import numpy as np

class UsefulPanda:
    
    def __init__(self, df):
        if type(df) == pd.core.frame.DataFrame:
            self.df = df
        else:
            raise TypeError("Invalid Type: Not a Pandas DataFrame")

    @staticmethod
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


    def add_addtional_columns(self, list_of_cols):
        """

        :param dataframe_needing_cols: pd.DataFrame; DataFrame needing columns added
        :param list_of_cols: list(); List of the columns to be added
        :return: datafame_with_cols_added; pd.DataFrame
        """
        dataframe_needing_cols = self.df
        datafame_with_cols_added = pd.concat([
            dataframe_needing_cols,
            pd.DataFrame([
                [np.nan] * len(list_of_cols) for col_names in range(dataframe_needing_cols.shape[0])],
                dataframe_needing_cols.index,
                list_of_cols)],
            axis=1
        )
        return datafame_with_cols_added

    def subset_of_df(self, row_names=None, col_names=None):
        """

        :param df: pd.DataFrame; DataFrame to be subsetted
        :param row_names: list(); List of the rows to include in subset
        :param col_names: col_names; list(); List of the columns to include in subset
        :return: df; pd.DataFrame: Subset of original DataFrame
        """
        subset_df = self.df[col_names].loc[row_names]
        return subset_df


    def apply_function(self, function, row_or_col=None, rows_or_cols=None):
        """

        :param df: pd.DataFrame; DataFrame to perform function on
        :param function: function(); The function to be applied
        :param row_or_col: str; Choose if row or col is to be performed on
        :param rows_or_cols: list(); List of the rows or columns to apply the function to
        :return: df; pd.DataFrame: DataFrame with the function applied to the desired rows or columns
        """
        applied_function_df = self.df
        if row_or_col == "col".lower():
            applied_function_df[rows_or_cols] = applied_function_df[rows_or_cols].apply(function)
            return applied_function_df
        elif row_or_col == "row".lower():
            applied_function_df.loc[rows_or_cols] = applied_function_df.loc[rows_or_cols].apply(function)
            return df
        else:
            raise ValueError('Invalid: Select "row" or "col"')
