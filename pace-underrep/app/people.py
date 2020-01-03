from .models import Person
from .models import Visibility
#from django.http import HttpRequest

def filter(request, person):

    if not request.user.is_authenticated:
        return Person.people.filter(visibility = Visibility.PUBLIC)
    else:
        records = Set()
        user = Person.people.get(user = request.user)
        
