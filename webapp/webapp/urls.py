from django.contrib import admin
from django.urls import path
from contact import views as contact_views

urlpatterns = [
    path('', contact_views.index, name='index'),
    path('add/', contact_views.add_contact, name='add_contact'),
    path('delete/', contact_views.delete_contact, name='delete_contact'),
    path('admin/', admin.site.urls),
]