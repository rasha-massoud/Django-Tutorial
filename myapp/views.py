from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def basicIndex(request):
    context = {
        'name': 'John Doe',
        'work': 'Developer',
        'experience': 20,
    }
    return render(request, 'basicIndex.html', context)

def onlineTemplate(request):
    features = Feature.objects.all()
    return render(request, 'onlineTemplate.html', {'features': features})

def wordCounter(request):
    return render(request, 'wordCounter.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatedPassword = request.POST['repeatedPassword']

        if password == repeatedPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Mismatch Passwords.')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, email=email, password=password)            

        if user is not None:
            auth.login(request, user)
            return redirect('/resume')
        else:
            messages.info(request, 'Invalid Credentials.')    
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
