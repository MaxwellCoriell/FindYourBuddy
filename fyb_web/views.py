from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from fyb_web.forms import UserForm
from fyb_web.forms import LostPetForm
from fyb_web.forms import FoundPetForm



def index(request):
    """
    Renders the index page with the most recent lost and found posts
    Author: Max Baldridge
    Arguments: request -- the full HTTP request object
    Returns: rendered view of the index page, with a display of recent posts
    """
    template_name = 'index.html'
    return render(request, template_name, {})


# Create your views here.
def register(request):
    """
    Handles the creation of a new user for authentication
    Author: Max Baldridge
    Arguments: request -- The full HTTP request object
    """

    # A boolean value for telling the template 
    # whether the registration was successful.
    # Set to False initially. 
    # Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        template_name = 'register.html'
        return render(request, template_name, {'user_form': user_form})


def login_user(request):
    """
    Handles the creation of a new user for authentication
    Author: Max Baldridge
    Arguments: request -- The full HTTP request object
    """

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username=request.POST['username']
        password=request.POST['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/')

        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")


    return render(request, 'login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')


@login_required
def lost_pet_post(request):
    """
    Purpose: to present the user with a form to upload information 
            about a pet they may have lost
    Author: Max Baldridge
    Arguments: request -- the full HTTP request object
    Returns: a form that lets a user upload a lost pet post
    """
    if request.method == 'GET':
        lost_pet_form = LostPetForm()
        template_name = 'posts/lost_create.html'
        return render(reuqest, template_name, {'lost_pet_form': lost_pet_form})

    elif request.method == 'POST':
        form_data = request.POST

        lp = LostPet(
            owner = request.user,
            name = form_data['name'],
            species = form_data['species'],
            breed = form_data['breed'],
            description = form_data['description'],
            reward = form_data['reward'],
        )
        lp.save()
        template_name = 'posts/success.html'
        return render(request, template_name, {})


def found_pet_post(request):
    return HttpResponse("Hello, world. You're on the found_pet_post page")
