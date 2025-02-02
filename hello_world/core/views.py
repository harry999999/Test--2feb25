from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def mysite(request):
    context = {
        "title": "Django Test",
    }
    return render(request, "mysite.html", context)

def about(request):
    content = {
        "title": "Django Test",
    }
    return render(request, "about.html", content)
