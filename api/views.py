# django imports
from django.shortcuts import render
# REST imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# other imports
import time


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

    # your code here
    print (word)

    # time taken by the code to process
    time_taken = time.process_time() - start_time

    # response message
    success = [{
            	"status": "success",
            	"data": {
            		"suggession_list": ["a", "aa", "aaa", "aassd"],
            		"time": time_taken
            	},
            }]

    return Response(success, status=status.HTTP_200_OK)
