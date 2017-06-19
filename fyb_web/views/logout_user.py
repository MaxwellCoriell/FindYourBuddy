from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Use the login_required() decorator
# to ensure only those logged in can access the view.
@login_required
def logout_user(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    return HttpResponseRedirect('/')