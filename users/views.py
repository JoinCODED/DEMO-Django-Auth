from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from users.forms import UserSigninForm, UserSignupForm

# Create your views here.
def signup(req):
    form = UserSignupForm()
    if req.method == "POST":
        form = UserSignupForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect("item_list")
    context = {"form": form}
    return render(req, "signup.html", context)

def signin(req):
    form = UserSigninForm()
    if req.method == "POST":
        form = UserSigninForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect("item_list")
    context = {"form": form }
    return render(req, "signin.html", context)

def signout(req):
    logout(req)
    return redirect("signin")