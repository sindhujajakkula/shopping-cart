from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'product/home.html', context)


 


