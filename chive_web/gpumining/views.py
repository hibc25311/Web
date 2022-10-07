from django.shortcuts import render
from .models import GPU


# Create your views here.
def gpumining(request):
    gpus = GPU.objects.all().order_by('-profit')
    return render(request, 'gpumining/gpumining.html', {'gpus': gpus})
