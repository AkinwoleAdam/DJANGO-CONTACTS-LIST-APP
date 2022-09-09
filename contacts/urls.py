from django.urls import path
from . import views

#app_name = 'contacts'

urlpatterns = [
path('',views.index, name='index'),

path('add_contact/',views.addContact,name='add_contact'),

path('contact_profile/<str:pk>',views.contactProfile,name='contact_profile'),

path('edit_contact/<str:pk>',views.editContact,name='edit_contact'),

path('delete_contact/<str:pk>',views.deleteContact,name='delete_contact'),

]