'''
   This file contains a basic code to 
   cleaning and preprocess for data

'''
import pandas as pd 
import numpy as np
def load_csv(path: str ) -> pd.DataFrame :
    '''
        this function created to read a csv_file that in path

        Args: path(str):a path that contain a file
        Return: pd.DataFrame : data after reading

    '''
    data =pd.read_csv(path)
    return data

def get_info(data : pd.DataFrame) -> None:
    ''' 
        if you want to show info of data with any number of columns
        Args: data(pd.DataFrame): a data that wanted to be shown its info
        Return: None
    '''
    data.info(verbose=True)

def get_shape(data:pd.DataFrame) ->tuple :
    '''
        this function to get a shape of the data to know the number ofrows and columns

        Args: data(pd.DataFrame):data that wanted to know its shape

        Return: tuple : tuple has(number of rows, number of columns)

    '''
    return data.shape

def explain_columns(netflix_data: pd.DataFrame)-> None:
    '''
        this function saved a explaining of columns
        Args: netflix_data(pd.DataFrame): this data that function saved its datails
        return : None :it will print the details of colunms only

    '''
    print("""
            - show_id → The index column; a unique identifier for each title on Netflix.
            - type → Indicates whether the title is a Movie or a TV Show.
            - title → The name of the movie or TV show.
            - director → The director(s) of the movie or TV show (may be NaN if unknown or not applicable).
            - cast → The main actors/actresses involved in the title (may be NaN if not provided).
            - country → The country or countries where the title was produced.
            - date_added → The date when the title was added to the Netflix catalog.
            - release_year → The year in which the movie or TV show was originally released.
            - rating → The content rating (e.g., PG-13, R, TV-MA) indicating suitability for audiences.
            - duration → For movies, shows the runtime in minutes; for TV shows, indicates the number of seasons.
            - listed_in → Categories or genres describing the title (e.g., Dramas, Comedies, Documentaries).
            - description → A short summary or synopsis of the movie or TV show.
    """)

def nna(column: pd.Series) -> int:
    """
    Count the number of missing (NaN) values in a given pandas Series.

    Args:
        column (pd.Series): The input pandas Series to check for missing values.

    Returns:
        int: The total number of NaN values in the Series.
    """
    number_of_null = column.isna().sum()
    return number_of_null


def indx_na(column: pd.Series) -> list:
    """
    Get the indices of missing (NaN) values in a given pandas Series.

    Args:
        column (pd.Series): The input pandas Series to check for missing values.

    Returns:
        list: A list of indices where the Series contains NaN values.
    """
    mask = column.isna()
    indx = mask[mask > 0].index.to_list()
    return indx

def most_popular_val(column : pd.Series , number_of_val) -> list :
    """
        Return the most frequent values from a given pandas Series.

        Args:
            column (pd.Series): The pandas Series (column of a DataFrame) to analyze.
            number_of_val (int): The number of top frequent values to return.

        Returns:
            list: A list containing the most frequent values in the Series,
            limited to the specified number_of_val.
    """
    popular_vals=column.value_counts().sort_values(ascending=False).index
    values=popular_vals[:number_of_val]
    return values

def handel_null ( data : pd.DataFrame ,column:str  ,use: str = ""  ) -> pd.DataFrame :
    """
    Handle missing values in a pandas DataFrame according to the given strategy.

    Args:
        data (pd.DataFrame): The input DataFrame to process.
        column (str): The column name to process
        use (str): The strategy to handle null values. Options could be:
                   - "drop": drop rows with NaN
                   - "fill_mean": fill NaN with column mean
                   - "fill_median": fill NaN with column median
                   - "fill_mode": fill NaN with column mode
                   
    Returns:
        pd.DataFrame: The DataFrame after applying the chosen strategy.
    """
    if (nna(data[column])>0 and use  == 'fill_mode') :
        mod=most_popular_val(data[column],1)[0]
        data[column].fillna(mod)

    elif (nna(data[column])>0 and use  == 'drop'):
        