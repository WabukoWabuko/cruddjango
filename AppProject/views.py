from django.shortcuts import render, redirect, get_object_or_404
from .models import PeopleM
from .forms import PeopleForm


# Create your views here.
def list(request):
    people = PeopleM.objects.all()
    return render(request, 'index.html', {'people': people})


def add(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_page')
    else:
        form = PeopleForm()
    return render(request, 'add.html', {'form': form})

def edit(request, person_id):
    person = get_object_or_404(PeopleM, id=person_id)
    
    if request.method == 'POST':
        form = PeopleForm(request.POST, request.FILES, instance=person)  
        if form.is_valid():
            form.save()  
            return redirect('list_page')  
    else:  
        form = PeopleForm(instance=person)
    
    return render(request, 'edit.html', {'form': form, 'person': person})


def delete(request, person_id):
    person = get_object_or_404(PeopleM, id=person_id)
    
    if request.method == 'POST':
        person.delete()  
        return redirect('list_page')  
    
    return render(request, 'confirmDelete.html', {'person': person})  
