from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from accounts.models import User

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form":form})

def account_view(request):
    if request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": True, "username": request.user.username})
    else:
        return JsonResponse({"isAuthenticated": False})
    
def get_attributes(request):
    if request.user.is_authenticated:
        user_attributes = {
            "username": request.user.username
        }
    else:
        user_attributes = {"error": "User is not logged in."}
    
    
    return JsonResponse(user_attributes)

def delete_account(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()
        return redirect('homepage')
    return redirect('login')

    