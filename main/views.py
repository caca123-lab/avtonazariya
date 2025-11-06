from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
def test(request):
    return render(request, 'main/test.html')
