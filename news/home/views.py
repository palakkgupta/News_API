from django.shortcuts import render
import json
import requests
# Create your views here.
API_KEY = '7d9c4ed9c3784248a254e5a34052b16b'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
    else:

        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

    articles = data['articles']

    context = {
        'articles': articles
    }
    return render(request, 'home.html',context)
