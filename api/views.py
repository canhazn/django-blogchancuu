from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List' : 'post-list',
        'Detail': 'post-detail'
    }
    return Response(api_urls)

