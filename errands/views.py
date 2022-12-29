from django.shortcuts import render
from .forms import errandsForm
from .models import errands
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

def get_showing_Errands(request, Errands):

    if request.GET and request.GET.get('filter'):
        if request.GET.get('filter') == 'complete':
            return Errands.filter(is_completed=True)
        if request.GET.get ('filter') == 'incomplete':
            return Errands.filter(is_completed=False)
    return Errands

def index(request):
    Errands = errands.objects.all()

    completed_count = Errands.filter(is_completed=True).count()
    incomplete_count = Errands.filter(is_completed=False).count()
    all_count = Errands.count()

    incomplete_count = Errands.filter(is_completed=False).count()
    context = {'Errands' : get_showing_Errands(request, Errands), 'all_count' :all_count, 'completed_count': completed_count, 'incomplete_count': incomplete_count}
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

def errands_detail(request, id):
    Errands = get_object_or_404(errands, pk=id)
    context = {'errands': Errands}
    return render(request, 'errands/errands-detail.html', context)

def errands_delete(request, id):
    Errands = get_object_or_404(errands, pk=id)
    context = {'errands': Errands}

    if request.method == 'POST':
        Errands.delete()
        return HttpResponseRedirect(reverse('home'))
        
    return render(request, 'errands/errands-delete.html', context)

