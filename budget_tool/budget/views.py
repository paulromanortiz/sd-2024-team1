from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'budget/home.html')

@login_required
def dashboard(request):
    notifications = [
"Welcome to the dashboard!",
"You have no new messages.",
]
    return render(request, 'budget/dashboard.html', {'notifications': notifications})