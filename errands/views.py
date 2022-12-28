from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'errands/index.html')

def create_errands(request):
    return render(request, 'errands/create-errands.html')