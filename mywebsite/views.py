from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('<h1>Selamat datang di Home</h1>')

def index(request):
    context = {
        'judul' : 'Nyoba Django',
        'subjudul' : 'Selamat Datang',
        'nav' : [
            ['', 'Home'],
            ['/myApp', 'myApp'],
            ['/about', 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request, 'index.htm', context)