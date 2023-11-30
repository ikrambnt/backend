from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.forms import SignInForm


class SignInView(View):
    """ User registration view """

    template_name = "accounts/signin.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            #if request.recaptcha_is_valid:
                email = forms.cleaned_data["email"]
                print(email)
                password = forms.cleaned_data["password"]
                print(password)
                user = authenticate(email=email, password=password)
                print(user)
                if user:
                    login(request, user)
                    return redirect("accounts:list_users")
            #else:
            #    forms.add_error(None, "Invalid CAPTCHA")
        context = {"form": forms}
        return render(request, self.template_name, context)
