from django.urls import path
from . import views
urlpatterns =[
path('home.html', views.home, name='itreporting-home'),
path('', views.home, name='itreporting-home'),
path('about.html', views.about, name='itreporting-about'),
path('contact.html', views.contact, name='itreporting-contact'),
path('products.html', views.products, name='itreporting-products'),
path('profile.html', views.profile, name='itreporting-profile'),

]
