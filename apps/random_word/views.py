from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    random_str = get_random_string(length=14)
    print random_str
    input = {
        "random_str": random_str
    }
    return render(request, 'random_word/index.html', input)

def generate(request):
    return redirect('/random_word')

def reset(request):
    request.session['count'] = 0
    return redirect('/random_word')
