from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'John Doe',
        'work': 'Developer',
        'experience': 20,
    }
    return render(request, 'index.html', context)

def wordCounter(request):
    return render(request, 'wordCounter.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})