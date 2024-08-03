from django.shortcuts import render, HttpResponse
import json
import urllib.request

def index(request):
    movies = []

    if request.method == 'POST':
        movie = request.POST.get('movie', '').capitalize()
        genre = request.POST.get('genre', '').capitalize()
        if movie:
            url = f'http://www.omdbapi.com/?s={movie}&apikey=c88dab6a'
            try:
                with urllib.request.urlopen(url) as response:
                    res = response.read()
                    json_data = json.loads(res)
                    if json_data.get('Response') == "True":
                        movies = json_data.get('Search', [])
                    else:
                        movies = []
            except urllib.error.URLError as e:
                print(f"Error fetching data: {e}")

    return render(request, 'index.html', {'movies': movies})

def search(request):
    movies = []

    if request.method == 'POST':
        genre = request.POST.get('genre', '').capitalize()
        if genre:
            url = f'http://www.omdbapi.com/?s={genre}&apikey=c88dab6a'
            try:
                with urllib.request.urlopen(url) as response:
                    res = response.read()
                    json_data = json.loads(res)
                    if json_data.get('Response') == "True":
                        movies = json_data.get('Search', [])
                    else:
                        movies = []
            except urllib.error.URLError as e:
                print(f"Error fetching data: {e}")

    return render(request, 'search.html', {'movies': movies})
