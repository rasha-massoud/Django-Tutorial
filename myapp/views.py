from django.shortcuts import render

# Create your views here.
def basicIndex(request):
    context = {
        'name': 'John Doe',
        'work': 'Developer',
        'experience': 20,
    }
    return render(request, 'basicIndex.html', context)

def onlineTemplate(request):
    return render(request, 'onlineTemplate.html')

def wordCounter(request):
    return render(request, 'wordCounter.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})