from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Anasayfa görünümü
def index(request):
    return render(request, "home.html")

# Ana içerik görünümü
def home(request):
    data = {
        "welcome_message": "Wise Projesine Hoş Geldiniz!"
    }
    return render(request, "home.html", data)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User

# Giriş görünümü
def login(request):
    form = LoginForm(data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
        if user is not None:
                 auth_login(request, user)
                 return redirect("panel")  # Başarılı giriş sonrası yönlendirme
        else:
                # Kullanıcı doğrulanamadıysa hata mesajı ekleyin
                return render(request, "login.html", {"form": form, "error": "User not found or invalid credentials."})

    return render(request, "login.html", {"form": form})


# Kayıt görünümü
def register(request):
    form = SignupForm(data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")  # Başarılı kayıt sonrası giriş sayfasına yönlendirme

    return render(request, "register.html", {"form": form})


# Kullanıcı çıkış görünümü
def logout(request):
    auth_logout(request)  # Kullanıcının oturumunu kapat
    return redirect('/')  # Çıkış sonrası anasayfaya yönlendirme
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Dashboard after login
@login_required
def panel(request):
    # Features available in the project
    features = [
        {"id": 1, "name": "Food Waste Analysis"},
        {"id": 2, "name": "Data Upload"},
        {"id": 3, "name": "Reporting"},
        {"id": 4, "name": "Management Strategies"},
    ]
    return render(request, "panel.html", {"features": features})

# Feature detail page
@login_required
def feature_detail(request, feature_id):
    # Feature details loaded dynamically
    feature_details = {
        1: "This feature analyzes food waste.",
        2: "This feature allows users to upload food data.",
        3: "This feature generates reports for management.",
        4: "This feature suggests strategic solutions.",
    }
    detail = feature_details.get(feature_id, "This feature is not available.")
    return render(request, "feature_detail.html", {"detail": detail})

def view_results(request):
    return render(request, "view_results.html")  # "results.html" şablonunu çağırır

def view_graphs(request):
    return render(request, "view_graphs.html")  # "results.html" şablonunu çağırır

def upload_images(request):
    return render(request, "upload_images.html")  # "results.html" şablonunu çağırır
def genarate_report(request):
    return render(request, "genarate_report.html")  # "results.html" şablonunu çağırır
