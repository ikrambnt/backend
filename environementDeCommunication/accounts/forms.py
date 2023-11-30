from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from accounts.models import User


class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    
    )

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        validators=[validate_password],
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ["email", "name", "surname","phone_number"]
        label = {"email": "Email Address",
                 "name": "Name",
                 "surname": "Surname",
                 "phone_number" : "Phone Number"}
        
        
        widgets = {"email": forms.EmailInput(attrs={"class": "form-control"}),
                   "name": forms.TextInput(attrs={"class": "form-control"}),
                   "surname": forms.TextInput(attrs={"class": "form-control"}),
                   "phone_number":forms.TextInput(attrs={"class": "form-control"})}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password didn't match!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class essaye(forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone_number"]
        label = {"phone_number": "Phone Number"}
        widgets = {"phone_number": forms.TextInput(attrs={"class": "form-control"})}
        # Set the required attribute of the field to False
        required = {"phone_number": False}


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture", required=False)
    class Meta:
        model = User
        fields = ["profile_image"]
        required = {"profile_image": False}
        
        widgets = {
            "profile_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control-file",
                    "accept": "image/*",
                    "aria-describedby": "profile-image-help",
                }
            )
        }
        help_texts = {
            "profile_image": "Select an image file (JPEG or PNG) to use as your profile picture.",
        }

        
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'phone_number','is_active' ]