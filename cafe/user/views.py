from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        error = False

        print(f_name, l_name, username, email, password)

        if User.objects.filter(username=username).exists():
            print("sic already registerd")
            messages.error(request, "sic already registerd")
            # return render(request,'user/signup.html')
            error = True

        if User.objects.filter(email = email).exists():
            print("email already registerd")
            messages.error(request, "email already registerd")
            # return render(request,'user/signup.html')
            error = True
        if error:
            return render(request,'user/signup.html')
        try:
            user = User.objects.create_user(
                first_name = f_name,
                last_name = l_name,
                username = username,
                email = email,
                password = password
            )
            user.save()
            messages.success(request,"sucessfully account created")
            print("user created")
            return redirect('sign_in')
        except Exception as e:
            print(e)

    return render(request,'user/signup.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        if user is not  None:
            login(request,user)
            return redirect('menu')
        else:
            messages.error(request,"invalid Credential")
    return render(request, 'user/sign_in.html')



def signout(request):
    logout(request)
    print("ithee")
    return redirect('sign_in')