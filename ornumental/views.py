from django.http import HttpResponse

def home_page(request):
    return HttpResponse("This is the main page")

def about_page(request):
    return HttpResponse("This is the about page")