"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Person
from .models import PersonTable
from .models import PersonForm
import app.people as people
from django.http import HttpResponseRedirect

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    user = request.user
    return render(
        request,
        'app/index.html',
        {
            'records':people.filter(request, user),
            'table':PersonTable(people.filter(request, user)),
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

#def directory(request):
#    assert isinstance(request, HttpRequest)
#    user = request.user
#    return render(
#        request,
#        'app/directory.html',
#        {
#            'records':people.filter(request, user),
#            'message' : 'Test message please ignore',
#            'title':'Directory',
#            'year':datetime.now().year,
#        }
#    )

def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            newPerson = form.save()
            return HttpResponseRedirect('/')
    else:
        form = PersonForm()
    return render(
        request,
        'app/add.html',
        {
            'title':'Add Record',
            'form':form,
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
