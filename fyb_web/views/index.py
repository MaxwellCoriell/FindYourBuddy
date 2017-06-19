from django.shortcuts import render


def index(request):
    """
    Purpose: Renders the index page with the most recent lost and found posts
    Author: Max Baldridge
    Arguments: request -- the full HTTP request object
    Returns: rendered view of the index page, with a display of recent posts
    """

    if request.method == 'GET':
        template_name = 'index.html'
        return render(request, template_name, {})