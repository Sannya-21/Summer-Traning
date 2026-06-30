from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            if User.objects.filter(username=username).exists():

                messages.error(request, "Username already exists")
                return redirect("register")

            if User.objects.filter(email=email).exists():

                messages.error(request, "Email already exists")
                return redirect("register")

            user = User.objects.create_user(

                username=username,

                first_name=form.cleaned_data['first_name'],

                last_name=form.cleaned_data['last_name'],

                email=email,

                password=form.cleaned_data['password']

            )

            profile = form.save(commit=False)

            profile.user = user

            profile.save()

            messages.success(request, "Account Created Successfully")

            return redirect("login")

    else:

        form = RegisterForm()

    return render(

        request,

        "authentication/register.html",

        {

            "form": form

        }

    )


def login_view(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, "authentication/login.html")


def dashboard(request):

    if not request.user.is_authenticated:

        return redirect("login")

    return render(request, "authentication/dashboard.html")


def logout_view(request):

    logout(request)

    return redirect("login")