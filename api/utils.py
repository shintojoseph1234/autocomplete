# importing libraries
import pandas as pd


def sort_dataframe(df):
    '''
    Filter dataframe by word_length and sort in descending by count

    Parameters:
        df (dataframe)   : Input dataframe to sort.

    Returns:
        df: returns a dataframe
    '''
    # find the unique word length
    word_length_list = df['word_length'].drop_duplicates().tolist()

    # create a new datafarme
    df1 = pd.DataFrame()

    # for each in word_length_list
    for each in word_length_list:
        # extract by word length
        df2 = df[df['word_length'] == each]
        # sort in descending order
        df2 = df2.sort_values(by=['count'], ascending=False)
        # append to the df1 dataframe
        df1 = df1.append(df2, ignore_index=True)

    return df1
