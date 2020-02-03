"""
Definition of urls for pace_underrep.
"""

from datetime import datetime
from django.urls import include, path, reverse_lazy
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.views.static import serve
from django_registration.backends.one_step.views import RegistrationView


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('add/', views.add, name='add'),
    #path('directory/', views.directory, name='directory'),
    path('accounts/login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    #path('register/', RegistrationView.as_view(success_url=reverse_lazy('home')), name='register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
