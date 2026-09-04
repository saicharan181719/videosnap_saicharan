from re import A
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
import math
from .models import (
    Profile,
    Education,
    Experience,
    Skill,
    Project,
    Certification,
    Position,
    Service,
    CareerBreak,
    Language,
)
User=get_user_model()

# Create your views here.
def index(request):
	return render(request, "accounts/index.html")

@login_required
def dashboard(request):
	return render(request, "accounts/dashboard.html")

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect("signup")
                    
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("index")

    return render(request, "accounts/signup.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")

            next_url = request.GET.get("next")
            return redirect(next_url or "index")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "accounts/login.html")

def contactus(request):
	return render(request, "accounts/contactus.html")

def forgotpass(request):
    return render(request,"accounts/forgotpass.html")

def resetpass(request):
    return render(request,"accounts/resetpass.html")

def profile(request):
    return render(request,"accounts/profile.html")

def editprofile(request):
    return render(request,"accounts/editprofile.html")

def faq(request):
    return render(request,"accounts/faq.html")

def privacypolicy(request):
    return render(request,"accounts/privacypolicy.html")

def tandc(request):
    return render(request,"accounts/tandc.html")

def features(request):
    return render(request,"accounts/features.html")

def services(request):
    return render(request,"accounts/services.html")

def testimonials(request):
    return render(request,"accounts/testimonials.html")

def helpcentre(request):
    return render(request,"accounts/helpcentre.html")

def blog(request):
    return render(request,"accounts/blog.html")

def news(request):
    return render(request,"accounts/news.html")

def cookie(request):
    return render(request,"accounts/cookie.html")

def accessibility(request):
    return render(request,"accounts/accessibility.html")

def careers(request):
    return render(request,"accounts/careers.html")

def partners(request):
    return render(request,"accounts/partners.html")    

def community(request):
    return render(request,"accounts/community.html")    

def events(request):
    return render(request,"accounts/events.html")   

def releasenotes(request):
    return render(request, "accounts/releasenotes.html") 

def roadmap(request):
    return render(request, "accounts/roadmap.html") 

def about(request):
    return render(request,"accounts/about.html")

@login_required
def logout_view(request):
     logout(request)
     messages.success(request, "Logged out successfully.")
     return redirect("login")

def ad(request):
    if request.method == "POST":
        AValue = int(request.POST.get("AValue", ""))
        BValue = int(request.POST.get("BValue", ""))
        CValue = AValue+BValue
        print(CValue)
        return render(request,"accounts/ad.html",{"AValue":AValue,"BValue":BValue,"CValue":CValue})
        
    return render(request,"accounts/ad.html")

def sub(request):
    if request.method == "POST":
        AValue = int(request.POST.get("AValue", ""))
        BValue = int(request.POST.get("BValue", ""))
        CValue = int(AValue-BValue)
        print(CValue)
        return render(request,"accounts/sub.html",{"AValue":AValue,"BValue":BValue,"CValue":CValue})
    return render(request,"accounts/sub.html")

def mul(request):
    if request.method == "POST":
        AValue = int(request.POST.get("AValue", ""))
        BValue = int(request.POST.get("BValue", ""))
        CValue = int(AValue*BValue)
        print(CValue)
        return render(request,"accounts/mul.html",{"AValue":AValue,"BValue":BValue,"CValue":CValue})
    return render(request,"accounts/mul.html")
    
def div(request):
    if request.method == "POST":
        AValue = int(request.POST.get("AValue", ""))
        BValue = int(request.POST.get("BValue", ""))
        CValue = int(AValue/BValue)
        print(CValue)
        return render(request,"accounts/div.html",{"AValue":AValue,"BValue":BValue,"CValue":CValue})
    return render(request,"accounts/div.html")

def sqrt(request):
    if request.method == "POST":
        AValue = int(request.POST.get("AValue", ""))
        BValue = int(request.POST.get("BValue", ""))
        CValue = math.sqrt(AValue),math.sqrt(BValue)
        print(CValue)
        return render(request,"accounts/sqrt.html",{"AValue":AValue,"BValue":BValue,"CValue":CValue})
    return render(request,"accounts/sqrt.html")

@login_required
def profile_view(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    context = {
        "profile": profile,
        "educations": Education.objects.filter(user=request.user),
        "experiences": Experience.objects.filter(user=request.user),
        "skills": Skill.objects.filter(user=request.user),
        "projects": Project.objects.filter(user=request.user),
        "certifications": Certification.objects.filter(user=request.user),
        "positions": Position.objects.filter(user=request.user),
        "services": Service.objects.filter(user=request.user),
        "career_breaks": CareerBreak.objects.filter(user=request.user),
        "languages": Language.objects.filter(user=request.user),
    }

    return render(request, "accounts/profile.html", context)


@login_required
def edit_profile_view(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        profile.about = request.POST.get("about")
        profile.city = request.POST.get("city")
        profile.district = request.POST.get("district")
        profile.state = request.POST.get("state")

        if request.FILES.get("profile_picture"):
            profile.profile_picture = request.FILES.get("profile_picture")

        profile.save()

        return redirect("profile")

    return render(
        request,
        "accounts/edit_profile.html",
        {
            "profile": profile
        }
    )


@login_required
def my_profile_view(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    context = {
        "profile": profile,
        "educations": Education.objects.filter(user=request.user),
        "experiences": Experience.objects.filter(user=request.user),
        "skills": Skill.objects.filter(user=request.user),
        "projects": Project.objects.filter(user=request.user),
        "certifications": Certification.objects.filter(user=request.user),
        "positions": Position.objects.filter(user=request.user),
        "services": Service.objects.filter(user=request.user),
        "career_breaks": CareerBreak.objects.filter(user=request.user),
        "languages": Language.objects.filter(user=request.user),
    }

    return render(request, "accounts/my_profile.html", context)


@login_required
def add_details_view(request):

    return render(request, "accounts/add_details.html")
