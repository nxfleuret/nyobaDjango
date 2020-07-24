from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Nyoba Django',
        'subjudul' : 'myApp',
        'nav' : [
            ['', 'Home'],
            ['/myApp/post', 'Post'],
            ['/myApp/stories', 'Stories']
        ]
    }

    return render(request, 'myApp/index.htm', context)
