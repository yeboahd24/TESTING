# Django has a built-in authentication system that works great.
# For example, if you are handling double confirmation email and
# you do not want to allow users without a verified email address to log into
# your application, you can do something like this:

# forms.py:
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm (AuthenticationForm):
    def confirm_login_allowed (self, user):
        if not user.is_active or not user.is_validated:
            raise forms.ValidationError ('There was a problem with your login.', code = 'invalid_login')

# urls.py:
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .forms import CustomAuthenticationForm

urlpatterns = [
    url (r '^ login / $', auth_views.login, {'template_name': 'core / login.html',
        'authentication_form': CustomAuthenticationForm}, name = 'login'),
    url (r '^ logout / $', auth_views.logout, name = 'logout'),
    ...
]

# It is mostly just a matter of overriding the confirm_login_allowed method
# and replacing the authentication_form parameter with a new form in the urlconf.
# You can add any login policy, and to invalidate the authentication just call ValidationError.

# For built-in login views, Django uses the django.contrib.auth.forms.AuthenticationForm to handle 
# the authentication process. 
# It mainly checks for username, password and is_active.
# Django makes it easy to add custom validations because the 
# AuthenticationForm has a method named confirm_login_allowed (user). 