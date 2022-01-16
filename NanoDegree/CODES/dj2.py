# How to protect confidential information?

# Even when you run your application with DEBUG = False, 
# if it is configured to send bug reports by email, 
# there is a chance that bugs will be shown, especially if you are submitting them unencrypted.

# Don't add sensitive information directly to the settings.py file,
# use an environment variable or python-decouple instead.

# Speaking of filtering error reports, there are two decorators you can use:

# sensitive_variables
# If your code handles sensitive information in local variables inside a function,
# mark them as sensitive to avoid showing them in errors:

from django.views.decorators.debug import sensitive_variables

@sensitive_variables ('user', 'pw', 'cc')
def process_info (user):
    pw = user.pass_word
    cc = user.credit_card_number
    name = user.name
    ...

# Or, if you want to hide all local variables inside a function:
    
@sensitive_variables ()
def my_function ():
    ...

# PS: When using multiple decorators, make sure the @sensitive_variables () decorator is the first.

# sensitive_post_parameters

# Similar to the previous example, but this one handles publish parameters, as the name suggests:
from django.views.decorators.debug import sensitive_post_parameters

@sensitive_post_parameters ('pass_word', 'credit_card_number')
def record_user_profile (request):
    UserProfile.create (
        user = request.user,
        password = request.POST ['pass_word'],
        credit_card = request.POST ['credit_card_number'],
        name = request.POST ['name'],
    )
    ...

# Likewise, to hide all publish options:
@sensitive_post_parameters ()
def my_view (request):
    ...

# Read more about filtering confidential information in the official documentation. 