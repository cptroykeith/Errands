from django.shortcuts import render
from .forms import errandsForm
from .models import errands
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def get_showing_Errands(request, Errands):

    if request.GET and request.GET.get('filter'):
        if request.GET.get('filter') == 'complete':
            return Errands.filter(is_completed=True)
        if request.GET.get ('filter') == 'incomplete':
            return Errands.filter(is_completed=False)
    return Errands


@login_required
def index(request):
    Errands = errands.objects.filter(owner=request.user)

    completed_count = Errands.filter(is_completed=True).count()
    incomplete_count = Errands.filter(is_completed=False).count()
    all_count = Errands.count()

    incomplete_count = Errands.filter(is_completed=False).count()
    context = {'Errands' : get_showing_Errands(request, Errands), 'all_count' :all_count, 'completed_count': completed_count, 'incomplete_count': incomplete_count}
    return render(request, 'errands/index.html',context)

@login_required
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
        Errands.owner = request.user
        Errands.save()

        messages.add_message(request, messages.SUCCESS, "Errands created successfully")

        return HttpResponseRedirect(reverse("errands",kwargs={'id': Errands.pk}))

    return render(request, 'Errands/create-errands.html', context)

@login_required
def errands_detail(request, id):
    Errands = get_object_or_404(errands, pk=id)
    context = {'errands': Errands}
    return render(request, 'errands/errands-detail.html', context)
@login_required
def errands_delete(request, id):
    Errands = get_object_or_404(errands, pk=id)
    context = {'errands': Errands}

    if request.method == 'POST':
        if Errands.owner == request.user:
            Errands.delete()

            messages.add_message(request, messages.SUCCESS, "Errands Deleted")

            return HttpResponseRedirect(reverse('home'))
    return render(request, 'errands/errands-delete.html', context)

@login_required
def errands_edit(request,id):
    Errands = get_object_or_404(errands, pk=id)
    form=errandsForm(instance=Errands)
    context = {'errands': Errands, 'form':form}

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed',False)

    
         
        Errands.title = title
        Errands.description = description
        Errands.is_completed  = True if is_completed == "on" else False

        if Errands.owner == request.user:
         Errands.save()

        messages.add_message(request, messages.SUCCESS, "Errands update success")

        return HttpResponseRedirect(reverse("errands",kwargs={'id': Errands.pk}))


    return render(request, 'errands/errands-edit.html', context)
