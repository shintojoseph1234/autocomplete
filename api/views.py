# django imports
from django.shortcuts import render

# REST imports
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# local imports
from api.utils import sort_dataframe

# other imports
import pandas as pd
import time
import os


# index page function
def index(request):
    # returns index.html template
    return render(request, 'index.html', {})


@api_view(['GET'])
def search(request, word):
    '''
    API endpoint that returns a list of suggestions
    for the input word.

    Parameters:
        word (str)   : Input word to search suggestions.

    Returns:
        list: returns a list with suggested words
    '''
    # record the start time
    start_time = time.process_time()
    # current path
    current_path = os.getcwd()
    # csv file path
    csv_path = current_path+"/media/csv/word_search.csv"
    # read the csv file
    df = pd.read_csv(csv_path, sep='\s+')
    # rename columns
    df.columns = ["word", "count"]
    # extract the subset containing the word
    subset_df = df[df.iloc[:,0].str.contains(word, regex=False, na=False)]
    # find the lengths of each word
    subset_df['word_length'] = subset_df['word'].str.len()
    # find the words starting with the required word
    subset_df["word_begning_value"] = subset_df["word"].str.startswith(word).astype(int)
    # find the words starting with the word
    word_begining_True = subset_df[subset_df['word_begning_value'] == 1].sort_values(by=['word_length'])
    # find the words not starting with the required word
    word_begining_False = subset_df[subset_df['word_begning_value'] == 0].sort_values(by=['word_length'])
    # sort dataframe according to or requirement
    result_1 = sort_dataframe(word_begining_True)
    # sort dataframe according to or requirement
    result_2 = sort_dataframe(word_begining_False)
    # append dataframes together
    result_1 = result_1.append(result_2, ignore_index=True)
    # convert word into list
    suggession_list = result_1['word'].tolist()
    # extract only 25
    suggession_list = suggession_list[:25]
    # time taken by the code to process
    time_taken = time.process_time() - start_time

    # response message
    success = [{
            	"status": "success",
            	"data": {
            		"suggession_list": suggession_list,
            		"time": time_taken
            	},
            }]

    return Response(success, status=status.HTTP_200_OK)
