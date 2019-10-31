from django.shortcuts import render

# REST imports
from rest_framework.decorators import api_view

# Create your views here.

# index function
def index(request):
    # returns index.html template
    return render(request, 'index.html', {})



@api_view(['GET'])
def search(request, word):
    '''
    API endpoint that returns a list .
    Parameters:
        word (str)   : The destination port.
    Returns:
        list: returns a list with 
    Curl:
        curl -X GET -H 'Content-Type: application/json'  http://localhost:8000/api/search/word
    '''

    print (word)


    pass
