from django.http.response import HttpResponseRedirect
from .forms import MyForm
from django.shortcuts import get_object_or_404, render
from .models import Flower

# Create your views here.
def index(request):

    q = request.GET.get("q" , None)

    if q is None or q == '':
        flowers = Flower.objects.all()
    else:
        flowers = Flower.objects.filter(title__icontains=q)

        
    context = {
        'flowers':flowers,
    }
    return render(request, 'myapp/index.html', context)



def detail(request, slug=None):

    flower = get_object_or_404(Flower, slug=slug)
    context = {
        'flower': flower
    }

    return render(request, 'myapp/detail.html', context)


def tags(request, slug=None):
    
    flowers = Flower.objects.filter(tags__slug=slug)
    context = {
        'flowers': flowers
    }
    return render(request, 'myapp/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
        context = {
        'form': form
        }
        return render(request, 'myapp/edit.html', context)


def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = MyForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
        context = {
            'form': form
        }
        return render(request, 'myapp/edit.html', context)


def delete(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()
    return HttpResponseRedirect('/')