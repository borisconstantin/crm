from django.shortcuts import render, redirect
from api.crm import get_all_user, User

# Create your views here.
def index(request):
    context = {"users": get_all_user()}
    return render(request, "contact/index.html", context=context)

def add_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    address = request.POST.get("address")
    phone_number = request.POST.get("phone_number")

    user = User(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number)
    user.save()

    return redirect("index")

def delete_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    address = request.POST.get("address")
    phone_number = request.POST.get("phone_number")

    user = User(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number)
    user.delete()

    return redirect("index")