from django.shortcuts import render

# Create your views here.
def index(request):
    print('====debug : client url http://127.0.0.1:8000/index, index() call ~~, render - index.html')
    return render(request, 'sample/index.html')

def generic(request):
    print('====debug : client url http://127.0.0.1:8000/generic, generic() call ~~, render - generic.html')
    return render(request, 'sample/generic.html')

def elements(request):
    print('====debug : client url http://127.0.0.1:8000/elements, elements() call ~~, render - elements.html')
    return render(request, 'sample/elements.html')

def map(request):
    print('====debug : client url ../map, map() call ~~, render - kakaoMap.html')
    return render(request, 'sample/kakaoMap.html')

def map2(request):
    print('====debug : client url ../map, map2() call ~~, render - map2.html')
    return render(request, 'sample/map2.html')

def enter(request):
    print('====debug : client url ../enter, enter() call ~~, render - test_enter.html')
    return render(request, 'sample/test_enter.html')