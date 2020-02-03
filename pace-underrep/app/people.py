from .models import Person
from .models import Visibility
#from django.http import HttpRequest

def filter(request, person):
    records = Person.people.filter(visibility = Visibility.index("PUBLIC"))
    if not request.user.is_authenticated:
        #persons = Person.people.all()
        #persons = Person.people.filter(visibility = Visibility.PUBLIC);
        return records;
    else:        
        records.union(Person.people.filter(visibility = Visibility.index("AUTHED")))        
        try:
            user = Person.people.get(account = request.user)
            records.union(Person.people.filter(identities__in=user.identities.all()).exclude(id=user.pk).distinct())
        except Person.DoesNotExist:
            persons = None        
    return records
        
