from django.shortcuts import render
from .forms import errandsForm
from .models import errands
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    Errands = errands.objects.all()

    completed_count=Errands,filter(is_completed=True).count()
    incompleted_count=Errands,filter(is_completed=False).count()

    context = {'Errands' : Errands}
    return render(request, 'errands/index.html',context)

def create_errands(request):
    form = errandsForm()
    context = {'form': form}

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed',False)

        Errands=errands()
        
        Errands.title = title
        Errands.description = description
        Errands.is_completed  = True if is_completed == "on" else False

        Errands.save()

        return HttpResponseRedirect(reverse("errands",kwargs={'id': Errands.pk}))

    return render(request, 'Errands/create-errands.html', context)

def errands_detail(request, id):
    return render(request, 'Errands/errands-detail.html', {})
