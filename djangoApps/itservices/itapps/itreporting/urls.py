from django.urls import path
from . import views
from .views import PostListView, PostListView2, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from django.urls import reverse

urlpatterns = [
    path('', views.home, name = 'itreporting-home'),
    path('about/', views.about, name = 'itreporting-about'),
    path('products/', PostListView2.as_view(), name = 'itreporting-products'),
    path('review/<int:pk>', PostDetailView.as_view(), name = 'review-detail'),
    path('review/new/', PostCreateView.as_view(), name = 'review-create'),
    path('review/<int:pk>/update/', PostUpdateView.as_view(), name = 'review-update'),
    path('review/<int:pk>/delete/', PostDeleteView.as_view(), name = 'review-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'itreporting-userreview'),
    path('contact/', views.contact, name = 'itreporting-contact'),
    



]
