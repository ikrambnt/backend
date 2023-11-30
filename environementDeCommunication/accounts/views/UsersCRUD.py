from accounts.models import User
#import render
from django.shortcuts import render , redirect , get_object_or_404
from accounts.forms import essaye,ProfilePicForm, UserForm

#show the list of users
def list_users(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "calendarapp/dashboard.html", context) 

#modify the user
def modify_user(request,user_id): 
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        # Assuming you have a UserForm for updating user information
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to a success page or perform any other required actions
    else:
        # Assuming you have a UserForm for updating user information
        form = UserForm(instance=user)

    return render(request, 'accounts/modify-user.html', {'form': form, 'user': user})

#delete a user
def delete_user(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect("calendarapp:dashbord")