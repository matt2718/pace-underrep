"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Person
import app.people as people

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def directory(request):
    assert isinstance(request, HttpRequest)
    user = request.user
    return render(
        request,
        'app/directory.html',
        {
            'records':people.filter(request, user),
            'title':'Directory',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Ramapriya\'s contact page.',
            'year':datetime.now().year,
        }
    )

#def about(request):
#    """Renders the about page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/about.html',
#        {
#            'title':'About',
#            'message':'Your application description page.',
#            'year':datetime.now().year,
#        }
#    )
