from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            user_type = form.cleaned_data.get('user_type')
            print(username)
            print(user_type)
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def pagelogin(request):
  
    uservalue=''
    passwordvalue=''


#    valuenext= request.POST.get('next')

    form= Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(username=uservalue, password=passwordvalue)

        print(user.username)
        if user is not None and valuenext=='':
            login(request, user)

            context= {'form': form,
                      'valuenext': valuenext}

            messages.success(request, "You have successfully logged in")
            if user_type == "Seller":
                return redirect('blog-about')
            else:
                return redirect('blog-home')
'''
        if user is not None and valuenext !='':
            login(request, user)

	    messages.success(request, "You have successfully logged in")

            context= {'form': form,
                      'valuenext': valuenext}
            
            return redirect(valuenext)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'accounts/Login.html', context)

    else:
    
        
        context= {'form': form}
        return render(request, 'accounts/Login.html', context)
'''
'''
            if user_type == 'Seller':
                return redirect('blog-about')
            else:
                return redirect('blog-home')
'''
