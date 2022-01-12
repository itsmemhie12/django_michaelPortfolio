from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {'name': 'Michael', 'course':'Django' }
    return render(request, 'home.html', context)

def about(request):
    return HttpResponse("HI I AM MICHAEL!!")