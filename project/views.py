from django.shortcuts import render, redirect
from .models import Icecream
from .forms import IcecreamForm

# Create your views here.
def icecream_list(request):
    icecreams = Icecream.objects.all()
    return render(request, 'project/icecream_list.html', { 'icecreams': icecreams })

def icecream_detail(request, pk):
    icecream = Icecream.objects.get(id=pk)
    return render(request, 'project/icecream_detail.html', {'icecream': icecream })

def icecream_create(request):
    if request.method == 'POST':
        form = IcecreamForm(request.POST)
        if form.is_valid():
            icecream = form.save()
            return redirect('icecream_detail', pk=icecream.pk)
        
    else:
        form = IcecreamForm()
    return render(request, 'project/icecream_form.html', { 'form': form })

def icecream_edit(request, pk):
    icecream = Icecream.objects.get(pk=pk)
    if request.method == 'POST':
        form = IcecreamForm(request.POST, instance=icecream)
        if form.is_valid():
            icecream = form.save()
            return redirect('icecream_detail', pk=artist.pk)
    else:
        form = IcecreamForm(instance=icecream)
    return render(request, 'project/icecream_form.html', {'form':form})

def icecream_delete(request, pk):
    Icecream.objects.get(id=pk).delete()
    return redirect('icecream_list')