from django.shortcuts import render
from .forms import errandsForm
from .models import errands
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'errands/index.html')

def create_errands(request):
    form = errandsForm()
    context = {'form': form}

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed',False)

        Errands=errands()
        
        errands.title = title
        errands.description = description
        errands.is_completed  = True if is_completed == "on" else False

        Errands.save()

        return HttpResponseRedirect(reverse("errands",kwargs={'id': errands.pk}))

    return render(request, 'errands/create-errands.html', context)

def errands_detail(request, id):
    return render(request, 'errands/errands-detail.html', {})
