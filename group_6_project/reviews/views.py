from django.shortcuts import render
from .forms import LogInForm
# Create your views here.


def Login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            # TODO: authenticate user and redirect to home page
            pass
    else:
        form = LogInForm()
    return render(request, 'reviews/LogIn.html', {'form': form})