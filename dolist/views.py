from django.shortcuts import render

# Create your views here.
def index(reqeust):
    return render(request, 'dolist/index.html')