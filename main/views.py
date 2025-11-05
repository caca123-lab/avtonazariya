from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def test(request):
    return render(request, 'main/test.html')
def webapp_home(request):
    return render(request, 'main/webapp_home.html')

def webapp_test(request):
    return render(request, 'main/webapp_test.html')

def webapp_practice(request):
    return render(request, 'main/webapp_practice.html')

def webapp_topics(request):
    return render(request, 'main/webapp_topics.html')

def webapp_results(request):
    return render(request, 'main/webapp_results.html')