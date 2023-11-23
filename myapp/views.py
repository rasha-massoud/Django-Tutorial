from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'John Doe',
        'work': 'Developer',
        'experience': 20,
    }
    return render(request, 'index.html', context)
