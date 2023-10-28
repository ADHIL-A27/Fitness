from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Gallery,Attendence
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, "index.html")


def attendence(request):

    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer": SelectTrainer}

    if request.method=="POST":
        Login=request.POST.get("logintime")
        Logout=request.POST.get("logout")
        SelectWorkout=request.POST.get("selcworkout")
        TraineredBy=request.POST.get("Trainer")
        Logout=request.POST.get("logout")
        query=Attendence(Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TraineredBy=TraineredBy)
        query.save()
        messages.warning(request,"Attendence Applied Success")
        return redirect('/login')
       

    
    return render(request, "attendence.html",context)

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request, "gallery.html",context)


@login_required
def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')


    user_phone=9633362430
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendence=Attendence.objects.all()
    context={"posts":posts,"attendence":attendence}
    return render(request, "profile.html",context)

def signup(request):
    if request.method=="POST":
        username=request.POST.get("usernumber")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")
        if pass1!=pass2:
            messages.info(request,"Pasword is Not Matching")
            return redirect('/signup')
        
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
            
        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Creadentials")
            return redirect('/login')

    return render(request,"login.html")
    
    
def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/login')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()

        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
    return render(request,"contact.html")
   

    
def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')


    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership": Membership,"SelectTrainer": SelectTrainer}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        Trainers=request.POST.get('Trainer') 
        reference=request.POST.get('reference')
        adress=request.POST.get('adress')
        query=Enrollment(FullName=name,Email=email,Gender=gender,DOB=DOB,SelectTrainer=Trainers,
        SelectMembershipplan=member,Refernce=reference,Adress=adress,PhoneNumber=PhoneNumber)
        query.save()
        messages.success(request,"Now You Are Joined ,Happy Work Out..!!!! ")
        return redirect('/join')


    return render(request,"enroll.html",context)