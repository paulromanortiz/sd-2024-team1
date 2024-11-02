from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'budget/home.html')
@csrf_exempt
@login_required
def dashboard(request):
    notifications = [
"Welcome to the dashboard!",
"You have no new messages.",
]
    return render(request, 'budget/dashboard.html', {'notifications': notifications})