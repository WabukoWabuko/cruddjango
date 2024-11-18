from django.shortcuts import render, redirect, get_list_or_404
from .models import TestUserCrud

# Create your views here.
# Read 
# def Index(request):
#     items = TestUserCrud.objects.all()
#     return render(request, "index.html", {"items": items})

# def Create(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         TestUserCrud.objects.create(name=name, email=email, password=password)
#         return redirect("index_page")
#     return render(request, "index.html")

# def Update(request, pk):
#     items = get_list_or_404(TestUserCrud, pk)
#     if request.method == "POST":
#         items.name = request.POST.get("name")
#         items.email = request.POST.get("email")
#         items.save()
#         return redirect("index_page")
#     return redirect(request, "index.html", {"items": items})

def Delete(request, pk):
    items = get_list_or_404(TestUserCrud, pk)
    if request.method == "POST":
        items.delete()
        return redirect("index_page")
    return render(request, "index.html", {"items": items})