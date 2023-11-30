from django.shortcuts import render, redirect,  get_object_or_404
from accounts.models import User
from accounts.forms import essaye, ProfilePicForm , UserForm
from django.contrib import messages


# from django.contrib.auth.models import User

def profile(request, pk):
    if request.user.is_authenticated:
            profile= User.objects.get(id=pk)
            return render ( request, "accounts/profile.html" , {"profile": profile})
   
    else:
        messages.success(request, ("You must be logged "))
        return redirect('login')
    
    
def update_user(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            current_user = User.objects.get(id=pk)  
                
            user_form= essaye(request.POST or None , request.FILES or None ,instance=current_user)
            profile_form= ProfilePicForm(request.POST or None ,request.FILES or None ,instance=current_user)
            
            
            if user_form.is_valid():
                user_form.save()
                
                
            if profile_form.is_valid():
                profile_form.save()
            
            messages.success(request, " Your profile is updated succefully! ") 
        else : 
            current_user = User.objects.get(id=pk)       
            user_form= essaye(instance=current_user)
            profile_form= ProfilePicForm(instance=current_user)

        return render ( request, "accounts/update_user.html" , {'user_form': user_form,'profile_form' : profile_form })
    else:
        messages.error(request, ("you must be logged "))
        return redirect('login')

def update_user_admin(request,user_id): 
    # superuser = User.objects.get(is_superuser=True)
    # request.user = superuser
    user2 = get_object_or_404(User, pk=user_id)

    if ((request.method == 'POST') & (request.user.is_superuser)):
        # Assuming you have a UserForm for updating user information
        form = UserForm(request.POST, instance=user2)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('accounts:list_users')
            # Redirect to a success page or perform any other required actions
    else:
        # Assuming you have a UserForm for updating user information
        form = UserForm(instance=user2)

    return render(request, 'accounts/update_user_byadmin.html', {'form': form, 'user2': user2})