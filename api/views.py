from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def welcome(request, *args, **kwargs):
    data = {
        "Welcome": "Welcome to the DemoApp API! \
To list the students check the /student/ \
and for the detailed view, check the \
/student/{id}/ which id is an integer"
    }
    return Response(data)
