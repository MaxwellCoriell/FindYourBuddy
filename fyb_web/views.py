from django.shortcuts import render


# Create your views here.

# Use the login_required() decorator to ensure
# only those logged in can access the view.
# @login_required
# def view_account(request):
#     """
#     Purpose: When the user is logged in, they can view their account
#     Author: Max Baldridge
#     """
#     template_name = 'view_account.html'
#     if request.method == 'GET':
#         return(request, template_name)

#     if request.method == 'POST':
#         return render(request, template_name)


# @login_required
# def lost_pet_post(request):
#     """
#     Purpose: to present the user with a form to upload information
#             about a pet they may have lost
#     Author: Max Baldridge
#     Arguments: request -- the full HTTP request object
#     Returns: a form that lets a user upload a lost pet post
#     """
#     if request.method == 'GET':
#         lost_pet_form = LostPetForm()
#         template_name = 'posts/lost_create.html'
#         return render(reuqest, template_name, {'lost_pet_form': lost_pet_form})

#     elif request.method == 'POST':
#         form_data = request.POST

#         lp = LostPet(
#             owner = request.user,
#             name = form_data['name'],
#             species = form_data['species'],
#             breed = form_data['breed'],
#             description = form_data['description'],
#             reward = form_data['reward'],
#         )
#         lp.save()
#         template_name = 'posts/success.html'
#         return render(request, template_name, {})


# def found_pet_post(request):
#     return HttpResponse("Hello, world. You're on the found_pet_post page")
